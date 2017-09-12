from subprocess import call
from subprocess import check_output


class Adb:
    def __init__(self):
        call(['adb', 'wait-for-device'])
        self.screen_res = self.get_screen_resolution()

    @staticmethod
    def start_server():
        call(['adb', 'start-server'])

    @staticmethod
    def run_shell_cmd(cmd):
        call(['adb', 'shell'] + cmd.split(' '))

    def input_key_event(self, keyevent):
        self.run_shell_cmd('input keyevent {}'.format(keyevent))
    
    def input_tap(self, **kwargs):
        self._convert_relative_coords_if_used(kwargs)
        self.run_shell_cmd('input tap {} {}'.format(str(kwargs['x']), str(kwargs['y'])))

    def input_swipe(self, **kwargs):
        self._convert_relative_coords_if_used(kwargs)
        self.run_shell_cmd('input swipe {} {} {} {}'.format(str(kwargs['start_x']), str(kwargs['start_y']),
                                                            str(kwargs['end_x']), str(kwargs['end_y'])))

    def _convert_relative_coords_if_used(self, kwargs):
        for coord in kwargs:
            if type(kwargs[coord]) == str:
                kwargs[coord] = int(kwargs[coord].split('%')[0])
                kwargs[coord] = (kwargs[coord] / 100) * int(self.screen_res[coord[-1]])

    def input_text(self, text):
        self.run_shell_cmd('input text {}'.format(text))

    def unlock_screen_with_pin(self, pin=None):
        self.input_key_event('KEYCODE_POWER')
        self.input_swipe(start_x="44%", start_y="78%", end_x="44%", end_y="16%")
        if pin:
            self.input_text(str(pin))
            self.input_key_event('KEYCODE_ENTER')
        self.input_key_event('KEYCODE_HOME')

    def clear_sim_card_msg(self):
        if 'No SIM card' in self.get_screen_xml():
            self.input_tap(x=250, y=250)

    def launch_activity(self, activity_name):
        self.run_shell_cmd('am start -n {}'.format(activity_name))

    def clear_all_apps(self):  # Android 7 only!!!
        self.input_key_event('KEYCODE_APP_SWITCH')
        self.input_swipe(start_x="44%", start_y="16%", end_x="44%", end_y="78%")
        self.input_tap(x="82%", y="9%")

    def clear_most_recent_app(self):
        self.input_key_event('KEYCODE_APP_SWITCH')
        self.input_swipe(start_x="44%", start_y="78%", end_x="44%", end_y="16%")
        self.input_swipe(start_x="25%", start_y="75%", end_x="100%", end_y="75%")

    @staticmethod
    def get_stdout_from_command(cmd):
        return str(
            check_output(cmd.split(' '))
        )

    def grant_permissions(self):
        self.input_tap(x="77%", y="64%")

    def get_screen_xml(self):
        return self.get_stdout_from_command('adb exec-out uiautomator dump /dev/tty')

    def get_screen_resolution(self):
        info = self.get_stdout_from_command('adb shell dumpsys window')
        info = info.split('init=')[1].split('x')
        x = info[0]
        y = info[1].split(' ')[0]
        return {'x': x, 'y': y}

    def get_device_names(self):
        raw_output = self.get_stdout_from_command('adb devices')
        return raw_output.replace('\\tdevice', '').split('\\r\\n')[1:][:-2]
