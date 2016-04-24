### NEXT INDENTATION

![memes](https://cloud.githubusercontent.com/assets/8445924/10242439/65ce9baa-68e0-11e5-9d98-ba01a6c6e05e.jpg)

Do you wanna to go deeper?

- Use `IndentationGoUpShallower` if you wanna move cursor up and shallower.
- Use `IndentationGoUpDeeper` if you wanna move cursor up and deeper.
- Use `IndentationGoDownShallower` if you wanna move cursor up and shallower.
- Use `IndentationGoDownDeeper` if you wanna move cursor up and deeper.

.vimrc:
```
Plug 'kovetskiy/next-indentation'
    nnoremap gjh :IndentationGoUpShallower<CR>
    nnoremap gjl :IndentationGoUpDeeper<CR>
    nnoremap gkh :IndentationGoDownShallower<CR>
    nnoremap gkl :IndentationGoDownDeeper<CR>
```

I'm glad to share it with you.

![IndentationGoDown](https://cloud.githubusercontent.com/assets/8445924/10242333/a5a43f9c-68df-11e5-9096-033d680b645c.gif)
