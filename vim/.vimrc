filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab
set clipboard=unnamed
syntax on
set number
set noswapfile
set hlsearch 
set ignorecase 
set incsearch 
" Solarized color vim color setting
syntax enable
"set background=light
"let g:solarized_termcolors=256
"colorscheme solarized
"colorscheme monokai
"colorscheme sorbet
colorscheme retrobox
"the below was added for neovim/lazyvim, so might not need
let g:python3_host_prog = '/Library/Frameworks/Python.framework/Versions/3.11/bin/python3'
set backspace=indent,eol,start
filetype plugin indent on
set clipboard+=unnamedplus
