import unittest
import adb


class TestRunner(unittest.TestCase):
    def setUp(self):
        adb.start_server()

        adb.wait_for_device()
        adb.unlock_screen_with_pin()
        adb.clear_sim_card_msg()

    def tearDown(self):
        adb.input_key_event('KEYCODE_HOME')
        adb.input_key_event('KEYCODE_POWER')

    def test_file_commander_version(self):
        self._start_file_commander()
        adb.input_tap(50, 100)
        adb.input_swipe(250, 1200, 250, 30)
        adb.input_tap(175, 800)
        adb.input_swipe(250, 1200, 250, 30)
        adb.input_tap(150, 1200)

        self.assertIn('3.9.14746',
                      adb.get_screen_xml())
        adb.clear_all_apps()

    def test_file_commander_version_directly(self):
        dump = adb.get_stdout_from_command(
            'adb shell dumpsys package com.mobisystems.fileman')
        self.assertIn('3.9.14746', dump)

    @staticmethod
    def _start_file_commander():
        adb.launch_activity('com.mobisystems.fileman/com.mobisystems.files.FileBrowser')
        if 'Welcome to' in adb.get_screen_xml():
            adb.input_tap(260, 1220)
            adb.input_tap(260, 1220)
            adb.grant_permissions()
        if 'Sign up' in adb.get_screen_xml():
            adb.input_tap(670, 100)


if __name__ == '__main__':
    unittest.main()
