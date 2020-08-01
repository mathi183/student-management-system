import sys
from cx_Freeze import setup, Executable

import os.path
#PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.file))
#os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
#os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files":['tcl86t.dll','tk86t.dll']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
'''
options = {
    'build.exe': {'include_files': [
    os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
    os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
    ],
    },
}
'''

setup(  name = "Student Management System",
        version = "0.1",
        description = "Student Management System developed by https://mathiconsultant.com",
        options = {"build_exe": build_exe_options},
        executables = [Executable("student_management_system.py", base=base, icon = 'mathi.ico')])