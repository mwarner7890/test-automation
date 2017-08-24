def _start_file_commander(adb):
    adb.launch_activity('com.mobisystems.fileman/com.mobisystems.files.FileBrowser')
    if 'Welcome to' in adb.get_screen_xml():
        adb.input_tap(x="36%", y="95%")
        adb.input_tap(x="36%", y="95%")
        adb.grant_permissions()
    if 'Sign up' in adb.get_screen_xml():
        adb.input_tap(x="93%", y="8%")


def test_file_commander_version(adb):
    _start_file_commander(adb)
    adb.input_tap(x="7%", y="8%")
    adb.input_swipe(start_x="35%", start_y="95%", end_x="35%", end_y="2%")
    adb.input_tap(x="24%", y="63%")
    adb.input_swipe(start_x="35%", start_y="95%", end_x="35%", end_y="2%")
    adb.input_tap(x="21%", y="95%")

    screen_xml = adb.get_screen_xml()
    adb.clear_most_recent_app()

    return '3.9.14746' in screen_xml


def test_file_commander_version_directly(adb):
    dump = adb.get_stdout_from_command(
        'adb shell dumpsys package com.mobisystems.fileman')
    return '3.9.14746' in dump
