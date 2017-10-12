import os
from subprocess import call
from subprocess import check_output


class Adb:
    def __init__(self, **kwargs):
        self.adb_exe_path = kwargs.get('adb_exe_path')
        self.device_name = kwargs.get('device_name')
        self.model_name = kwargs.get('model_name')
        self.screen_res = self.get_screen_resolution()
        self.prop = self._get_prop()
        self._call_adb_cmd_silently('wait-for-device')

    def _call_adb_cmd_silently(self, cmd):
        cmd = self.adb_exe_path + ' ' + cmd
        call(cmd, stdout=open(os.devnull, 'wb'),
             stderr=open(os.devnull, 'wb'))

    def start_server(self):
        self._call_adb_cmd_silently('start-server')

    def run_shell_cmd(self, cmd):
        if self.device_name:
            self._call_adb_cmd_silently(' -s ' + self.device_name + ' shell ' + cmd)
        else:
            self._call_adb_cmd_silently('shell ' + cmd)

    def input_key_event(self, keyevent):
        self.run_shell_cmd('input keyevent {}'.format(keyevent))

    def input_key_event_sequence(self, key_event_sequence):
        self.run_shell_cmd('input keyevent {}'.format(' '.join(key_event_sequence)))

    def repeat_input_key_event(self, keyevent, count):
        key_event_sequence = []
        for _ in range(0, count):
            key_event_sequence.append(keyevent)
        self.input_key_event_sequence(key_event_sequence)

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

    def lock_screen(self):
        self.input_key_event('KEYCODE_POWER')

    def launch_activity_component(self, activity_name):
        self.run_shell_cmd('am start -n {}'.format(activity_name))

    def launch_activity_action(self, action_name):
        self.run_shell_cmd('am start -a {}'.format(action_name))

    def clear_all_apps(self):  # Android 7 only!!!
        self.input_key_event('KEYCODE_APP_SWITCH')
        self.input_swipe(start_x="44%", start_y="16%", end_x="44%", end_y="78%")
        self.input_tap(x="82%", y="9%")

    def clear_most_recent_app(self):
        self.input_key_event('KEYCODE_APP_SWITCH')
        self.input_swipe(start_x="44%", start_y="78%", end_x="44%", end_y="16%")
        self.input_swipe(start_x="25%", start_y="75%", end_x="100%", end_y="75%")

    def grant_permissions(self):
        self.input_tap(x="77%", y="64%")

    def get_screen_xml(self):
        if self.device_name:
            return get_stdout_from_adb_command('-s {} exec-out uiautomator dump /dev/tty'
                                               .format(self.device_name), adb_exe_path=self.adb_exe_path)
        return get_stdout_from_adb_command('exec-out uiautomator dump /dev/tty',
                                           self.adb_exe_path)

    def get_screen_resolution(self):
        if self.device_name:
            info = get_stdout_from_adb_command('-s {} shell dumpsys window'.
                                               format(self.device_name), self.adb_exe_path)
        else:
            info = get_stdout_from_adb_command('shell dumpsys window',
                                               self.adb_exe_path)

        info = info.split('init=')[1].split('x')
        x = info[0]
        y = info[1].split(' ')[0]
        return {'x': x, 'y': y}

    def device_is_qualcomm(self):
        if self.device_name:
            info = get_stdout_from_adb_command('-s {} shell getprop'.
                                               format(self.device_name), adb_exe_path=self.adb_exe_path)
            return 'qualcomm' in info

    def _get_prop(self):
        if self.device_name:
            getprop = get_stdout_from_adb_command('-s {} shell getprop'.
                                                  format(self.device_name), self.adb_exe_path)
        else:
            getprop = get_stdout_from_adb_command('shell getprop'.
                                                  format(self.device_name), self.adb_exe_path)
        getprop = getprop.replace('\n    ', '').replace('\n', '').replace(']', '').replace(': ', '').split('[')[1:]
        return _list_to_dict(getprop)

    def get_imei(self):
        imei_raw = get_stdout_from_adb_command('-s {} shell service call '
                                               'iphonesubinfo 1'.format(self.device_name),
                                               adb_exe_path=self.adb_exe_path)
        imei = ''
        for imei_part in imei_raw.split('\'')[1::2]:
            imei += imei_part.replace('.', '').replace(' ', '')
        return imei


def _list_to_dict(input_list):
    return_dict = {}
    for key, elem in zip(input_list[::2], input_list[1::2]):
        return_dict[key] = elem
    return return_dict


def get_stdout_from_adb_command(cmd, adb_exe_path):
    cmd = adb_exe_path + ' ' + cmd
    return str(
        check_output(cmd.split(' '))
    )
