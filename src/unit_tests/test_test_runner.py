import unittest
import test_runner as tr


class TestTestRunner(unittest.TestCase):
    def test_cmd_line_args_only_one_device(self):
        cmd_args = ['path', 'device_one', 
                    'test_one', 'test_two']
        devices, test_names, message = \
            tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, ['device_one'])
        self.assertEqual(test_names, ['test_one', 'test_two'])
        self.assertEqual(message, '')

    def test_cmd_line_args_two_devices(self):
        cmd_args = ['path', 'device_one', '-device2', 'device_two', 
                    'test_one', 'test_two']
        devices, test_names, message = \
            tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, ['device_one', 'device_two'])
        self.assertEqual(test_names, ['test_one', 'test_two'])
        self.assertEqual(message, '')

    def test_cmd_line_args_second_but_not_first_device(self):
        cmd_args = ['path', '-device2', 'device_two', 
                    'test_one', 'test_two']
        devices, test_names, message = \
            tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, [])
        self.assertEqual(message, 'Please specify primary device')

    def test_cmd_line_args_no_args(self):
        cmd_args = ['path']
        devices, test_names, message = \
            tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, [])
        self.assertEqual(message, 'Usage: python test_runner.py '
                                  '<device> -device2 <device2> <test1> <test2> ...')

    def test_cmd_line_args_all(self):
        cmd_args = ['path', 'device_1', 'all']
        devices, test_names, message = \
            tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, ['device_1'])
        self.assertEqual(test_names, ['test_file_commander_version',
                                      'test_file_commander_version_directly'])

if __name__ == '__main__':
    unittest.main()
