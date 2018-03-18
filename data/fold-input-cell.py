def doFold(max_height=200):
    '''define this function in your first input cell
       call it in the input cell you want to fold
       then you can fold the input cell like the output cell
    '''
    from IPython.display import HTML
    from IPython.display import display as Display
    randid = np.random.randint(9999999999)
    Display(HTML('''
    <style>
    .input_area {{
        overflow-y: scroll; 
    }}
    .foldable-cell:hover {{
        box-shadow: inset 0 0 1px #000;
        background: rgba(240, 240, 240, 0.5);
    }}
    .fold-cell {{
      border-radius: 2px;
      -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
      box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
    }}
    </style>
    <button id="code-{randid}" style="display:none;" onclick="marked_code_toggle(document.getElementById('code-{randid}'))">
        hide
    </button>'''.format(**locals()) + 
    '''
    <script>
        var max_input_cell_height = {}
        thisid = {}
    </script>
    '''.format(max_height, randid) +
    '''
    <script>
    (function () {
        var el = document.getElementById('code-'+thisid)
        while (($.inArray('code_cell', el.classList)<0)) {
            el = el.parentElement
        }
        var input_prompt = el.getElementsByClassName('input_prompt')[0]
        input_prompt.classList.add('foldable-cell')
        input_prompt.onclick = function () {
            marked_code_toggle(el)
        }
    })()
    </script>
    ''' + 
    '''
    <script>
    function marked_code_toggle(el) {
        while (($.inArray('code_cell', el.classList)<0)) {
            el = el.parentElement
        }
        var inputContainer = el.getElementsByClassName('input')[0]
        var inputEl = el.getElementsByClassName('input_area')[0]
        if (inputEl.style.height) {
            inputEl.style.height = ''
            inputContainer.classList.remove('fold-cell')
        } else {
            inputEl.style.height = max_input_cell_height + 'px'
            inputContainer.classList.add('fold-cell')
        }
    }
    </script>
    '''))
doFold()
