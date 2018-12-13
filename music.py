######### MUSIC PLAYER, IN PROGRESS #########
import discord
from discord.ext import commands
import youtube_dl
import json

players = {}
queues = {}

class music:
	def __init__(self, client):
		self.client = client

	def check_queue(self, id):
		if queues[id] != []:
			player = queues[id].pop(0)
			players[id] = player
			player.start()

	@commands.command(pass_context=True)
	async def join(self, ctx):
		channel = ctx.message.author.voice.voice_channel
		await self.client.join_voice_channel(channel)
		#needs to fix bug where if called when user is not in a voice channel, the bot will go to the hospital

	@commands.command(pass_context=True)
	async def leave(self, ctx):
		server = ctx.message.server
		voice_client = self.client.voice_client_in(server) #if no voice channel exists in the server, this will make the bot crash
		await voice_client.disconnect()
		#still needs some work done
		
	@commands.command(pass_context=True)
	async def play(self, ctx, url):
		server = ctx.message.server
		voice_client = self.client.voice_client_in(server)
		player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
		players[server.id] = player
		player.start()
		
	@commands.command(pass_context=True)
	async def pause(self, ctx):
		server_id = ctx.message.server.id
		players[server_id].pause()

	@commands.command(pass_context=True)
	async def stop(self, ctx):
		server_id = ctx.message.server.id
		players[server_id].stop()
		
	@commands.command(pass_context=True)
	async def resume(self, ctx):
		server_id = ctx.message.server.id
		players[server_id].resume()
		
	@commands.command(pass_context=True)
	async def skip(self, ctx):
		server_id = ctx.message.server.id
		players[server_id].stop()
	#if you are reading this, u r a nerd.
	@commands.command(pass_context=True)
	async def queue(self, ctx, url):
		server = ctx.message.server
		voice_client = self.client.voice_client_in(server)
		#it assumes bot is already in a voice channel, if not, boom it goes ripperino
		player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
		
		if server.id in queues:
			queues[server.id].append(player)
		else:
			queues[server.id] = [player]
		await self.client.say("Gottit, I added the song!")

def setup(client):
	client.add_cog(music(client))
	