from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('adb.py', base=base, targetName = 'test_automation.exe')
]

setup(name='TestAutomation',
      version = '1',
      description = 'Automates tests',
      options = dict(build_exe = buildOptions),
      executables = executables)
