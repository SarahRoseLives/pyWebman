from pyWebman.pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')
misc_instance = webman_instance.Misc(webman_instance)

# Show admin mode status
misc_instance.admin_mode_status()

# Switch to user mode
misc_instance.switch_to_user_mode()

# Switch to admin mode with password
misc_instance.switch_to_admin_mode(password='your_password')

# Wait for 10 seconds
misc_instance.wait(seconds=10)

# Wait for a specific path or file
misc_instance.wait_for_path_or_file(path='/path/to/file')

# Wait for XMB
misc_instance.wait_for_xmb()

# Show CPU/RSX temperature
misc_instance.show_cpu_rsx_temperature()

# Show minimum firmware version
misc_instance.show_minimum_firmware_version()

# Rebuild database
misc_instance.rebuild_database()

# Enter recovery mode
misc_instance.enter_recovery_mode()
