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


if __name__ == '__main__':
    unittest.main()
