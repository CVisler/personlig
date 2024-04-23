" PLUGINS ---------------------------------------------------------------- {{{

call plug#begin('~/.vim/plugged')

  Plug 'dense-analysis/ale'

  Plug 'preservim/nerdtree'

call plug#end()

" }}}

" Filetype -------------------------------------------------------------- {{{
filetype on
filetype plugin on
filetype indent on
" }}}

" Visuals -------------------------------------------------------------- {{{
colorscheme retrobox
set relativenumber
syntax on
" }}}

" Generic -------------------------------------------------------------- {{{
set shiftwidth=4
set tabstop=4
set expandtab

set nobackup
set scrolloff=10 " Do not let cursor scroll below or above N number of lines when scrolling.
set nowrap
set incsearch " While searching though a file incrementally highlight matching characters as you type.
set ignorecase
set smartcase

set showcmd " Show partial command you type in the last line of the screen.
set showmode
set showmatch
set hlsearch
set history=1000
" }}}

" Other -------------------------------------------------------------- {{{
set wildmenu
set nocompatible
" }}}

" Code folding -------------------------------------------------------------- {{{
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END
" }}}
