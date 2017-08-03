def wait_for_phone(adb):
    adb.wait_for_device()
    phone = adb.get_devices()
    return phone


def unlock_screen_with_pin(adb, pin):
    adb.input_key_event('KEYCODE_POWER')
    adb.input_swipe(320, 1000, 320, 200)
    adb.input_text(str(pin))
    adb.input_key_event('KEYCODE_ENTER')


def launch_activity(adb, activity_name):
    adb.shell_command('am start -n {}'.format(activity_name))


def input_key_event(adb, keyevent):
    adb.shell_command('input keyevent {}'.format(keyevent))


def input_tap(adb, x, y):
    adb.shell_command('input tap {} {}'
                           .format(str(x), str(y)))


def input_swipe(adb, startx, starty, endx, endy):
    adb.shell_command('input swipe {} {} {} {}'
                           .format(str(startx), str(starty),
                                   str(endx), str(endy)))


def input_text(adb, text):
    adb.shell_command('input text {}'.format(text))
