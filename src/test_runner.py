import unittest
import adb


class TestRunner(unittest.TestCase):
    def setUp(self):
        adb.start_server()

        adb.wait_for_device()
        adb.unlock_screen_with_pin()

    def tearDown(self):
        adb.input_key_event('KEYCODE_HOME')
        adb.input_key_event('KEYCODE_POWER')

    def test_file_commander_version(self):
        adb.launch_activity('com.mobisystems.fileman/com.mobisystems.files.FileBrowser')
        print(adb.get_screen_contents())


if __name__ == '__main__':
    unittest.main()
