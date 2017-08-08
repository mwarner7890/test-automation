import unittest
from adb_extended import AdbExtended


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.adbe = AdbExtended('/usr/bin/adb')
        self.adbe.pyadb.start_server()

        self.adbe.wait_for_device()
        self.adbe.unlock_screen_with_pin()

    def tearDown(self):
        self.adbe.input_key_event('KEYCODE_HOME')
        self.adbe.input_key_event('KEYCODE_POWER')

    def test_file_commander_version(self):
        self.adbe.launch_activity('com.mobisystems.fileman/com.mobisystems.files.FileBrowser')
        print self.adbe.get_screen_contents()


if __name__ == '__main__':
    unittest.main()
