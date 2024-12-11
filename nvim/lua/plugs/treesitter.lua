return {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    main = "nvim-treesitter.configs",

    opts = {
        ensure_installed = {
            "c",
            "lua",
            "python",
            "go",
            "zig",
            "javascript",
            "java",
            "html",
            "css",
            "json",
            "toml",
            "sql",
            "regex",
            "dockerfile",
            "markdown",
            "markdown_inline",
        },

        auto_install = true,
        highlight = {
            enable = true,
            additional_vim_regex_highlighting = { "ruby" },
        },
        indent = { enable = true, disable = { "ruby" } },
    },
}
