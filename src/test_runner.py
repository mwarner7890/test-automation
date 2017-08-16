import adb
import standard_testing
import throughput_testing
import sys


def set_up():
    adb.start_server()

    adb.wait_for_device()
    adb.unlock_screen_with_pin()
    adb.clear_sim_card_msg()


def tear_down():
    adb.input_key_event('KEYCODE_HOME')
    adb.input_key_event('KEYCODE_POWER')


def run_tests():
    num_of_tests = len(test_names)
    test_count = 1
    passed_count = 0
    failed_count = 0
    for test_name in test_names:
        print('Running test ({}/{}): {}'.format(test_count,
                                                num_of_tests,
                                                test_name))
        try:
            if sys.argv[1] == 'throughput_test':
                test_method = getattr(throughput_testing, test_name)
            else:
                test_method = getattr(standard_testing, test_name)
        except AttributeError:
            print('Error: No test case named {}'.format(test_name))
            tear_down()
            num_of_tests -= 1
            continue
        set_up()
        test_passed = test_method()
        if test_passed:
            passed_count += 1
        else:
            failed_count += 1

        print(eval_test_result(test_passed))
        tear_down()
        test_count += 1

    print('Finished running {} tests(s):'.format(num_of_tests))
    print('{} passed'.format(passed_count))
    print('{} failed'.format(failed_count))


def eval_test_result(result):
    if result:
        return 'Test passed'
    return 'Test failed'


def _parse_cmd_line_args(args):
    parsed_devices = []
    parsed_test_names = []
    parse_error = ''
    if len(args) == 1:
        parse_error = 'Usage:\n' \
                      'To run specific test(s): python test_runner.py test_only <test1> <test2>\n' \
                      'To run standard tests (single device): python test_runner.py standard_tests\n' \
                      'To run throughput tests (between two devices): ' \
                      'python test_runner.py throughput_testing <2g/3g/4g/wifi>'
    else:
        if args[1] == 'test_only':
            if args[2:]:
                parsed_test_names = args[2:]
            else:
                parse_error = 'Please specify the tests to run.\n' \
                              'Usage: python test_runner.py test_only test1 test2'
        elif args[1] == 'standard_tests':
            parsed_test_names = [obj for obj in dir(standard_testing) if 'test_' in obj]
        elif args[1] == 'throughput_test':
            if len(args) < 3:
                parse_error = 'Usage: python test_runner.py throughput_test 2g/3g/4g/wifi device1 device2'
            else:
                if args[2] not in ['2g', '3g', '4g', 'wifi']:
                    parse_error = 'Please specify the speed to test.\n' \
                                  'Usage: python test_runner.py throughput_test 2g/3g/4g/wifi device1 device2'
                else:
                    parsed_test_names = ['test_{}_throughput'.format(args[2])]
                    if len(args) < 4:
                        parse_error = 'Please specify the two devices to test.\n' \
                                      'Usage: python test_runner.py throughput_test 2g/3g/4g/wifi device1 device2'
                    parsed_devices = args[3:]

    return parsed_devices, parsed_test_names, parse_error

if __name__ == '__main__':
    devices, test_names, error = _parse_cmd_line_args(sys.argv)
    if error:
        print(error)
    else:
        run_tests()
