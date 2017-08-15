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
    devices = []
    test_names = []
    message = ''
    if len(args) == 1:
        message = 'Usage: python test_runner.py ' \
                   '<device> -device2 <device2> <test1> <test2> ...'
    else:
        if args[1] == '-device2':
            message = 'Please specify primary device'
        else:
            if args[1] != 'all' and args[2] == '-device2':
                devices = [args[1], args[3]]
                test_names = args[4:]
            else:
                if test_names == ['all']:
                    test_names = [obj for obj in dir(test_cases) if 'test_' in obj]
                else:
                    test_names = args[2:]
                    devices = [args[1]]


    return devices, test_names, message

if __name__ == '__main__':
    print(sys.argv)
    test_names, devices, message = args = _parse_cmd_line_args(sys.argv)
    if message:
        print(message)
    else:
        run_tests()
