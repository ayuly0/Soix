import discord
from discord.ext import commands
from pretty_help import PrettyHelp

class Soix(commands.Bot):

	def __init__(self):
		super().__init__(
			command_prefix = '>',
			intents = discord.Intents.all(),
			application_id = 1128617415182389358,
			help = PrettyHelp())

	async def setup_hook(self):
		await self.load_extension("cogs.control")
		await self.load_extension("cogs.other")
		await bot.tree.sync(guild = discord.Object(id = 1117628520273813536))

	async def on_ready(self):
		print(f'--- {self.user} conntected to Discord!')

bot = Soix()
bot.run('MTEyODYxNzQxNTE4MjM4OTM1OA.Gc7kL1.wHDOBwz_Q4DJpKgtNwpZHal3yKiP2KpKno_k5g')