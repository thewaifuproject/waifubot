#########HELP STUFO#########
import discord
from discord.ext import commands
import json

class help:
	def __init__(self, client):
		self.client = client


	@commands.command(pass_context=True)
	async def help(self, ctx):
		author = ctx.message.author
		await self.client.send_message(author, "If you need help call 119, as the help here is still in development.")
		
	'''	
	This is spoiler of the help thing->
	@client.command(pass_context=True)
	async def info(ctx, user: discord.Member):
	#user : discord.User = None
	#await client.say("banned the user {}.".format(user.name))
		if info: discord.Member
		user: discord.message.author
		embed = discord.Embed(title= "{}'s info".format(user.name), color=0xEC23BF)
		embed.add_field(name= "Name", value=user.name, inline=True)
		embed.add_field(name= "ID", value=user.id, inline=True)
		embed.add_field(name="Status", value=user.status, inline=True)
		embed.add_field(name="Highest Role", value=user.top_role, inline=True)
		embed.add_field(name="Joined At", value=user.joined_at, inline=False)
		embed.add_field(name="Created At", value=user.created_at, inline=True)
		embed.set_thumbnail(url=user.avatar_url)
		await bot.say(embed=embed)'''

def setup(client):
	client.add_cog(help(client))
	