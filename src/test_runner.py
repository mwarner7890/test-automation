import adb as adb_module
import csv
import os
import standard_testing
import throughput_testing
import subprocess
import sys
from throughput_ftp import ThroughputFTP


def set_up(adb_instance):
    adb_instance.start_server()
    adb_instance.unlock_screen_with_pin()


def tear_down(adb_instance):
    adb_instance.input_key_event_sequence(['KEYCODE_HOME',
                                          'KEYCODE_POWER'])


def run_tests(**kwargs):
    adb_instances = [kwargs.get('adb_device_1'),
                     kwargs.get('adb_device_2')]
    num_of_tests = len(test_names)
    test_count = 1
    passed_count = 0
    failed_count = 0
    running_throughput_test = sys.argv[1] == 'throughput_test'
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
            csv_filename = test_names[0] + '.csv'
            _create_csv_file_for_results(csv_filename, adb_device_1.model_name,
                                         adb_device_2.model_name)
            ftp_config_dir = os.path.expanduser('~') + '/Documents/throughput_test'
            ftp_config_fname = 'ftp_config.json'
            ftp = ThroughputFTP(ftp_config_dir, ftp_config_fname)
            for _ in range(0, ftp.test_count):
                temp_results = []
                for adb_instance in adb_instances:
                    if adb_instance:
                        set_up(adb_instance)
                        adb_instance.ftp = ftp
                        temp_result = test_method(adb_instance)
                        if temp_result == 'Fail':
                            failed_count += 1
                        else:
                            passed_count += 1
                        temp_results.append(temp_result)
                        tear_down(adb_instance)
                _add_line_to_results_csv(temp_results, csv_filename)
        else:
            set_up(adb_instances[0])
            test_passed = test_method(adb_instances[0])

            if test_passed:
                passed_count += 1
            else:
                failed_count += 1
            print(eval_test_result(test_passed))

        for adb_instance in adb_instances:
            if adb_instance and not running_throughput_test:
                tear_down(adb_instance)
        test_count += 1

    if running_throughput_test:
        print('Finished running {} tests(s):'.format(num_of_tests))
        print('{} passed'.format(passed_count))
        print('{} failed'.format(failed_count))


def eval_test_result(result):
    if result:
        return 'Test passed'
    return 'Test failed'


def _create_csv_file_for_results(csv_filename, device_model_name_1,
                                 device_model_name_2):
    results_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'throughput_test',
                               'results')
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    with open(os.path.join(results_dir, csv_filename), 'w+',
              newline="\n", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([device_model_name_1, device_model_name_2])


def _add_line_to_results_csv(results_line, csv_filename):
    results_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'throughput_test',
                               'results')

    with open(os.path.join(results_dir, csv_filename), 'a',
              newline="\n", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([results_line[0], results_line[1]])


def _parse_cmd_line_args(args):  # TODO: simplify this!!!
    parsed_test_names = []
    parse_error = ''
    usage_msg = 'Usage:\n' \
                'To run standard tests (single device): standard_tests\n' \
                'To run specific standard test(s): test_only <test1> <test2>\n' \
                'To run throughput tests (between two devices):\n' \
                '    All throughput testing: throughput_test all\n' \
                '    Specific RAT/Wi-Fi testing: throughput_test <2g/3g/4g/wifi>'

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
                parse_error = 'Please specify the RAT or WiFi.\n'\
                    'Usage: throughput_test 2g/3g/4g/wifi'
            else:
                if args[2] == 'all':
                    parsed_test_names = [obj for obj in dir(throughput_testing) if 'test_' in obj]
                else:
                    if len(args) > 3:
                        for parsed_test_type in args[2:]:
                            parsed_test_names.append('test_{}_throughput'.format(parsed_test_type))
                    else:
                        if args[2] not in ['2g', '3g', '4g', 'wifi']:
                            parse_error = 'Please specify the RAT or WiFi.\n'\
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


def _get_device_model_name(device_name):
    model_name = adb_module.get_stdout_from_command(
        'adb -s {} shell getprop ro.product.model'.format(device_name))
    return model_name.replace('b\'', '').replace('\\r', '').replace('\\n', '')[:-1]


if __name__ == '__main__':
    test_names, error = _parse_cmd_line_args(sys.argv)
    if error:
        print(error)
    else:
        if 'throughput' in test_names[0]:
            try:
                device_name_1, device_name_2 = _get_device_names()
                adb_device_1 = adb_module.Adb(device_name=device_name_1,
                                              model_name=_get_device_model_name(device_name_1))
                adb_device_2 = adb_module.Adb(device_name=device_name_2,
                                              model_name=_get_device_model_name(device_name_2))
                run_tests(adb_device_1=adb_device_1, adb_device_2=adb_device_2)
            except ValueError:
                print('Please connect two devices for throughput testing',
                      file=sys.stderr)
            except KeyboardInterrupt:
                print('Stopping setup... (interrupted by user)')

        else:
            try:
                run_tests(adb_device_1=adb_module.Adb())
            except subprocess.CalledProcessError:
                print('Please connect one device for standard tests',
                      file=sys.stderr)
            except KeyboardInterrupt:
                print('Stopping tests... (interrupted by user)')
