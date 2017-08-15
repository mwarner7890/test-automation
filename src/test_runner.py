import adb
import test_cases
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
            test_method = getattr(test_cases, test_name)
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
        parse_error = 'Usage: python test_runner.py ' \
                   '<device> -device2 <device2> <test1> <test2> ...'
    else:
        if args[1] == '-device2':
            parse_error = 'Please specify primary device'
        else:
            if args[1] != 'all' and args[2] == '-device2':
                parsed_devices = [args[1], args[3]]
                parsed_test_names = args[4:]
            else:
                if parsed_test_names == ['all']:
                    parsed_test_names = [obj for obj in dir(test_cases) if 'test_' in obj]
                else:
                    parsed_test_names = args[2:]
                    parsed_devices = [args[1]]

    return parsed_devices, parsed_test_names, parse_error

if __name__ == '__main__':
    test_names, devices, error = _parse_cmd_line_args(sys.argv)
    if error:
        print(error)
    else:
        run_tests()
