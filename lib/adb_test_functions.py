def wait_for_device(adb):
    adb.wait_for_device()
    device = adb.get_devices()
    return device


def unlock_screen_with_pin(adb, pin=None):
    input_key_event(adb, 'KEYCODE_POWER')
    input_swipe(adb, 320, 1000, 320, 200)
    if pin:
        input_text(adb, str(pin))
        input_key_event(adb, 'KEYCODE_ENTER')


def launch_activity(adb, activity_name):
    adb.shell_command('am start -n {}'.format(activity_name))


def input_key_event(adb, keyevent):
    adb.shell_command('input keyevent {}'.format(keyevent))


def input_tap(adb, x, y):
    adb.shell_command('input tap {} {}'
                      .format(str(x), str(y)))


def input_swipe(adb, startx, starty, endx, endy):
    adb.shell_command('input swipe {} {} {} {}'.
                      format(str(startx), str(starty), str(endx), str(endy)))


def input_text(adb, text):
    adb.shell_command('input text {}'.format(text))
