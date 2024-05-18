# WebMan Python Library

This is a Python library for interacting with a webman-mod server. The library provides a set of classes and methods to perform various tasks such as browsing files, managing system settings, controlling the PlayStation 3 console, and more.

## Installation

You can install this library using pip:

```bash
pip install pyWebman
```

## Usage

Below is a guide on how to use the different classes and methods provided by this library.

### Initialization

First, you need to create an instance of the `WebMan` class with the IP address of your webman-mod server:

```python
from pyWebman import WebMan

# Replace 'your_ps3_ip' with the actual IP address of your PS3
webman_instance = WebMan(('your_ps3_ip')
```

### General Commands

The `General` class provides methods to browse files, manage settings, and list games.

```python
general = webman_instance.General(webman_instance)

# Browse a specific path
general.browse_path('path/to/browse')

# Open settings
general.open_settings()

# List games in HTML grid
general.list_games_in_html_grid()
```

### Temperature Management

The `Temperature` class allows you to manage the fan speed and monitor system temperatures.

```python
temperature = webman_instance.Temperature(webman_instance)

# Show system info
temperature.show_system_info()

# Set fan speed
temperature.set_fan_speed(50)
```

### Mounting and Unmounting

The `Mount` class provides methods to mount and unmount games and ISO files.

```python
mount = webman_instance.Mount(webman_instance)

# Mount a game
mount.mount_path_or_iso('path/to/game.iso')

# Unmount the current game
mount.unmount_game()
```

### Stealth Mode

The `Stealth` class offers methods to manage system identifiers and syscall modes.

```python
stealth = webman_instance.Stealth(webman_instance)

# Change IDPS and PSID
stealth.change_idps_psid()

# Disable syscalls
stealth.disable_syscalls()
```

### File Management

The `Files` class provides various methods for file operations such as copying, moving, deleting, and editing files.

```python
files = webman_instance.Files(webman_instance)

# Copy files
files.copy_files('source/path', 'destination/path')

# Delete files
files.delete_files('path/to/delete')
```

### In-Game Features

The `InGame` class allows you to manage in-game settings and features.

```python
ingame = webman_instance.InGame(webman_instance)

# Toggle video recording
ingame.toggle_video_recording()

# Enable in-game background music
ingame.enable_ingame_bgm()
```

### XMB Management

The `XMB` class provides methods to navigate the XMB, install packages, and download files.

```python
xmb = webman_instance.XMB(webman_instance)

# Install a package
xmb.install_package('path/to/package.pkg')

# Download a file to the packages directory
xmb.download_file_to_packages('http://example.com/file.pkg')
```

### Debugging Tools

The `Debug` class offers tools for debugging and managing system processes.

```python
debug = webman_instance.Debug(webman_instance)

# Ring the buzzer
debug.ring_buzzer()

# Manage LED settings
debug.manage_leds()
```

### Notifications

The `Notifications` class allows you to send popup messages and notifications.

```python
notifications = webman_instance.Notifications(webman_instance)

# Send a popup message
notifications.popup('This is a test message')
```

### Gamepad Control

The `Gamepad` class provides methods to simulate gamepad inputs.

```python
gamepad = webman_instance.Gamepad(webman_instance)

# Simulate a button press
gamepad.pad('cross')

# Hold a button
gamepad.hold('circle')

# Release a button
gamepad.release()
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

This library is inspired by the webman-mod project and provides a convenient way to interact with it using Python.

---

By following this guide, you should be able to effectively use the `WebMan` Python library to interact with your webman-mod server and perform a wide range of tasks programmatically.