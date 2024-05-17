webman_instance = WebMan(ip='192.168.1.14')
stealth_instance = webman_instance.Stealth(webman_instance)

# Change IDPS/PSID
stealth_instance.change_idps_psid()

# Dump IDPS & ACT.DAT
stealth_instance.dump_idps_act()

# Dump IDPS to specified path
stealth_instance.dump_idps_act(path='/dev_hdd0/idps.bin')

# Dump PSID & ACT.DAT
stealth_instance.dump_psid_act()

# Dump PSID to specified path
stealth_instance.dump_psid_act(path='/dev_hdd0/psid.bin')

# Dump console ID
stealth_instance.dump_console_id()

# Show IDPS/PSID
stealth_instance.show_idps_psid()

# Manage syscall modes
stealth_instance.manage_syscall_modes(syscall_number='392', hex_value='1004')

# Disable syscalls
stealth_instance.disable_syscalls(ccapi=True)

# Enable syscalls
stealth_instance.enable_syscalls()

# Toggle network access in registry
stealth_instance.toggle_network_access_registry()

# Block online servers
stealth_instance.block_online_servers()

# Restore blocked servers
stealth_instance.restore_blocked_servers()
