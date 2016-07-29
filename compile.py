from __future__ import (absolute_import, division, print_function, unicode_literals)

"""
auto generate the table of contents for README.md and tag list in the tag.md
"""

import re
try:
    import mistune
    from lxml import etree
except ImportError as e:
    raise Exception("you need to install mistune and lxml package!")

filename = "./_posts.md"

with open(filename,'r') as f:
    readme = f.read().decode("utf-8")
    md = mistune.markdown(readme)
html = etree.HTML(md)
titles = html.xpath("//h2")
repoUrl = "https://github.com/AstroWheel/AstroWheel"
tagUrl = "https://github.com/AstroWheel/AstroWheel/blob/master/tags.md"

defaultPosts = ["post regulations", "some problems title", "table of contents"]
allPosts = []
allTags = {}
for eachH2 in titles:
    eachTitle = eachH2.text.strip()
    if eachTitle in defaultPosts:
        continue
    print("add: ", eachTitle)
    allPosts.append(eachTitle)
    nextLine = eachH2.getnext()
    while nextLine.tag[0] != "h":
        if nextLine.tag=="ul":
            allLi = nextLine.xpath("li")
            for eachLi in allLi:
                if eachLi.text[:5]=="tags:":
                    aux = eachLi.text[5:].split(",")
                    tags = [each.strip() for each in aux]
                    for eachTag in tags:
                        if allTags.has_key(eachTag):
                            allTags[eachTag].append(eachTitle)
                        else:
                            allTags[eachTag]=[eachTitle]
                    break
        nextLine = nextLine.getnext()

# make toble of contents
tableOfContentsDict = {eachPost:"* [{}]({}#{})\n".\
        format(eachPost, repoUrl,
               "-".join(eachPost.split())) \
        for eachPost in allPosts}
tableOfContents = [tableOfContentsDict[each] for each in allPosts]
tableOfContents.append("\n")

mark = re.findall(r"(## table of contents.*?[\S\s])##", readme, re.DOTALL)
assert len(mark)==1, "should not have string:'## table of contents\\n' more than one time in the README.md"
wholeFile = readme.split(mark[0])

newReadmeList = tableOfContents
newReadmeList.insert(0, "## table of contents\n")
newReadmeList.insert(0, wholeFile[0])
newReadmeList.append(wholeFile[1])

newReadme = "".join(newReadmeList)

with open("README.md",'w') as f:
    f.write(newReadme.encode("utf-8"))

# make tag file
tagList = list(allTags)
N = len(tagList)
tagList.sort()
tagListWithUrl = ["[{}]({}#{}) ".\
                    format(eachTag, tagUrl, "-".join(eachTag.split())) \
                    for eachTag in tagList]
tagListWithUrl.append("\n\n")

header="# Tags\n"
template = "## {}\n {}\n"
allH2 = [template.format(eachTag,
                "\n".join([tableOfContentsDict[eachTerm]
                    for eachTerm in allTags[eachTag]]))
            for eachTag in tagList]
allH2 = tagListWithUrl + allH2
allH2.insert(0, header)
tagFileContent = "".join(allH2)
with open("tags.md",'w') as f:
    f.write(tagFileContent.encode("utf-8"))
