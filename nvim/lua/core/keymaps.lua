-- Use CTRL+<hjkl> to switch between windows
vim.keymap.set("n", "<C-h>", "<C-w><C-h>", { desc = "Move focus to the left window" })
vim.keymap.set("n", "<C-l>", "<C-w><C-l>", { desc = "Move focus to the right window" })
vim.keymap.set("n", "<C-j>", "<C-w><C-j>", { desc = "Move focus to the lower window" })
vim.keymap.set("n", "<C-k>", "<C-w><C-k>", { desc = "Move focus to the upper window" })

-- Tab
vim.keymap.set("n", "<leader>tn", ":tabnew<CR>:Ex<CR>", { desc = "Create new tab" })
vim.keymap.set("n", "<leader>tx", ":tabclose<CR>", { desc = "Close current tab" })
vim.keymap.set("n", "<S-h>", ":tabp<CR>", { desc = "Move to previus tab" })
vim.keymap.set("n", "<S-l>", ":tabn<CR>", { desc = "Move to next tab" })
vim.keymap.set("n", "<leader>to", ":tabo<CR>", { desc = "Close all tabs except the current one" })

-- Terminal
vim.keymap.set("n", "<leader>tt", ":tabnew<CR>:terminal<CR>", { desc = "Create new tab with terminal" })
vim.keymap.set('t', '<Esc><Esc>', '<C-\\><C-n>', { desc = 'Exit terminal mode' })

-- Explore
vim.keymap.set("n", "<leader>e", ":Ex<CR>", { desc = "Opens File Explorer" })
vim.keymap.set("n", "<leader>r", "<C-6>", { desc = "Close File Explorer" })

-- Navigate
vim.keymap.set("n", "<C-u>", "<C-u>zz", { desc = "Go half page up and center screen" })
vim.keymap.set("n", "<C-d>", "<C-d>zz", { desc = "Go half page down and center screen" })
vim.keymap.set("n", "<leader>q", ":q<CR>", { desc = "[Q]uit" })

--Diagnostics
vim.keymap.set('n', '<leader>cd', vim.diagnostic.setloclist, { desc = 'Open [C]ode [D]iagnostics' })

-- Clear highlights when pressing <Esc> in normal mode
vim.keymap.set('n', '<Esc>', '<cmd>nohlsearch<CR>')
