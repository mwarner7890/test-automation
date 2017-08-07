from pyadb import ADB


class AdbExtended:
    def __init__(self, path):
        self.pyadb = ADB(path)

    def wait_for_device(self):
        self.pyadb.wait_for_device()
        device = self.pyadb.get_devices()
        return device

    def unlock_screen_with_pin(self, pin=None):
        self.input_key_event('KEYCODE_POWER')
        self.input_swipe(320, 1000, 320, 200)
        if pin:
            self.input_text(str(pin))
            self.input_key_event('KEYCODE_ENTER')

    def launch_activity(self, activity_name):
        self.pyadb.shell_command('am start -n {}'.format(activity_name))

    def input_key_event(self, keyevent):
        self.pyadb.shell_command('input keyevent {}'.format(keyevent))

    def input_tap(self, x, y):
        self.pyadb.shell_command('input tap {} {}'
                                 .format(str(x), str(y)))

    def input_swipe(self, startx, starty, endx, endy):
        self.pyadb.shell_command('input swipe {} {} {} {}'.
                                 format(str(startx), str(starty), str(endx), str(endy)))

    def input_text(self, text):
        self.pyadb.shell_command('input text {}'.format(text))

    def get_screen_contents(self):
        pass
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
