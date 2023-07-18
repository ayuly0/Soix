import requests, socket, os, platform, psutil, subprocess, json, re, uuid

def get_size(bytes_, suffix="B"):
	factor = 1024
	for unit in ["", "K", "M", "G", "T", "P"]:
		if bytes_ < factor:
			return f"{bytes_:.2f}{unit}{suffix}"
		bytes_ /= factor

class Info:
	### IP INFOMATION ###
	def IP(self):
		ip = requests.get('https://api.ipify.org').content.decode('utf-8')
		return ip
		
	def IPData(self):
		r = requests.get('http://ipinfo.io/json')
		data = json.loads(r.text)
		return data

	### SYSTEM INFOMATION ###
	def HostName(self):
		return socket.gethostname()

	def OSVersion(self):
		return platform.version()

	def OSPlatform(self):
		return platform.system()

	def OSRelease(self):
		return platform.release()

	def Processor(self):
		return platform.processor()

	def MacAddress(self):
		mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		return mac_address

	def HWID(self):
		return str(subprocess.check_output('wmic csproduct get uuid', shell=True), 'utf-8').split('\n')[1].strip()

	def WindowProductKey(self):
		try:
			key = str(subprocess.check_output('powershell "(Get-WmiObject -query select * from SoftwareLicensingService).OA3xOriginalProductKey"', shell=True), 'utf-8').split('\n')[1].strip()
		except:
			key = "Not Found Key"
		return key

	### CPU INFOMATION ###
	def PhysicalCores(self):
		return psutil.cpu_count(logical=False)

	def TotalCores(self):
		return psutil.cpu_count(logical=True)

	### MEMORY INFORMATION ###
	def TotalRAM(self):
		return get_size(psutil.virtual_memory().total)

	### DISK INFOMATION ###
	def AllDiskPartitions(self):
		partitions = psutil.disk_partitions()
		lPartitions = []
		for partition in partitions:
			try:
				partition_usage = psutil.disk_usage(partition.mountpoint)
			except PermissionError:
				continue
			lPartitions.append([partition.device, partition.mountpoint, partition.fstype, get_size(partition_usage.total), get_size(partition_usage.used), get_size(partition_usage.free), f'{partition_usage.percent}%'])
		return lPartitions	


	### NETWORK INFOMATION ###
	# def AllNetworkInterfaces(self):
	# 	if_addrs = psutil.net_if_addrs()


