#AstroWheel

All kinds of wheels for astronomers

## post regulations
* Each post need to have a brief title start with level 2 title "## some question"
* we can some meta data for this posts, like tags.
* Then submitter start a level 3 title with his or her name "### someone"
* and the last is your content.

Here is an example post.

## some problems about python
* tags: python, blabla, wheel
### by [someone](https://github.com/someone)
blablabla
blalbalba
here is the code
```markdown
## some problems about python
* tags: python, blabla, wheel
### by [someone](https://github.com/someone)
blablabla
blalbalba
here is the code
```

## prevent neglectful rm -rf
* tags: shell, rm

how to prevent neglectful rm -rf?

## by [Fmajor](https://github.com/someone/Fmajor)
* description: mv the things to ~/.trash/\<data-time\>
* disadvantages: you should clean your .trash using rmSure from time to time

code:
```
alias rmSure=/bin/rm
alias rm=trash
trash()
{
    tempDir=~/.trash/`date +%Y-%m-%d-%H-%M-%S`
    mkdir -p $tempDir
    mv -f $@ $tempDir
}
```
my trash:
![my trash](./image/my-trash.png "my trash")

## good use of git branch
* tags: git, github, version control

how to manage git branches efficiently?

## by [Fmajor](https://github.com/someone/Fmajor)

see
* [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
* [gg———good use of git,一个实用的git分支模型](http://fmajor.lamost.org/blog/2014/08/08/gg.html)
* [gg](https://github.com/Fmajor/gg)
* [gitflow](https://github.com/nvie/gitflow)

