from subprocess import call


def start_server():
    call(['adb', 'start-server'])


def wait_for_device():
    call(['adb', 'wait-for-device'])


def adb_shell_cmd(cmd):
    call(['adb', 'shell'] + cmd)


def input_key_event(keyevent):
    adb_shell_cmd(['input', 'keyevent', keyevent])


def input_tap(x, y):
    adb_shell_cmd(['input', 'tap', str(x), str(y)])


def input_swipe(startx, starty, endx, endy):
    adb_shell_cmd(['input', 'swipe', str(startx),
                   str(starty), str(endx),
                   str(endy)])


def input_text(text):
    adb_shell_cmd(['input', 'text', text])


def unlock_screen_with_pin(pin=None):
    input_key_event('KEYCODE_POWER')
    input_swipe(320, 1000, 320, 200)
    if pin:
        input_text(str(pin))
        input_key_event('KEYCODE_ENTER')
    input_key_event('KEYCODE_HOME')


def launch_activity(activity_name):
    call(['adb', 'shell', 'am', 'start', '-n'] + [activity_name])


def get_screen_contents():
    call(['adb', 'exec-out', 'uiautomator', 'dump', '/dev/tty'])


"""
TODO: This method should get the contents of the screen. 
The data will be returned in an XML format.

We need this method in general to 
retrieve values from the screen and assert that they are correct (e.g., the correct 
version number for File Commander).

Additionally, another use for it is to allow the test program to 'know' what is 
on the screen, and where to tap. For instance, if File Commander is run for the 
first time, we need to know if it is asking us to accept the license agreement. 
Otherwise, we assume it has already been accepted before and we can interact with 
the app as normal.
"""
