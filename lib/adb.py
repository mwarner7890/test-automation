from subprocess import call
from subprocess import check_output


def start_server():
    call(['adb', 'start-server'])


def wait_for_device():
    call(['adb', 'wait-for-device'])


def run_shell_cmd(cmd):
    call(['adb', 'shell'] + cmd.split(' '))


def input_key_event(keyevent):
    run_shell_cmd('input keyevent {}'.format(keyevent))


def input_tap(x, y):
    run_shell_cmd('input tap {} {}'.format(str(x), str(y)))


def input_swipe(startx, starty, endx, endy):
    run_shell_cmd('input swipe {} {} {} {}'.format(str(startx), str(starty), str(endx),
                                                   str(endy)))


def input_text(text):
    run_shell_cmd('input text {}'.format(text))


def unlock_screen_with_pin(pin=None):
    input_key_event('KEYCODE_POWER')
    input_swipe(320, 1000, 320, 200)
    if pin:
        input_text(str(pin))
        input_key_event('KEYCODE_ENTER')
    input_key_event('KEYCODE_HOME')


def clear_sim_card_msg():
    if 'No SIM card' in get_screen_xml():
        input_tap(250, 250)


def launch_activity(activity_name):
    run_shell_cmd('am start -n {}'.format(activity_name))


def clear_all_apps():
    input_key_event('KEYCODE_APP_SWITCH')
    input_tap(590, 120)


def get_stdout_from_command(cmd):
    return str(
        check_output(cmd.split(' '))
    )


def grant_permissions():
    input_tap(555, 820)


def get_screen_xml():
    return get_stdout_from_command('adb exec-out uiautomator dump /dev/tty')
