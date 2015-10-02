py import indentation

func! IndentationGoUpPy (count)
 execute 'py indentation.go_up(' . count . ')'
endfunc

func! IndentationGoDownPy (count)
 execute 'py indentation.go_down(' . count . ')'
endfunc

command! -count=1 -nargs=? IndentationGoUp call IndentationGoUpPy(expand('<count>'))
command! -count=1 -nargs=? IndentationGoDown call IndentationGoDownPy(expand('<count>')) 
