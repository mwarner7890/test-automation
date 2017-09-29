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

    def test_cmd_line_args_throughput_test_all(self):
        cmd_args = ['path', 'throughput_test', 'all']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_2g_throughput', 'test_3g_throughput',
                                      'test_4g_throughput', 'test_wifi_throughput'])
        self.assertEqual(error, '')

    def test_cmd_line_args_specific_throughput_tests(self):
        cmd_args = ['path', 'throughput_test', '4g']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_4g_throughput'])
        self.assertEqual(error, '')
        cmd_args = ['path', 'throughput_test', '2g', '3g']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_2g_throughput', 'test_3g_throughput'])
        self.assertEqual(error, '')
        cmd_args = ['path', 'throughput_test', '2g', '3g', '4g']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, ['test_2g_throughput', 'test_3g_throughput',
                                      'test_4g_throughput'])
        self.assertEqual(error, '')

    def test_cmd_line_args_throughput_test_without_network(self):
        cmd_args = ['path', 'throughput_test']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the RAT or WiFi.\n'
                                'Usage: throughput_test 2g/3g/4g/wifi')

    def test_cmd_line_args_throughput_test_without_args(self):
        cmd_args = ['path', 'throughput_test']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Please specify the RAT or WiFi.\n'
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
                                'To run throughput tests (between two devices):\n'
                                '    All throughput testing: throughput_test all\n'
                                '    Specific RAT/Wi-Fi testing: throughput_test <2g/3g/4g/wifi>')

    def test_cmd_line_args_invalid_args(self):
        cmd_args = ['path', 'test_blahblahblah']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Unknown option "test_blahblahblah"\n'
                                'Usage:\n'
                                'To run standard tests (single device): standard_tests\n'
                                'To run specific standard test(s): test_only <test1> <test2>\n'
                                'To run throughput tests (between two devices):\n'
                                '    All throughput testing: throughput_test all\n'
                                '    Specific RAT/Wi-Fi testing: throughput_test <2g/3g/4g/wifi>')

    def test_cmd_line_args_throughput_test_suite(self):
        cmd_args = ['path', 'test_blahblahblah']
        test_names, error = tr._parse_cmd_line_args(cmd_args)
        self.assertEqual(test_names, [])
        self.assertEqual(error, 'Unknown option "test_blahblahblah"\n'
                                'Usage:\n'
                                'To run standard tests (single device): standard_tests\n'
                                'To run specific standard test(s): test_only <test1> <test2>\n'
                                'To run throughput tests (between two devices):\n'
                                '    All throughput testing: throughput_test all\n'
                                '    Specific RAT/Wi-Fi testing: throughput_test <2g/3g/4g/wifi>')


if __name__ == '__main__':
    unittest.main()
