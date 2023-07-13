import discord
from core.info import Info
pc = Info()

def CheckHwid(HWID):
	if HWID == pc.HWID():
		return True
	else:
		return False

async def SendOutput(interaction, output):
	output_embed = discord.Embed(description=f'**__Output__**\n```\n{output}\n```')
	await interaction.response.send_message(content = '', embed = output_embed)