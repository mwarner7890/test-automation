import socket
import sys
import time
from timestamp_print import ts_print


def _toggle_usb_tethering(adb):
    adb.launch_activity_component('com.android.settings/.TetherSettings')
    key_event_tmp = ['KEYCODE_DPAD_UP',
                     'KEYCODE_DPAD_UP',
                     'KEYCODE_DPAD_UP',
                     'KEYCODE_DPAD_UP']

    if adb.model_name not in ['S30', 'S40', 'AP01', 'Explore']:
        key_event_tmp.append('KEYCODE_DPAD_DOWN')
    print(adb.model_name)
    key_event_tmp.append('KEYCODE_ENTER')
    adb.input_key_event_sequence(key_event_tmp)
    time.sleep(5)
    adb.clear_most_recent_app()


def _set_rat(adb, rat):
    if adb.device_is_qualcomm() and adb.model_name != 'S30' and adb.model_name != 'S40':
        mb_net_settings_activity_name = 'com.qualcomm.qti.networksetting/' \
                                        'com.qualcomm.qti.networksetting.MobileNetworkSettings'
    else:
        mb_net_settings_activity_name = 'com.android.phone/' \
                                        'com.android.phone.MobileNetworkSettings'

    adb.launch_activity_component(mb_net_settings_activity_name)
    adb.input_key_event_sequence(['KEYCODE_DPAD_DOWN',
                                 'KEYCODE_DPAD_DOWN', 'KEYCODE_ENTER',
                                  'KEYCODE_DPAD_UP', 'KEYCODE_DPAD_UP',
                                  'KEYCODE_DPAD_UP'])

    adb.repeat_input_key_event('KEYCODE_DPAD_DOWN',
                               _get_menu_entry_count_for_rat(rat))
    adb.input_key_event('KEYCODE_ENTER')

    adb.clear_most_recent_app()


def _get_menu_entry_count_for_rat(rat):
    if rat == '4g':
        return 0
    if rat == '3g':
        return 1
    if rat == '2g':
        return 2


def _toggle_wifi(adb):
    adb.launch_activity_action('android.settings.WIFI_SETTINGS')

    if adb.model_name == 'S30' or adb.model_name == 'S40':
        adb.input_tap(x=470, y=130)
    else:
        adb.input_key_event_sequence(['KEYCODE_DPAD_DOWN',
                                     'KEYCODE_ENTER'])
    adb.clear_most_recent_app()


def _time_download(adb, download_filename):
    _toggle_usb_tethering(adb)
    time.sleep(8)
    adb.lock_screen()
    while True:
        try:
            ts_print('Downloading {}/{} through device {}:'.
                     format(adb.ftp.download_dir, download_filename, adb.model_name))
            time_started = time.time()
            adb.ftp.login_and_download_file_from_ftp(download_filename)
            time_taken = round(time.time() - time_started)
            ts_print('Download complete; time taken: {} seconds'.format(time_taken))
            adb.unlock_screen_with_pin()
            _toggle_usb_tethering(adb)
            return time_taken
        except socket.gaierror:
            print('Error: Could not connect to FTP server. Marking as fail...',
                  file=sys.stderr)
            adb.unlock_screen_with_pin()
            _toggle_usb_tethering(adb)
            return 'Fail'
        except (socket.timeout, TimeoutError):
            print('\nError: Connection timed-out. Marking as fail...', file=sys.stderr)
            adb.unlock_screen_with_pin()
            _toggle_usb_tethering(adb)
            adb.ftp.current_download_byte_count = 0
            return 'Fail'


def test_2g_throughput(adb):
    _set_rat(adb, '2g')
    return _time_download(adb, adb.ftp.two_g_download_filename)


def test_3g_throughput(adb):
    _set_rat(adb, '3g')
    return _time_download(adb, adb.ftp.three_g_download_filename)


def test_4g_throughput(adb):
    _set_rat(adb, '4g')
    return _time_download(adb, adb.ftp.four_g_download_filename)


def test_wifi_throughput(adb):
    _toggle_wifi(adb)
    result = _time_download(adb, adb.ftp.wifi_download_filename)
    _toggle_wifi(adb)
    return result
