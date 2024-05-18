from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')
ingame_instance = webman_instance.InGame(webman_instance)

# Toggle video recording
ingame_instance.toggle_video_recording()

# Set video and audio formats
ingame_instance.set_video_audio_formats(video_format='mp4', audio_format='aac')

# Record video to a specific path
ingame_instance.record_video_to_path(file_path='/dev_hdd0/videos/my_video.mp4')

# Toggle klicensee log auto
ingame_instance.toggle_klicensee_log_auto()

# Toggle ingame background music
ingame_instance.toggle_ingame_bgm()

# Enable ingame background music
ingame_instance.enable_ingame_bgm()

# Disable ingame background music
ingame_instance.disable_ingame_bgm()

# Show ingame background music status
ingame_instance.show_ingame_bgm_status()

# Enable ingame screenshot
ingame_instance.enable_ingame_screenshot()

# Play music on XMB
ingame_instance.play_music_on_xmb()

# Play video on XMB
ingame_instance.play_video_on_xmb()

# Go to webMAN Games entry on XMB
ingame_instance.go_to_webman_games_entry()

# Go to webMAN Games + reload category game
ingame_instance.go_to_webman_games_and_reload()
