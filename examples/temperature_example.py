from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')

# Create a Temperature instance
temperature_manager = webman_instance.Temperature(webman_instance)

# Example of each function:

# Show system info
temperature_manager.show_system_info()

# Set fan speed to 50%
temperature_manager.set_fan_speed(50)

# Set target temperature to 70°C
temperature_manager.set_target_temperature(70)

# Set fan controller to manual mode
temperature_manager.set_fan_controller_to_manual_mode()

# Set fan controller to dynamic mode
temperature_manager.set_fan_controller_to_dynamic_mode()

# Set fan controller to auto mode
temperature_manager.set_fan_controller_to_auto_mode()

# Set fan controller to SYSCON mode
temperature_manager.set_fan_controller_to_syscon_mode()

# Switch fan controller mode between manual and dynamic
temperature_manager.switch_fan_controller_mode()

# Increase fan speed or target temperature
temperature_manager.increase_fan_speed_or_temperature()

# Decrease fan speed or target temperature
temperature_manager.decrease_fan_speed_or_temperature()

# Open temperature monitor GUI in Celsius
temperature_manager.open_temperature_monitor_celsius_gui()

# Open temperature monitor GUI in Fahrenheit
temperature_manager.open_temperature_monitor_fahrenheit_gui()
