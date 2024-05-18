from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')
notifications_instance = webman_instance.Notifications(webman_instance)

# Display a popup message
notifications_instance.popup('Hello World')

# Show system information
notifications_instance.show_version()

# Display a persistent popup message
notifications_instance.persistent_popup('This is a persistent message')

# Display a bottom popup message
notifications_instance.bottom_popup('This is a bottom popup message')

# Display a message using VshFpsCounter plugin
notifications_instance.vsh_fps_counter('Displaying message using VshFpsCounter')
