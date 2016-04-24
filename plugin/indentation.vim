py import indentation

"
func! IndentationGoUpPy (count)
    execute 'py indentation.go("up", "shallow", ' . count . ')'
endfunc

func! IndentationGoDownPy (count)
    execute 'py indentation.go("down", "deeper", ' . count . ')'
endfunc

command! -count=1 -nargs=?
            \ IndentationGoUp
            \ call IndentationGoUpPy(expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationGoDown
            \ call IndentationGoDownPy(expand('<count>'))

func! IndentationGo(line_direction, level_direction, count)
    execute 'py indentation.go(' .
        \ '"' . a:line_direction . '", ' .
        \ '"' . a:level_direction . '", ' .
        \ a:count . ')'
endfunc

command! -count=1 -nargs=?
            \ IndentationGoUpDeeper
            \ call IndentationGo("up", "deeper", expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationGoUpShallower
            \ call IndentationGo("up", "shallower", expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationGoDownDeeper
            \ call IndentationGo("down", "deeper", expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationGoDownShallower
            \ call IndentationGo("down", "shallower", expand('<count>'))
