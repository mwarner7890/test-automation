import datetime
import time


def timestamp():
    return '[' + \
           str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) + '] '


def ts_print(string):
    print(timestamp() + string)
