from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')
xmb_instance = webman_instance.XMB(webman_instance)

# Install a package and delete it after installation
xmb_instance.install_package(pkg_path='/dev_hdd0/packages/your_package.pkg', delete_after_install=True)

# Download a file from a URL and save it to /dev_hdd0/packages
xmb_instance.download_file_to_packages(url='http://example.com/your_file.pkg')

# Open a URL on the PS3 web browser
xmb_instance.open_url_on_browser(url='http://example.com')

# Execute a script file
xmb_instance.execute_script_file(script_file='/dev_hdd0/scripts/your_script.txt')

# Toggle VSH menu
xmb_instance.toggle_vsh_menu()

# Capture XMB screen and save it
xmb_instance.capture_xmb_screen(path_filename='/dev_hdd0/screenshots/xmb_screen.png')

# Show the captured XMB screen
xmb_instance.show_captured_xmb_screen()
