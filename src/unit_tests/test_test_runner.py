import unittest
import test_runner as tr


class TestTestRunner(unittest.TestCase):
    def test_cmd_line_args_test_only_single(self):
        cmd_args = ['path', 'test_only', 'test_one']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, ['test_one'])
        self.assertEqual(error, '')

    def test_cmd_line_args_test_only_multiple(self):
        cmd_args = ['path', 'test_only', 'test_one', 'test_two']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, ['test_one', 'test_two'])
        self.assertEqual(error, '')

        cmd_args = ['path', 'test_only', 'test_one', 'test_two', 'test_three']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, ['test_one', 'test_two', 'test_three'])
        self.assertEqual(error, '')

    def test_cmd_line_args_test_standard_tests(self):
        cmd_args = ['path', 'standard_tests']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, ['test_file_commander_version',
                                      'test_file_commander_version_directly'])
        self.assertEqual(error, '')

    def test_cmd_line_args_throughput_test(self):
        cmd_args = ['path', 'throughput_test', '4g', 'device1', 'device2']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, ['device1', 'device2'])
        self.assertEqual(test_names, ['test_4g_throughput'])
        self.assertEqual(error, '')

    def test_cmd_line_args_throughput_test_without_devices(self):
        cmd_args = ['path', 'throughput_test', '4g']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, ['test_4g_throughput'])
        self.assertEqual(error, 'Please specify the two devices to test.\n'
                                'Usage: python test_runner.py throughput_test 2g/3g/4g/wifi device1 device2')

    def test_cmd_line_args_throughput_test_without_speed(self):
        cmd_args = ['path', 'throughput_test', 'device1', 'device2']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the speed to test.\n'
                                'Usage: python test_runner.py throughput_test 2g/3g/4g/wifi device1 device2')

    def test_cmd_line_args_throughput_test_without_args(self):
        cmd_args = ['path', 'throughput_test']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Usage: python test_runner.py throughput_test 2g/3g/4g/wifi device1 device2')

    def test_cmd_line_args_test_only_without_tests_specified(self):
        cmd_args = ['path', 'test_only']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the tests to run.\n'
                                'Usage: python test_runner.py test_only test1 test2')

    def test_cmd_line_args_no_args_specified(self):
        cmd_args = ['path']
        devices, test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(devices, [])
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Usage:\n'
                                'To run specific test(s): python test_runner.py test_only test1 test2\n'
                                'To run standard tests (single device): python test_runner.py standard_tests\n'
                                'To run throughput tests (between two devices): '
                                'python test_runner.py throughput_testing 2g/3g/4g/wifi (where 2g/3g/4g/wifi is s41, s31 etc...)')


if __name__ == '__main__':
    unittest.main()
