# Importing the Webman and Mount classes
from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')


# Creating a Mount instance
mount = webman_instance.Mount(webman_instance)

# Mounting a game from a path with options
mount.mount_path_or_iso('/dev_hdd0/game/my_game', options='auto')

# Mounting a game from a URI
mount.mount_path_or_iso('http://example.com/game.iso')

# Mounting a PS2 game folder
mount.mount_ps2_game_folder('/dev_hdd0/PS2ISO/my_ps2_game')

# Fixing a game
mount.fix_game('/dev_hdd0/game/my_game')

# Playing a game by its identifier
mount.play_game('my_game')

# Ejecting the physical disc
mount.eject_physical_disc()

# Inserting the physical disc
mount.insert_physical_disc()

# Ejecting the emulated disc image
mount.eject_emulated_disc_image()

# Inserting the emulated disc image
mount.insert_emulated_disc_image()

# Exiting game to XMB
mount.exit_game_to_xmb()

# Reloading PS3 game
mount.reload_ps3_game()

# Toggling external game data
mount.toggle_external_game_data(enable=True)

# Remapping a path to a destination
mount.remap_path_to_destination('/dev_hdd0/game/my_game', '/dev_usb000/my_game')

# Unmapping a remapped path
mount.unmap_remapped_path('/dev_hdd0/game/my_game')

# Setting a path to app_home
mount.set_app_home_path('/dev_hdd0/game/my_game')

# Unmounting a game
mount.unmount_game()

# Unmounting a PS2 game
mount.unmount_ps2_game()
