# Assume you have already created a Webman instance
webman = Webman()

# Create a General instance
general_manager = General(webman)

# Browse a full path
general_manager.browse_path('dev_hdd0')

# Browse a path with name filter
general_manager.browse_path_with_name_filter('dev_hdd0', 'name')

# Find files containing text
general_manager.find_files_containing_text('dev_hdd0', 'text')

# Open settings
general_manager.open_settings()

# Reset settings
general_manager.reset_settings()

# List games in HTML grid
general_manager.list_games_in_html_grid()

# List games in slider
general_manager.list_games_in_slider()

# Show sMAN GUI
general_manager.show_sman_gui()

# Rescan games and refresh XML
general_manager.rescan_games_and_refresh_xml()

# Reload XMB
general_manager.reload_xmb()

# Refresh NTFS volumes
general_manager.refresh_ntfs_volumes()

# Restart PS3
general_manager.restart_ps3()

# Hard reboot PS3
general_manager.hard_reboot_ps3()

# Soft reboot PS3
general_manager.soft_reboot_ps3()

# Shutdown PS3
general_manager.shutdown_ps3()

# Stop webMAN MOD
general_manager.stop_webman_mod()