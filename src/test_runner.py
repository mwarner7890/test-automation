import adb as adb_module
import standard_testing
import throughput_testing
import sys


def set_up(adb_instance):
    adb_instance.start_server()

    adb_instance.unlock_screen_with_pin()
    adb_instance.clear_sim_card_msg()


def tear_down(adb_instance):
    adb_instance.input_key_event('KEYCODE_HOME')
    adb_instance.input_key_event('KEYCODE_POWER')


def run_tests(**kwargs):
    adb_instances = [kwargs.get('adb_device_1'),
                     kwargs.get('adb_device_2')]
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
            for adb_instance in adb_instances:
                if adb_instance:
                    tear_down(adb_instance)
            num_of_tests -= 1
            continue
        for adb_instance in adb_instances:
            if adb_instance:
                set_up(adb_instance)
                test_passed = test_method(adb_instance)
        if test_passed:
            passed_count += 1
        else:
            failed_count += 1

        print(eval_test_result(test_passed))
        for adb_instance in adb_instances:
            if adb_instance:
                tear_down(adb_instance)
        test_count += 1

    print('Finished running {} tests(s):'.format(num_of_tests))
    print('{} passed'.format(passed_count))
    print('{} failed'.format(failed_count))


def eval_test_result(result):
    if result:
        return 'Test passed'
    return 'Test failed'


def _parse_cmd_line_args(args):
    parsed_test_names = []
    parse_error = ''
    usage_msg = 'Usage:\n' \
                'To run standard tests (single device): standard_tests\n' \
                'To run specific standard test(s): test_only <test1> <test2>\n' \
                'To run throughput tests (between two devices): ' \
                'throughput_testing <2g/3g/4g/wifi>'
    if len(args) == 1:
        parse_error = usage_msg
    else:
        if args[1] == 'test_only':
            if args[2:]:
                parsed_test_names = args[2:]
            else:
                parse_error = 'Please specify the tests to run.\n' \
                              'Usage: test_only test1 test2'
        elif args[1] == 'standard_tests':
            parsed_test_names = [obj for obj in dir(standard_testing) if 'test_' in obj]
        elif args[1] == 'throughput_test':
            if len(args) < 3:
                parse_error = 'Please specify the network to test.\n'\
                    'Usage: throughput_test 2g/3g/4g/wifi'
            else:
                if args[2] not in ['2g', '3g', '4g', 'wifi']:
                    parse_error = 'Please specify the network to test.\n'\
                                  'Usage: throughput_test 2g/3g/4g/wifi'
                else:
                    parsed_test_names = ['test_{}_throughput'.format(args[2])]
        else:
            parse_error = 'Unknown option "{}"\n' \
                            '{}'.format(args[1], usage_msg)

    return parsed_test_names, parse_error


def _get_device_names():
    raw_output = adb_module.get_stdout_from_command('adb devices')
    return raw_output.replace('\\tdevice', '').split('\\r\\n')[1:][:-2]


if __name__ == '__main__':
    test_names, error = _parse_cmd_line_args(sys.argv)
    if error:
        print(error)
    else:
        if 'throughput' in test_names[0]:
            device_name_1, device_name_2 = _get_device_names()
            adb_device_1 = adb_module.Adb(device_name=device_name_1)
            adb_device_2 = adb_module.Adb(device_name=device_name_2)
            run_tests(adb_device_1=adb_device_1, adb_device_2=adb_device_2)
        else:
            run_tests(adb_device_1=adb_module.Adb())
