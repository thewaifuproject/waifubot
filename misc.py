###MISCELANEOUS###
import discord
from discord.ext import commands
import random
import time
import json

class misc:
	def __init__(self, client):
		self.client = client

	#async def on_message_delete(self, message):
	#	await self.client.send_message(message.channel, "Message deleted.")

	async def on_message(self, message):

		if message.content ==  "Best waifu?":
			await self.client.send_message(message.channel, "I'm the best waifu!")
		if message.content ==  "Best husbando?":
			if message.author.id == '424221454490402816':
				await self.client.send_message(message.channel, "Definitely you are the best husbando!")
			else:
				userID = message.author.id
				await self.client.send_message(message.channel, "<@%s> you ain't, sorry~" % (userID))
		if message.content.upper().startswith("PLS CHAIN"):
			await self.client.send_message(message.channel, "If you say please, you know I can't say no :blush:")
		if message.content.upper().startswith("PLS AMIBETATESTER?"):
			if "517740341907030026" in [role.id for role in message.author.roles]:
				await self.client.send_message(message.channel, "Yes, you are. Yaay~")
			if "523211588870602753" in [role.id for role in message.author.roles]:
				await self.client.send_message(message.channel, "You are a dev, you should be creating more content. Uhhh... pretty please?")
			else:
				await self.client.send_message(message.channel, "You are not, thats too bad. Go get a waifu at `WaifuChain.moe` to enter the beta test. Easy, right?")
	#As .event has priority over .commands, this lines allows the bot to search for cmds if they ain't in .event
	#await self.client.process_commands(message)
		
	@commands.command()
	async def ping(self):
		await self.client.say('Uhhhh, *pong* I guess...')
		
	#await client.send_message(message.channel, "%a" % (args[1]))
	#takes the first word the user said

	@commands.command()
	async def say(self, *args):
		output = ''
		for word in args:
			output += word
			output += ' '
		await self.client.say(output)
	
	@commands.command(pass_context=True)
	async def fuck(self, ctx):
		fuker = ctx.message.author
		await self.client.say("How you dare? I am a pure maiden! \n**User %s has now been banned.**" % (fuker))
		
	@commands.command()
	async def add(self, left : int, right : int):
		await self.client.say(left + right)

		
	@commands.command()
	async def subs(self, left : int, right : int):
		await self.client.say(left - right)

		
	@commands.command()
	async def choose(self, *choices : str):
		await self.client.say("I'll go with '%s'!" % (random.choice(choices)))	
		
	@commands.command()
	async def heresince(self, member : discord.Member):
		await self.client.say('{0.name} has been here since {0.joined_at}'.format(member))
		
		
def setup(client):
	client.add_cog(misc(client))
	
	
	
	
