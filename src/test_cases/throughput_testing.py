import adb


def _test_throughput(ftp_file_path):
    return ftp_file_path


def _toggle_usb_tethering():
    adb.launch_activity('com.android.settings/.TetherSettings')
    adb.input_tap_abs(210, 360)


def test_2g_throughput():
    print('TODO: 2G throughput test!')


def test_3g_throughput():
    print('TODO: 2G throughput test!')


def test_4g_throughput():
    print('TODO: 3G throughput test!')


def test_wifi_throughput():
    print('TODO: WiFi throughput test!')
