import socket
import sys
import time


def _toggle_usb_tethering(adb):
    adb.launch_activity('com.android.settings/.TetherSettings')
    adb.input_tap(x="29%", y="28%")


def _test_throughput(adb, download_filename):
    _toggle_usb_tethering(adb)
    time.sleep(8)
    adb.lock_screen()
    while True:
        try:
            print('Downloading {}/{} through device {}'.
                  format(adb.ftp.download_dir, download_filename, adb.device_name))
            time_started = time.time()
            adb.ftp.login_and_download_file_from_ftp(download_filename)
            time_taken = round(time.time() - time_started)
            print('Download complete; time taken: {} seconds'.format(time_taken))
            adb.unlock_screen_with_pin()
            _toggle_usb_tethering(adb)
            time.sleep(8)
            return time_taken
        except socket.gaierror:
            print('Error: Could not connect to FTP server. Retrying connection...',
                  file=sys.stderr)
            time.sleep(adb.ftp.retry_timer)
        except (socket.timeout, TimeoutError):
            print('Error: Connection timed-out. Retrying download in {} seconds...'
                  .format(adb.ftp.retry_timer), file=sys.stderr)


def test_2g_throughput(adb):
    return _test_throughput(adb, adb.ftp.two_g_download_filename)


def test_3g_throughput(adb):
    return _test_throughput(adb, adb.ftp.three_g_download_filename)


def test_4g_throughput(adb):
    return _test_throughput(adb, adb.ftp.four_g_download_filename)


def test_wifi_throughput(adb):
    return _test_throughput(adb, adb.ftp.wifi_download_filename)
