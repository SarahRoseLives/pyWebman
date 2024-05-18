from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')
togglers_instance = webman_instance.Togglers(webman_instance)

# Toggle REBUG Mode Debug XMB
togglers_instance.toggle_rebug_mode()

# Toggle Normal Mode (CEX vsh.self)
togglers_instance.toggle_normal_mode()

# Toggle between DEX Debug Menu and CEX QA Menu
togglers_instance.toggle_debug_menu()

# Toggle COBRA mode
togglers_instance.toggle_cobra()

# Toggle PS2 Emulation mode
togglers_instance.toggle_ps2emu()

# Set PS2 Netemu as default PS2 emulator
togglers_instance.set_ps2_netemu()

# Restore default PS2 emulator
togglers_instance.restore_default_ps2emu()

# Enable PS2 Classic mode
togglers_instance.enable_classic_ps2_mode()

# Disable PS2 Classic mode
togglers_instance.disable_classic_ps2_mode()
