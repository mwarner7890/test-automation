def _toggle_usb_tethering(adb):
    adb.launch_activity('com.android.settings/.TetherSettings')
    adb.input_tap_abs(210, 360)


def _test_throughput(adb):
    return ftp_file_path


def test_2g_throughput(adb):
    print('TODO: 2G throughput test!')


def test_3g_throughput(adb):
    print('TODO: 2G throughput test!')


def test_4g_throughput(adb):
    print('TODO: 3G throughput test!')


def test_wifi_throughput(adb):
    print('TODO: WiFi throughput test!')
