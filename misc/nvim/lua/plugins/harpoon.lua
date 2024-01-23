return {

  {
    "ThePrimeagen/harpoon",
    config = function()
      local hrpn = require("harpoon")
      local ui = require("harpoon.ui")
      local list = hrpn:list()
      local km = vim.keymap

      hrpn.setup()

      km.set("n", "<leader>a", function() list:append() end)
      km.set("n", "<C-e>", function() ui:toggle_quick_menu(list) end)

      km.set("n", "<A-z>", function() hrpn:list():select(1) end)
      km.set("n", "<A-x>", function() hrpn:list():select(2) end)
      km.set("n", "<A-c>", function() hrpn:list():select(3) end)
      km.set("n", "<A-v>", function() hrpn:list():select(4) end)

    end,
    branch = "harpoon2",
    dependencies = { { "nvim-lua/plenary.nvim" } },
  },
}
