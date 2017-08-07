import unittest
from adb_extended import AdbExtended


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.adbe = AdbExtended('/usr/bin/adb')
        self.adbe.pyadb.start_server()

        print 'DEBUG: waiting for device'
        print self.adbe.wait_for_device()

    def test_unlock_screen(self):
        print 'unlocking screen...'
        self.adbe.unlock_screen_with_pin()
        self.adbe.input_key_event('KEYCODE_POWER')


if __name__ == '__main__':
    unittest.main()
