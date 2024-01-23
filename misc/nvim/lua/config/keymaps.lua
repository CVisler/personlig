-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
local keymap = vim.keymap
local opts = { noremap = true, silent = true }

-- Select all
keymap.set({ "n", "v" }, "<C-a>", "0G<S-v>gg")

-- Move l up/down
keymap.set("v", "<M-j>", ":m '>+1<CR>gv=gv", opts)
keymap.set("v", "<M-k>", ":m '<-2<CR>gv=gv", opts)

-- Split screens
keymap.set("n", "<leader>sn", ":split<Return>", opts)
keymap.set("n", "<leader>sh", ":vsplit<Return>", opts)

-- Sticky up-pull of next row
vim.keymap.set("n", "J", "mzJ`z")

-- Sticky half-page jumping
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

-- Sticky search terms application
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Preserve register when pasting
vim.keymap.set("x", "<leader>p", [["_dP]])

-- Avoid cap-Q
vim.keymap.set("n", "Q", "<nop>")
vim.keymap.set("n", "<C-h>", "<Cmd>NvimTmuxNavigateLeft<CR>", { silent = true })
vim.keymap.set("n", "<C-j>", "<Cmd>NvimTmuxNavigateDown<CR>", { silent = true })
vim.keymap.set("n", "<C-k>", "<Cmd>NvimTmuxNavigateUp<CR>", { silent = true })
vim.keymap.set("n", "<C-l>", "<Cmd>NvimTmuxNavigateRight<CR>", { silent = true })
vim.keymap.set("n", "<C-\\>", "<Cmd>NvimTmuxNavigateLastActive<CR>", { silent = true })
vim.keymap.set("n", "<C-Space>", "<Cmd>NvimTmuxNavigateNavigateNext<CR>", { silent = true })
