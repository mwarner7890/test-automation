import unittest
import adb_test_functions
from pyadb import ADB


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.adb = ADB()
        self.adb.set_adb_path('/usr/bin/adb')
        self.adb.start_server()

        print 'DEBUG: waiting for device'
        # TODO: Probably revise adb_test_functions approach...
        print adb_test_functions. \
            wait_for_device(self.adb)

    def test_unlock_screen(self):
        print 'unlocking screen...'
        adb_test_functions.unlock_screen_with_pin(self.adb)
        adb_test_functions.input_key_event(self.adb, 'KEYCODE_POWER')


if __name__ == '__main__':
    unittest.main()
