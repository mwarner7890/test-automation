def _start_file_commander(adb):
    adb.launch_activity('com.mobisystems.fileman/com.mobisystems.files.FileBrowser')
    if 'Welcome to' in adb.get_screen_xml():
        adb.input_tap_abs(260, 1220)
        adb.input_tap_abs(260, 1220)
        adb.grant_permissions()
    if 'Sign up' in adb.get_screen_xml():
        adb.input_tap_abs(670, 100)


def test_file_commander_version(adb):
    _start_file_commander(adb)
    adb.input_tap_abs(50, 100)
    adb.input_swipe(250, 1200, 250, 30)
    adb.input_tap_abs(175, 800)
    adb.input_swipe(250, 1200, 250, 30)
    adb.input_tap_abs(150, 1200)

    screen_xml = adb.get_screen_xml()
    adb.clear_all_apps()

    return '3.9.14746' in screen_xml


def test_file_commander_version_directly(adb):
    dump = adb.get_stdout_from_command(
        'adb shell dumpsys package com.mobisystems.fileman')
    return '3.9.14746' in dump
