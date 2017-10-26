py import indentation

"
func! IndentationGoUpPy (count)
    execute 'py indentation.go_next("up", "shallow", ' . count . ')'
endfunc

func! IndentationGoDownPy (count)
    execute 'py indentation.go_next("down", "deeper", ' . count . ')'
endfunc

func! IndentationSameUpPy (count)
    execute 'py indentation.go_same("up", ' . count . ')'
endfunc

func! IndentationSameDownPy (count)
    execute 'py indentation.go_same("down", ' . count . ')'
endfunc

command! -count=1 -nargs=?
            \ IndentationGoUp
            \ call IndentationGoUpPy(expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationGoDown
            \ call IndentationGoDownPy(expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationSameUp
            \ call IndentationSameUpPy(expand('<count>'))

command! -count=1 -nargs=?
            \ IndentationSameDown
            \ call IndentationSameDownPy(expand('<count>'))

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
