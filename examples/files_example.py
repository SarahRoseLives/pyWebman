from pyWebman import WebMan

webman_instance = WebMan(ip='192.168.1.14')
files_instance = webman_instance.Files(webman_instance)

# Get folder size and count
files_instance.get_folder_size_and_count(folder_path='/dev_hdd0/GAMES')

# Compare files and symlink common
files_instance.compare_files_and_symlink_common(game_name='MyGame', title_id='BLES12345')

# Copy files
files_instance.copy_files(source_path='/dev_hdd0/myfile.txt', destination='/dev_usb000')

# Abort copy
files_instance.abort_copy()

# Store for copy operation
files_instance.store_for_copy_operation(source_path='/dev_hdd0/myfolder')

# Store for move operation
files_instance.store_for_move_operation(source_path='/dev_hdd0/myfile.txt')

# Paste to destination
files_instance.paste_to_destination(destination_path='/dev_hdd0/backup')

# Delete files
files_instance.delete_files(path='/dev_hdd0/myfile.txt')

# Delete history files
files_instance.delete_history_files()

# Delete webMAN config
files_instance.delete_webman_config()

# Delete webMAN tmp
files_instance.delete_webman_tmp()

# Reset webMAN
files_instance.reset_webman()

# Uninstall webMAN MOD
files_instance.uninstall_webman_mod()

# Truncate file content
files_instance.truncate_file_content(file_path='/dev_hdd0/myfile.txt')

# Rename or move file
files_instance.rename_or_move_file(source_path='/dev_hdd0/oldfile.txt', destination='/dev_hdd0/newfile.txt')

# Move files
files_instance.move_files(path1='/dev_hdd0/file1.txt', path2='/dev_hdd0/folder1')

# Swap files
files_instance.swap_files(file1='/dev_hdd0/file1.txt', file2='/dev_hdd0/file2.txt')

# Edit text file
files_instance.edit_text_file(file_path='/dev_hdd0/myfile.txt', text='Hello, World!')

# Start Artemis
files_instance.start_artemis(ncl_path='/dev_hdd0/art/code.ncl', code='12345678', attach=True)

# View file content
files_instance.view_file_content(file_path='/dev_hdd0/myfile.txt')

# Hex view file
files_instance.hex_view_file(file_path='/dev_hdd0/myfile.txt', offset=0x100, data='ABCDEF')

# Write text to file
files_instance.write_text_to_file(file_path='/dev_hdd0/myfile.txt', text='Line 1\nLine 2')

# Create zip file
files_instance.create_zip_file(folder_path='/dev_hdd0/folder', destination='/dev_usb000')

# Decompress archive
files_instance.decompress_archive(archive_file='/dev_usb000/archive.zip', destination='/dev_hdd0')

# Create folder
files_instance.create_folder(folder_path='/dev_hdd0/new_folder')

# Delete folder
files_instance.delete_folder(folder_path='/dev_hdd0/old_folder')

# Toggle dev_blind
files_instance.toggle_dev_blind(force='1')

# Auto mount dev_hdd1
files_instance.auto_mount_dev_hdd1()

# Show MD5 of file
files_instance.show_md5_of_file(file_path='/dev_hdd0/myfile.txt')

# Toggle unlock HDD space
files_instance.toggle_unlock_hdd_space(percentage='5', optimization='1')
