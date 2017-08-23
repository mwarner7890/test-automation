import unittest
import test_runner as tr


class TestTestRunner(unittest.TestCase):
    def test_cmd_line_args_test_only_single(self):
        cmd_args = ['path', 'test_only', 'test_one']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_one'])
        self.assertEqual(error, '')

    def test_cmd_line_args_test_only_multiple(self):
        cmd_args = ['path', 'test_only', 'test_one', 'test_two']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_one', 'test_two'])
        self.assertEqual(error, '')

        cmd_args = ['path', 'test_only', 'test_one', 'test_two', 'test_three']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_one', 'test_two', 'test_three'])
        self.assertEqual(error, '')

    def test_cmd_line_args_test_standard_tests(self):
        cmd_args = ['path', 'standard_tests']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_file_commander_version',
                                      'test_file_commander_version_directly'])
        self.assertEqual(error, '')

    def test_cmd_line_args_throughput_test(self):
        cmd_args = ['path', 'throughput_test', '4g']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_4g_throughput'])
        self.assertEqual(error, '')

    def test_cmd_line_args_throughput_test_without_network(self):
        cmd_args = ['path', 'throughput_test']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the network to test.\n'
                                'Usage: throughput_test 2g/3g/4g/wifi')

    def test_cmd_line_args_throughput_test_without_args(self):
        cmd_args = ['path', 'throughput_test']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the network to test.\n'
                                'Usage: throughput_test 2g/3g/4g/wifi')

    def test_cmd_line_args_test_only_without_tests_specified(self):
        cmd_args = ['path', 'test_only']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the tests to run.\n'
                                'Usage: test_only test1 test2')

    def test_cmd_line_args_no_args_specified(self):
        cmd_args = ['path']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Usage:\n'
                                'To run standard tests (single device): standard_tests\n'
                                'To run specific standard test(s): test_only <test1> <test2>\n'
                                'To run throughput tests (between two devices): '
                                'throughput_testing <2g/3g/4g/wifi>')

    def test_cmd_line_args_invalid_args(self):
        cmd_args = ['path', 'test_blahblahblah']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Unknown option "test_blahblahblah"\n'
                                'Usage:\n'
                                'To run standard tests (single device): standard_tests\n'
                                'To run specific standard test(s): test_only <test1> <test2>\n'
                                'To run throughput tests (between two devices): '
                                'throughput_testing <2g/3g/4g/wifi>')


if __name__ == '__main__':
    unittest.main()
