import adb as adb_module
import json
import os
import standard_testing
import throughput_testing
import sys


def set_up(adb_instance):
    adb_instance.start_server()
    adb_instance.unlock_screen_with_pin()


def tear_down(adb_instance):
    adb_instance.input_key_event('KEYCODE_HOME')
    adb_instance.input_key_event('KEYCODE_POWER')


def _load_ftp_config(ftp_config_dir, ftp_config_fname):
    ftp_config_fullpath = os.path.join(ftp_config_dir, ftp_config_fname)
    if os.path.isfile(ftp_config_fullpath):
        return _load_json_file(ftp_config_fullpath)
    if not os.path.isdir(ftp_config_dir):
        os.makedirs(ftp_config_dir)
    with open(ftp_config_fullpath, 'w') as jsonfile:
        jsonfile.write(json.dumps({
            'address': 'changeme',
            'username': 'changeme',
            'password': 'changeme',
            'download_dir': 'Test-team/Download',
            '2g_download_filename': '2G_Data_Test.zip',
            '3g_download_filename': '3G_Data_Test.zip',
            '4g_download_filename': '4G_Data_Test.zip',
            'wifi_download_filename': 'WiFi-Data_Test.zip'
                                   },
                                  indent=4))
        print('An FTP configuration file has been placed in Documents/throughput_test\n'
              'Please edit this file with the desired settings and run the test runner again.')
    exit(1)


def _load_json_file(fpath):
    with open(fpath, 'r') as jsonfile:
        loaded_json = json.load(jsonfile)
    return loaded_json


def run_tests(**kwargs):
    adb_instances = [kwargs.get('adb_device_1'),
                     kwargs.get('adb_device_2')]
    num_of_tests = len(test_names)
    test_count = 1
    passed_count = 0
    failed_count = 0
    running_throughput_test = sys.argv[1] == 'throughput_test'
    throughput_test_count = 10
    for test_name in test_names:
        print('Running test ({}/{}): {}'.format(test_count,
                                                num_of_tests,
                                                test_name))
        try:
            if running_throughput_test:
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
        if running_throughput_test:
            ftp_config_dir = os.path.expanduser('~') + '/Documents/throughput_test'
            ftp_config_fname = 'ftp_config.json'
            ftp_config = _load_ftp_config(ftp_config_dir, ftp_config_fname)
            for _ in range(0, throughput_test_count):
                for adb_instance in adb_instances:
                    if adb_instance:
                        set_up(adb_instance)
                        test_passed = test_method(adb_instance)  # TODO: throughput tests don't 'pass'
                        tear_down(adb_instance)
        else:
            set_up(adb_instances[0])
            test_passed = test_method(adb_instances[0])

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
