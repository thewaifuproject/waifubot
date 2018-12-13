import discord 
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import aiohttp
from io import BytesIO
import random
import time
import youtube_dl
import json

TOKEN = "NTIwNjY3MTA1NDk5MTUyMzg1.DuxM0Q.1PV1C2p76s-Yd1k99-waHYtn5Ok" 

Client = discord.Client()
client = commands.Bot(command_prefix = "pls ")
client.remove_command("help") #deletes the preded. help cmd. Gonna do the new more cool one

extensions = ['misc', 'help', 'music', 'games', 'trivia', 'love']

@client.event
async def on_ready():
	print("Bot is Kawaii and Ready.")
	await client.change_presence(game=discord.Game(name="it Cool."))
	
#FOR TESTING PURPOSES#
@client.command(pass_context=True)
async def load(ctx, extension):
	if ctx.message.author.id  == '424221454490402816':
		try:
			client.load_extension(extension)
			print("Loaded %s." % (extension))
			await client.say("Loaded %s" % (extension))
		except Exception as error:
				print("%s cannot be loaded. [%s]" % (extension, error))
	else:
		return
	
@client.command(pass_context=True)
async def unload(ctx, extension):
	if ctx.message.author.id  == '424221454490402816':
		try:
			client.unload_extension(extension)
			print("Unloaded %s." % (extension))
			await client.say("No more **%s** for you." % (extension))
		except Exception as error:
				print("%s cannot be unloaded. [%s]" % (extension, error))
	else:
		return

if __name__ == "__main__":
	for extension in extensions:
		try:
			client.load_extension(extension)
			print("Loaded %s." % (extension))
		except Exception as error:
			print("%s cannot be loaded. [%s]" % (extension, error))

client.run(TOKEN)