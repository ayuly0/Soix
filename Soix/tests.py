from pynput import keyboard
from threading import Thread
import time


def on_press(key):
	pass

def on_release(key):
	pass

with keyboard.Listener(
		suppress=True,
		on_press=on_press,
		on_release=on_release) as listener:
	def time_out(period_sec: int):
		time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
		listener.stop()

	Thread(target=time_out, args=(5.0,)).start()
	listener.join()
