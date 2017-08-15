import unittest
import test_runner as tr


class TestTestRunner(unittest.TestCase):
    def test_cmd_line_args_test_only_single(self):
        cmd_args = ['path', 'test_one']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, ['test_one'])
        self.assertEqual(tr.error, '')

    def test_cmd_line_args_test_only_multiple(self):
        cmd_args = ['path', 'test_one', 'test_two']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, ['test_one', 'test_two'])
        self.assertEqual(tr.error, '')

        cmd_args = ['path', 'test_one', 'test_two', 'test_three']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, ['test_one', 'test_two', 'test_three'])
        self.assertEqual(tr.error, '')

    def test_cmd_line_args_test_standard_tests(self):
        cmd_args = ['path', 'standard_tests']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, ['test_file_commander_version',
                                         'test_file_commander_version_directly'])
        self.assertEqual(tr.error, '')

    def test_cmd_line_args_throughput_test(self):
        cmd_args = ['path', 's41_throughput_test', 'device1','device2']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, ['device1', 'device2'])
        self.assertEqual(tr.test_names, ['s41_throughput_test'])
        self.assertEqual(tr.error, '')

    def test_cmd_line_args_throughput_test_without_devices(self):
        cmd_args = ['path', 's41_throughput_test']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, [])
        self.assertEqual(tr.error, 'Please specify the two devices to test.\n'
                                   'Usage: python test_runner.py ..._throughput_test device1 device2')

    def test_cmd_line_args_test_only_without_tests_specified(self):
        cmd_args = ['path', '']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, [])
        self.assertEqual(tr.error, 'Please specify the tests to run.\n'
                                   'Usage: python test_runner.py test_only test1 test2')

    def test_cmd_line_args_no_args_specified(self):
        cmd_args = ['path', '']
        tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(tr.devices, [])
        self.assertEqual(tr.test_names, [])
        self.assertEqual(tr.error, 'Usage:\n'
                                   'To run specific test(s): python test_runner.py test_only test1 test2\n'
                                   'To run standard tests (single device): python test_runner.py standard_tests\n'
                                   'To run throughput tests (between two devices): '
                                   'python test_runner.py sxx_throughput_testing (where sxx is s41, s31 etc...)')

if __name__ == '__main__':
    unittest.main()
