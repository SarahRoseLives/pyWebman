# Import the necessary class from pyWebman
from pyWebman import WebMan

# Create an instance of WebMan with the given IP address
webman_instance = WebMan(ip='ps3_ip')

# Instantiate the Gamepad class using the webman_instance
gamepad = webman_instance.Gamepad(webman_instance)

# Example usage of the Gamepad class

# Simulate pressing multiple buttons with a delay
gamepad.pad('up,cross', delay=2)

# Turn off the gamepad
gamepad.off(delay=1)

# Hold down multiple buttons
gamepad.hold('left,triangle', delay=3)

# Release previously held buttons
gamepad.release('left,triangle', delay=1)

# Accept the current selection (e.g., pressing 'Enter')
gamepad.accept(delay=1)

# Cancel the current selection (e.g., pressing 'Back')
gamepad.cancel(delay=1)

# Set a button to perform a specific action
gamepad.set_enter('cross', 'action', delay=1)

# Perform a combo action with multiple buttons
gamepad.combo('square,circle', delay=2)
