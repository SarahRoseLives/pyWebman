import requests
import time

class WebMan:
    def __init__(self, ip):
        self.ip = ip

    def command(self, route, delay=1):
        requests.get(f'http://{self.ip}/{route}')
        time.sleep(delay)

    class General:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def browse_path(self, full_path):
            self.webman.command(f'/{full_path}')

        def browse_path_with_name_filter(self, full_path, name):
            self.webman.command(f'/{full_path}?{name}')

        def find_files_containing_text(self, full_path, text):
            self.webman.command(f'/{full_path}/*{text}')

        def open_settings(self):
            self.webman.command('/setup.ps3')

        def reset_settings(self):
            self.webman.command('/setup.ps3?')

        def list_games_in_html_grid(self, text=None, path=None):
            if text:
                self.webman.command(f'/index.ps3?{text}')
            elif path:
                self.webman.command(f'/index.ps3?{path}')
            else:
                self.webman.command('/index.ps3')

        def list_games_in_slider(self, text=None, path=None, user_profile=None):
            route = '/games.ps3'
            if text:
                route += f'?{text}'
            elif path:
                route += f'?{path}'
            elif user_profile is not None:
                route += f'?usr={user_profile}'
            self.webman.command(route)

        def show_sman_gui(self):
            self.webman.command('/sman.ps3')

        def rescan_games_and_refresh_xml(self, cover_mode=None):
            route = '/refresh.ps3'
            if cover_mode:
                route += f'?cover={cover_mode}'
            self.webman.command(route)

        def reload_xmb(self):
            self.webman.command('/reloadxmb.ps3')

        def refresh_ntfs_volumes(self, keep_cached_files=False):
            route = '/refresh.ps3?ntfs'
            if keep_cached_files:
                route += '(0)'
            self.webman.command(route)

        def restart_ps3(self, mode=None):
            route = '/restart.ps3'
            if mode:
                route += f'?{mode}'
            self.webman.command(route)

        def hard_reboot_ps3(self):
            self.webman.command('/reboot.ps3?hard')

        def soft_reboot_ps3(self):
            self.webman.command('/reboot.ps3?soft')

        def shutdown_ps3(self):
            self.webman.command('/shutdown.ps3')

        def stop_webman_mod(self, fan_control_mode=None):
            route = '/quit.ps3'
            if fan_control_mode is not None:
                route += f'?{fan_control_mode}'
            self.webman.command(route)

    class Temperature:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def show_system_info(self):
            self.webman.command('/cpursx.ps3')

        def set_fan_speed(self, speed):
            self.webman.command(f'/cpursx.ps3?fan={speed}')

        def set_target_temperature(self, temperature):
            self.webman.command(f'/cpursx.ps3?max={temperature}')

        def set_fan_controller_to_manual_mode(self):
            self.webman.command('/cpursx.ps3?man')

        def set_fan_controller_to_dynamic_mode(self):
            self.webman.command('/cpursx.ps3?dyn')

        def set_fan_controller_to_auto_mode(self):
            self.webman.command('/cpursx.ps3?auto')

        def set_fan_controller_to_syscon_mode(self):
            self.webman.command('/cpursx.ps3?sys')

        def switch_fan_controller_mode(self):
            self.webman.command('/cpursx.ps3?mode')

        def increase_fan_speed_or_temperature(self):
            self.webman.command('/cpursx.ps3?up')

        def decrease_fan_speed_or_temperature(self):
            self.webman.command('/cpursx.ps3?dn')

        def open_temperature_monitor_celsius_gui(self):
            self.webman.command('/tempc.html')

        def open_temperature_monitor_fahrenheit_gui(self):
            self.webman.command('/tempf.html')

    class Mount:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def mount_path_or_iso(self, path_or_iso, options=None):
            route = f'/mount.ps3/{path_or_iso}'
            if options:
                route += '?' + options
            self.webman.command(route)

        def unmount_game(self, device=None):
            route = '/mount.ps3/unmount'
            if device:
                route += f'/{device}'
            self.webman.command(route)

        def mount_ps2_game_folder(self, folder_path):
            self.webman.command(f'/mount.ps2/{folder_path}')

        def unmount_ps2_game(self):
            self.webman.command('/mount.ps2/unmount')

        def fix_game(self, path_or_iso):
            self.webman.command(f'/fixgame.ps3/{path_or_iso}')

        def play_game(self, game_identifier):
            self.webman.command(f'/play.ps3/{game_identifier}')

        def eject_physical_disc(self):
            self.webman.command('/eject.ps3')

        def insert_physical_disc(self):
            self.webman.command('/insert.ps3')

        def eject_emulated_disc_image(self, device=None):
            route = '/xmb.ps3$eject'
            if device:
                route += f'/{device}'
            self.webman.command(route)

        def insert_emulated_disc_image(self, device=None):
            route = '/xmb.ps3$insert'
            if device:
                route += f'/{device}'
            self.webman.command(route)

        def exit_game_to_xmb(self):
            self.webman.command('/xmb.ps3$exit')

        def reload_ps3_game(self):
            self.webman.command('/xmb.ps3$reloadgame')

        def toggle_external_game_data(self, enable=True):
            route = '/extgd.ps3'
            if enable:
                route += '?enable'
            else:
                route += '?disable'
            self.webman.command(route)

        def remap_path_to_destination(self, source_path, destination_path):
            self.webman.command(f'/remap.ps3/{source_path}&to={destination_path}')

        def unmap_remapped_path(self, source_path):
            self.webman.command(f'/unmap.ps3/{source_path}')

    class Stealth:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def change_idps_psid(self):
            self.webman.command('/setidps.ps3mapi')

        def dump_idps_act(self, path=None):
            route = '/idps.ps3'
            if path:
                route += f'/{path}'
            self.webman.command(route)

        def dump_psid_act(self, path=None):
            route = '/psid.ps3'
            if path:
                route += f'/{path}'
            self.webman.command(route)

        def dump_console_id(self):
            self.webman.command('/consoleid.ps3')

        def show_idps_psid(self):
            self.webman.command('/xmb.ps3$show_idps')

        def manage_syscall_modes(self, syscall_number=None, hex_value=None, decimal_value=None, string_value=None):
            route = '/syscall.ps3mapi'
            if syscall_number:
                route += f'?{syscall_number}'
                if hex_value:
                    route += f'|0x{hex_value}'
                elif decimal_value:
                    route += f'|{decimal_value}'
                elif string_value:
                    route += f'|{string_value}'
            self.webman.command(route)

        def disable_syscalls(self, ccapi=False):
            route = '/xmb.ps3$disable_syscalls'
            if ccapi:
                route += '?ccapi'
            self.webman.command(route)

        def enable_syscalls(self):
            self.webman.command('/syscall.ps3mapi?sce=1')

        def toggle_network_access_registry(self):
            self.webman.command('/netstatus.ps3')

        def block_online_servers(self):
            self.webman.command('/xmb.ps3$block_servers')

        def restore_blocked_servers(self):
            self.webman.command('/xmb.ps3$restore_servers')

    class Files:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def get_folder_size_and_count(self, folder_path):
            route = f'/stat.ps3/{folder_path}'
            self.webman.command(route)

        def compare_files_and_symlink_common(self, game_name, title_id):
            route = f'/stat.ps3/dev_hdd0/GAMES/{game_name}&id={title_id}'
            self.webman.command(route)

        def copy_files(self, source_path, destination=None, restart=False):
            route = f'/copy.ps3/{source_path}'
            if destination:
                route += f'&to={destination}'
                if restart:
                    route += '?restart.ps3'
            self.webman.command(route)

        def abort_copy(self):
            self.webman.command('/copy.ps3$abort')

        def store_for_copy_operation(self, source_path):
            self.webman.command(f'/cpy.ps3/{source_path}')

        def store_for_move_operation(self, source_path):
            self.webman.command(f'/cut.ps3/{source_path}')

        def paste_to_destination(self, destination_path):
            self.webman.command(f'/paste.ps3/{destination_path}')

        def delete_files(self, path, recursive=False, restart=False):
            route = f'/delete.ps3/{path}'
            if recursive:
                route += '?restart.ps3' if restart else ''
            self.webman.command(route)

        def delete_history_files(self):
            self.webman.command('/delete.ps3?history')

        def delete_webman_config(self):
            self.webman.command('/delete.ps3?wmconfig')

        def delete_webman_tmp(self):
            self.webman.command('/delete.ps3?wmtmp')

        def reset_webman(self):
            self.webman.command('/delete.ps3?wmreset')

        def uninstall_webman_mod(self):
            self.webman.command('/delete.ps3?uninstall')

        def truncate_file_content(self, file_path):
            self.webman.command(f'/trunc.ps3/{file_path}')

        def truncate_directory_content(self, directory_path):
            self.webman.command(f'/trunc.ps3/{directory_path}')

        def truncate_file_by_pattern(self, path, wildcard_pattern):
            route = f'/trunc.ps3/{path}/{wildcard_pattern}'
            self.webman.command(route)

        def rename_or_move_file(self, source_path, destination, restart=False):
            route = f'/rename.ps3/{source_path}|{destination}'
            if restart:
                route += '?restart.ps3'
            self.webman.command(route)

        def move_files(self, path1, path2, restart=False):
            route = f'/move.ps3/{path1}|{path2}'
            if restart:
                route += '?restart.ps3'
            self.webman.command(route)

        def swap_files(self, file1, file2, restart=False):
            route = f'/swap.ps3/{file1}|{file2}'
            if restart:
                route += '?restart.ps3'
            self.webman.command(route)

        def edit_text_file(self, file_path, text=None):
            if text:
                route = f'/edit.ps3?f={file_path}&t={text}'
            else:
                route = f'/edit.ps3/{file_path}'
            self.webman.command(route)

        def start_artemis(self, ncl_path=None, code=None, attach=False, detach=False):
            route = '/artemis.ps3'
            if ncl_path:
                route += f'/{ncl_path}'
                if code:
                    route += f'?f={ncl_path}&t={code}'
                elif attach:
                    route += '?attach'
                elif detach:
                    route += '?detach'
            self.webman.command(route)

        def view_file_content(self, file_path, field=None, value=None, hex_value=None):
            route = f'/view.ps3/{file_path}'
            if field and value:
                route += f'?{field}={value}'
            elif field and hex_value:
                route += f'?{field}&={hex_value}'
            self.webman.command(route)

        def hex_view_file(self, file_path, offset=None, data=None, find=None):
            route = f'/hexview.ps3/{file_path}'
            if offset:
                route += f'&offset={offset}'
                if data:
                    route += f'&data={data}'
                elif find:
                    route += f'&find={find}'
            self.webman.command(route)

        def write_text_to_file(self, file_path, text=None, line=None, hex_value=None):
            route = f'/write.ps3/{file_path}'
            if text:
                route += f'&t={text}'
            elif line:
                route += f'&t={text}&line={line}'
            elif hex_value:
                route += f'&t={hex_value}&pos={offset}'
            self.webman.command(route)

        def create_zip_file(self, folder_path, destination=None):
            route = f'/dozip.ps3/{folder_path}'
            if destination:
                route += f'&to={destination}'
            self.webman.command(route)

        def decompress_archive(self, archive_file, destination=None):
            route = f'/unzip.ps3/{archive_file}'
            if destination:
                route += f'&to={destination}'
            self.webman.command(route)

        def create_folder(self, folder_path=None):
            route = '/mkdir.ps3'
            if folder_path:
                route += f'/{folder_path}'
            self.webman.command(route)

        def delete_folder(self, folder_path=None):
            route = '/rmdir.ps3'
            if folder_path:
                route += f'/{folder_path}'
            self.webman.command(route)

        def toggle_dev_blind(self, force=None):
            route = '/dev_blind'
            if force is not None:
                route += f'?{force}'
            self.webman.command(route)

        def auto_mount_dev_hdd1(self):
            self.webman.command('/dev_hdd1')

        def show_md5_of_file(self, file_path):
            self.webman.command(f'/md5.ps3/{file_path}')

        def toggle_unlock_hdd_space(self, percentage=None, optimization=None):
            route = '/unlockhdd.ps3'
            if percentage:
                route += f'?{percentage}&opt={optimization}'
            self.webman.command(route)

    class InGame:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def toggle_video_recording(self):
            self.webman.command('/videorec.ps3')

        def set_video_audio_formats(self, video_format, audio_format):
            route = f'/videorec.ps3?video={video_format}&audio={audio_format}'
            self.webman.command(route)

        def record_video_to_path(self, file_path):
            route = f'/videorec.ps3/{file_path}'
            self.webman.command(route)

        def toggle_klicensee_log_auto(self):
            self.webman.command('/klic.ps3?auto')

        def toggle_klicensee_log(self):
            self.webman.command('/klic.ps3?log')

        def toggle_klicensee_log_off(self):
            self.webman.command('/klic.ps3?off')

        def hook_savedata_plugin(self):
            self.webman.command('/secureid.ps3')

        def toggle_ingame_bgm(self):
            self.webman.command('/sysbgm.ps3')

        def enable_ingame_bgm(self):
            self.webman.command('/sysbgm.ps3?1')

        def disable_ingame_bgm(self):
            self.webman.command('/sysbgm.ps3?0')

        def show_ingame_bgm_status(self):
            self.webman.command('/sysbgm.ps3?status')

        def enable_ingame_screenshot(self):
            self.webman.command('/xmb.ps3$ingame_screenshot')

        def play_music_on_xmb(self):
            self.webman.command('/xmb.ps3$music')

        def play_video_on_xmb(self):
            self.webman.command('/xmb.ps3$video')

        def go_to_webman_games_entry(self):
            self.webman.command('/xmb.ps3$home')

        def go_to_webman_games_and_reload(self):
            self.webman.command('/xmb.ps3$home*')

    class XMB:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def install_package(self, pkg_path, delete_after_install=False, keep_package=False):
            route = '/install.ps3'
            if delete_after_install:
                route += '?d'
            if keep_package:
                route += '?k'
            self.webman.command(route)

        def navigate_or_install_package(self, pkg_path):
            route = f'/install.ps3?{pkg_path}'
            self.webman.command(route)

        def download_file_to_packages(self, url):
            route = f'/xmb.ps3/download.ps3?url={url}'
            self.webman.command(route)

        def download_file_to_path(self, url, destination_path):
            route = f'/xmb.ps3/download.ps3?to={destination_path}&url={url}'
            self.webman.command(route)

        def open_url_on_browser(self, url):
            route = f'/browser.ps3?{url}'
            self.webman.command(route)

        def open_local_path_on_browser(self, path):
            route = f'/browser.ps3/{path}'
            self.webman.command(route)

        def open_web_command_on_browser(self, cmd):
            route = f'/browser.ps3/{cmd}'
            self.webman.command(route)

        def execute_script_file(self, script_file):
            route = f'/play.ps3{script_file}'
            self.webman.command(route)

        def go_to_xmb_item(self, col_name, xmb_item_id):
            route = f'/play.ps3?col={col_name}&seg={xmb_item_id}'
            self.webman.command(route)

        def execute_explore_plugin_command(self, cmd):
            route = f'/xmb.ps3${cmd}'
            self.webman.command(route)

        def execute_xmb_plugin_command(self, cmd):
            route = f'/xmb.ps3*{cmd}'
            self.webman.command(route)

        def toggle_vsh_menu(self):
            self.webman.command('/xmb.ps3$vsh_menu')

        def toggle_slaunch_menu(self):
            self.webman.command('/xmb.ps3$slaunch')

        def capture_xmb_screen(self, path_filename):
            route = f'/xmb.ps3$screenshot/{path_filename}'
            self.webman.command(route)

        def show_captured_xmb_screen(self, fast=False):
            route = '/xmb.ps3$screenshot?show'
            if fast:
                route += '?fast'
            self.webman.command(route)

    class Debug:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def ps3mapi_home(self):
            self.webman.command('/home.ps3mapi')

        def manage_leds(self):
            self.webman.command('/led.ps3mapi')

        def ring_buzzer(self):
            self.webman.command('/buzzer.ps3mapi')

        def ring_buzzer_custom(self, number):
            self.webman.command(f'/beep.ps3?{number}')

        def manage_mappings(self):
            self.webman.command('/mappath.ps3mapi')

        def set_process_memory_value(self, proc_id, address, value):
            self.webman.command(f'/setmem.ps3mapi?proc={proc_id}&addr={address}&val={value}')

        def get_process_memory_value(self, proc_id, address):
            return self.webman.command(f'/getmem.ps3mapi?proc={proc_id}&addr={address}')

        def patch_process_memory(self, proc_id, address, hex_code):
            self.webman.command(f'/setmem.ps3mapi?proc={proc_id}&addr={address}&val={hex_code}')

        def list_load_unload_vsh_plugins(self):
            self.webman.command('/vshplugin.ps3mapi')

        def save_loaded_vsh_plugins(self, slot):
            self.webman.command(f'/vshplugin.ps3mapi?s={slot}')

        def list_load_unload_kernel_plugins(self):
            self.webman.command('/kernelplugin.ps3mapi')

        def save_loaded_kernel_plugins(self, slot):
            self.webman.command(f'/kernelplugin.ps3mapi?s={slot}')

        def list_load_unload_in_game_plugins(self):
            self.webman.command('/gameplugin.ps3mapi')

        def load_prx(self, path, slot=6):
            self.webman.command(f'/loadprx.ps3?slot={slot}&prx={path}')

        def unload_prx_by_slot(self, slot):
            self.webman.command(f'/unloadprx.ps3?slot={slot}')

        def unload_prx_by_name(self, name):
            self.webman.command(f'/unloadprx.ps3?prx={name}')

        def unload_prx_by_path(self, path):
            self.webman.command(f'/unloadprx.ps3/{path}')

        def unload_prx_by_id(self, plugin_id):
            self.webman.command(f'/unloadprx.ps3?id={plugin_id}')

        def pause_rsx_processor(self):
            self.webman.command('/xmb.ps3$rsx_pause')

        def continue_rsx_processor(self):
            self.webman.command('/xmb.ps3$rsx_continue')

        def show_value_xregistry_by_id(self, id):
            self.webman.command(f'/xmb.ps3$xregistry({id}) show')

        def update_value_xregistry_by_id(self, id, value):
            self.webman.command(f'/xmb.ps3$xregistry({id})={value}')

        def show_value_xregistry_by_key_path(self, key_path):
            self.webman.command(f'/xmb.ps3$xregistry({key_path}) show')

        def update_value_xregistry_by_key_path(self, key_path, value):
            self.webman.command(f'/xmb.ps3$xregistry({key_path})={value}')

        def dump_memory(self, memory_type='full', start_address=None, size=None):
            route = f'/dump.ps3?{memory_type}'
            if start_address and size:
                route += f'&start={start_address}&size={size}'
            self.webman.command(route)

        def toggle_noBD(self, enable=None):
            route = '/nobd.ps3'
            if enable is not None:
                if enable:
                    route += '?enable'
                else:
                    route += '?disable'
            self.webman.command(route)

    class Notifications:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def popup(self, message, icon=None, sound=None, rco=None, raw=False):
            route = 'popup.ps3'
            if message:
                if raw:
                    route += f'={message}'
                else:
                    if icon:
                        route += f'?msg={message}&icon={icon}'
                    elif sound:
                        route += f'?msg={message}&snd={sound}'
                    elif rco:
                        route += f'?msg={message}&icon={icon}&rco={rco}'
                    else:
                        route += f'/{message}'
            self.webman.command(route)

        def persistent_popup(self, message):
            self.webman.command(f'popup.ps3${message}')

        def bottom_popup(self, message):
            self.webman.command(f'popup.ps3*{message}')

        def show_version(self):
            self.webman.command('popup.ps3?')

        def vsh_fps_counter(self, message):
            self.webman.command(f'popup.ps3@{message}')

    class Gamepad:
        # Define buttons as class attributes
        buttons = {
            'up': 'up',
            'down': 'down',
            'left': 'left',
            'right': 'right',
            'cross': 'cross',
            'circle': 'circle',
            'square': 'square',
            'triangle': 'triangle',
            'r1': 'r1',
            'r2': 'r2',
            'l1': 'l1',
            'l2': 'l2',
            'psbtn': 'psbtn',
            'select': 'select',
            'start': 'start',
            'hold': 'hold',
            'release': 'release',
            'analogL_up': 'analogL_up',
            'analogL_down': 'analogL_down',
            'analogL_left': 'analogL_left',
            'analogL_right': 'analogL_right',
            'analogR_up': 'analogR_up',
            'analogR_down': 'analogR_down',
            'analogR_left': 'analogR_left',
            'analogR_right': 'analogR_right'
        }

        def __init__(self, webman_instance):
            self.webman = webman_instance

        # Define methods to interact with the buttons
        def pad(self, buttons, delay=1):
            self.webman.command(f'pad.ps3?{buttons}', delay)

        def off(self, delay=1):
            self.webman.command('pad.ps3?off', delay)

        def hold(self, buttons, delay=1):
            self.webman.command(f'pad.ps3?hold{buttons}', delay)

        def release(self, delay=1):
            self.webman.command('pad.ps3?release', delay)

        def accept(self, delay=1):
            self.webman.command('pad.ps3?accept', delay)

        def cancel(self, delay=1):
            self.webman.command('pad.ps3?cancel', delay)

        def set_enter(self, button, action, delay=1):
            self.webman.command(f'pad.ps3?{button}={action}', delay)

        def combo(self, buttons, delay=1):
            self.webman.command(f'combo.ps3?{buttons}', delay)

        # Instantiate the webman class with the IP address
        # my_webman = webman(ip='192.168.1.100')

        # Instantiate the Gamepad class with the webman instance
        # gamepad_instance = webman.Gamepad(my_webman)

        # Sending the triangle button
        # gamepad_instance.pad('triangle')

    class Togglers:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def toggle_rebug_mode(self):
            self.webman.command('xmb.ps3$toggle_rebug_mode')

        def toggle_normal_mode(self):
            self.webman.command('xmb.ps3$toggle_normal_mode')

        def toggle_debug_menu(self):
            self.webman.command('xmb.ps3$toggle_debug_menu')

        def toggle_cobra(self):
            self.webman.command('xmb.ps3$toggle_cobra')

        def toggle_ps2emu(self):
            self.webman.command('xmb.ps3$toggle_ps2emu')

        def set_ps2_netemu(self):
            self.webman.command('xmb.ps3$ps2_netemu')

        def restore_default_ps2emu(self):
            self.webman.command('xmb.ps3$ps2emu')

        def enable_classic_ps2_mode(self):
            self.webman.command('xmb.ps3$enable_classic_ps2_mode')

        def disable_classic_ps2_mode(self):
            self.webman.command('xmb.ps3$disable_classic_ps2_mode')

    class Misc:
        def __init__(self, webman_instance):
            self.webman = webman_instance

        def admin_mode_status(self):
            self.webman.command('admin.ps3?')

        def switch_to_user_mode(self):
            self.webman.command('admin.ps3?disabled')

        def switch_to_admin_mode(self, password):
            self.webman.command(f'admin.ps3?enabled&pwd={password}')

        def wait(self, seconds):
            self.webman.command(f'wait.ps3?{seconds}')

        def wait_for_path_or_file(self, path):
            self.webman.command(f'wait.ps3/{path}')

        def wait_for_xmb(self):
            self.webman.command('wait.ps3?xmb')

        def show_cpu_rsx_temperature(self):
            self.webman.command('cpursx_ps3')

        def show_minimum_firmware_version(self):
            self.webman.command('minver.ps3')

        def rebuild_database(self):
            self.webman.command('rebuild.ps3')

        def enter_recovery_mode(self):
            self.webman.command('recovery.ps3')

