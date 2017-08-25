import time

def _toggle_usb_tethering(adb):
    adb.launch_activity('com.android.settings/.TetherSettings')
    adb.input_tap(x="29%", y="28%")


# def _test_throughput(adb):
#     return ftp_file_path


def test_2g_throughput(adb):
    print('TODO: 2G throughput test!')
    _toggle_usb_tethering(adb)
    time.sleep(3)


def test_3g_throughput(adb):
    print('TODO: 2G throughput test!')


def test_4g_throughput(adb):
    print('TODO: 3G throughput test!')


def test_wifi_throughput(adb):
    print('TODO: WiFi throughput test!')
