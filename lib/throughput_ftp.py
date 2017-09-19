import json
import os
import tempfile
from ftplib import FTP


class ThroughputFTP:
    def __init__(self, ftp_config_dir, ftp_config_fname):
        ftp_config = _load_ftp_config(ftp_config_dir, ftp_config_fname)

        self.address = ftp_config['address']
        self.username = ftp_config['username']
        self.password = ftp_config['password']
        self.download_dir = ftp_config['download_dir']
        self.two_g_download_filename = ftp_config['2g_download_filename']
        self.three_g_download_filename = ftp_config['3g_download_filename']
        self.four_g_download_filename = ftp_config['4g_download_filename']
        self.wifi_download_filename = ftp_config['wifi_download_filename']
        self.download_timeout = int(ftp_config['download_timeout'])
        self.retry_timer = int(ftp_config['retry_timer'])

    def login_and_download_file_from_ftp(self, filename):
        with FTP(self.address, timeout=self.download_timeout) as ftp:
            ftp.login(user=self.username, passwd=self.password)
            ftp.cwd(self.download_dir)
            with tempfile.TemporaryFile() as tfile:
                ftp.retrbinary('RETR {}'.format(filename), tfile.write)


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
            'wifi_download_filename': 'WiFi-Data_Test.zip',
            'download_timeout': '60',
            'retry_timer': '8'
                                   }, indent=4))

        print('An FTP configuration file has been placed in Documents/throughput_test\n'
              'Please edit this file with the desired settings and run the test runner again.')

    exit(1)


def _load_json_file(fpath):
    with open(fpath, 'r') as jsonfile:
        loaded_json = json.load(jsonfile)
    return loaded_json
