return {
    { -- Hints keybinds
        "folke/which-key.nvim",
    },

    { -- Indent line
        "lukas-reineke/indent-blankline.nvim",
        main = "ibl",
        opts = {
            indent = {
                char = "▏",
            },
            scope = {
                show_start = true,
                show_end = false,
                show_exact_scope = true,
            },
        },
    },

    { -- Autoclose parentheses, brackets, quotes, etc.
        "windwp/nvim-autopairs",
        event = "InsertEnter",
        config = true,
        opts = {},
    },

    { -- Highlight todo, notes, etc in comments
        "folke/todo-comments.nvim",
        event = "VimEnter",
        dependencies = { "nvim-lua/plenary.nvim" },
        opts = { signs = false },
    },
}
