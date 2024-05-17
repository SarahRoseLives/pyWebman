from pyWebman.pyWebman import WebMan


webman_instance = WebMan(ip='192.168.1.14')
debug_instance = webman_instance.Debug(webman_instance)

# PS3MAPI home
debug_instance.ps3mapi_home()

# Manage LEDs
debug_instance.manage_leds()

# Ring the PS3 buzzer
debug_instance.ring_buzzer()

# Ring the PS3 buzzer with custom number (0-9)
debug_instance.ring_buzzer_custom(number=5)

# Manage mappings
debug_instance.manage_mappings()

# Set value to process memory
debug_instance.set_process_memory_value(proc_id=1, address='0x12345678', value='0xABCD')

# Get value from process memory
memory_value = debug_instance.get_process_memory_value(proc_id=1, address='0x12345678')
print(memory_value)

# Patch process memory
debug_instance.patch_process_memory(proc_id=1, address='0x12345678', hex_code='0xFF')

# List, load, unload VSH plugins
debug_instance.list_load_unload_vsh_plugins()

# Save currently loaded VSH plugins
debug_instance.save_loaded_vsh_plugins(slot=0)

# List, load, unload kernel plugins
debug_instance.list_load_unload_kernel_plugins()

# Save currently loaded kernel plugins
debug_instance.save_loaded_kernel_plugins(slot=0)

# List, load, unload in-game plugins
debug_instance.list_load_unload_in_game_plugins()

# Load PRX
debug_instance.load_prx(path='/dev_flash/your_plugin.prx', slot=6)

# Unload PRX by slot number
debug_instance.unload_prx_by_slot(slot=6)

# Unload PRX by name
debug_instance.unload_prx_by_name(name='your_plugin.prx')

# Unload PRX by path
debug_instance.unload_prx_by_path(path='/dev_flash/your_plugin.prx')

# Unload PRX by ID
debug_instance.unload_prx_by_id(plugin_id=123)

# Pause RSX processor
debug_instance.pause_rsx_processor()

# Continue RSX processor
debug_instance.continue_rsx_processor()

# Show value from xregistry by ID
debug_instance.show_value_xregistry_by_id(id=123)

# Update value in xregistry by ID
debug_instance.update_value_xregistry_by_id(id=123, value='new_value')

# Show value from xregistry by key path
debug_instance.show_value_xregistry_by_key_path(key_path='/path/to/key')

# Update value in xregistry by key path
debug_instance.update_value_xregistry_by_key_path(key_path='/path/to/key', value='new_value')

# Dump memory
debug_instance.dump_memory(memory_type='lv1', start_address='0x12345678', size=16)

# Toggle noBD
debug_instance.toggle_noBD(enable=True)
