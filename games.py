######### GAMES #########
import discord
from discord.ext import commands
import asyncio
import aiohttp
from io import BytesIO
import random
import json


already_playing = []
		

class games:
	def __init__(self, client):
		self.client = client
			
######### ROCK-PAPER-SCISSORS #########		
	def winner(self, m1, m2, p1, p2):
			
		if m1 == m2:
			return "\nWelp! Thats a Tie."
		elif m1 == "Rock":
			if m2 == "Paper":
				return "\n%s covers %s" % (p2, p1)
			else:
				return "\n%s smashes %s" % (p1, p2)
		elif m1 == "Paper":
			if m2 == "Scissors":
				return "\n%s cuts %s" % (p2, p1)
			else:
				return "\n%s covers %s" %(p1, p2)
		elif m1 == "Scissors":
			if m2 == "Rock":
				return "\n%s smashes %s" % (p2, p1)
			else:
				return "\n%s cuts %s" % (p1, p2)
		elif m1 == "Lizard":
			if m2 == "Spock":
				return "\n%s gets destroyed by %s" % (p2, p1)
			else:
				return "\n%s has now a new hole, thank %s for such kindess" % (p1, p2) 
		elif m1 == "Spock":
			if m2 == "Lizard":
				return "\n%s humiliates %s" % (p2, p1)
			else:
				return "\n%s death was a complete plot twist prepared by %s" % (p2, p1)
		else:
			print("That's not a valid play. Check your spelling!")
			



	async def winz(self, p1, p2):
		bad = "Ehem, check your spelling.\nWrite one of the following words to use: `Rock`, `Paper`, `Scissors`."
		msg = "Write one of the following words to use: `Rock`, `Paper`, `Scissors`."
		good = "Your answer has been registered."
		valid = False
		await self.client.send_message(p1, msg)
		while(valid == False):
			print("inside while")
			m = await self.client.wait_for_message(author=p1, timeout=60)
			if m == None:
				return m
			while m!= None and str(m.channel)[:14]!="Direct Message":
				m = await self.client.wait_for_message(author=p1, timeout=60)
				if m == None:
					return m
			if (m.content == "Paper" or m.content == "Scissors" or m.content == "Rock" or m.content == "Lizard" or m.content == "Spock"):
				valid = True
				await self.client.send_message(p1, good)
			else:
				await self.client.send_message(p1, bad)
		return m

	@commands.command(pass_context=True)
	async def rps(self, ctx, user : discord.Member):
		global already_playing
		#playing against the bot
		if (user.id == "520667105499152385"): 
			suker = ctx.message.author
			
			movs = ['Rock', 'Paper', 'Scissors']
			msg2 = "So... you know how this goes: write `Rock`, `Paper`, `Scissors`."
			
			await self.client.say("I am super bad at this. Please have mersi :sob: ")
			await self.client.say(msg2)
			
			m = await self.client.wait_for_message(author=suker, timeout=60)
			if m == None:
				await self.client.say("I am sad you gave up, %s" % (suker))
			if m.content == "Rock":
				await self.client.say("\n>%s uses Rock\n>Chain uses Paper\n" % (suker))
				await self.client.say("`Chain wins`\nYaaay! I did it!")
			elif m.content == "Paper":
				await self.client.say("\n>%s uses Paper\n>Chain uses Scissors\n" % (suker))
				await self.client.say("`Chain wins`\nWhat?! I did it...? Yess!")
			elif m.content == "Scissors":
				await self.client.say("\n>%s uses Scissors\n>Chain uses Rock\n" % (suker))
				await self.client.say("`Chain wins`\nOh, I won? Something in my code must be wrong...")
			elif m.content == "Spock":
				await self.client.say("\n>%s uses Spock\n>Chain uses Lizard\n" % (suker))
				await self.client.say("`Chain wins`\nThat was almost cheating from your part, luckily I did not fall for that.")
			elif m.content == "Lizard":
				await self.client.say("\n>%s uses Lizard\n>Chain uses %s\n" % (suker, random.choice(movs)))
				await self.client.say("`Chain wins`\nBut I like Lizards. They are super cute!")
			else:
				await self.client.say("\n>%s uses '%s'\n>Chain uses Indifference\n" % (suker, m.content))
				await self.client.say("%s was heavily hurt after being ignored by Chain.")
			
			
			#she will play with you, dont worry.
		
		#caller against himself, maybe if you have split personality it could work...
		elif (ctx.message.author.id == user.id): 
			await self.client.say("Awww, you don't have any friends to play rps...? C'on, play with me instead!")
		#Two players against each other.
		else: 
			intro = "You have challenged %s to a duel of rock-paper-scissors" % (user)
			msg = "Write one of the following words to use: `Rock`, `Paper`, `Scissors`."
			bad = "Ehem, check your spelling.\nWrite one of the following words to use: `Rock`, `Paper`, `Scissors`."
			good = "Your answer has been registered."
			toolate1 = "You didn't pick in time. Run the cmd again if you want to give it another shot."
			toolate2 = "Your opponent chickened out and didn't pick. Run the cmd again if you want to give it another shot."
			boring = "You both dropped the game!"
			givup1 = "%s didn't make a selection" % (ctx.message.author)
			givup2 = "%s didn't make a selection" % (user)
			givup3 = "%s and %s chickned out from rock-paper-scissors. Lame!" % (ctx.message.author, user)
			
			player1 = ctx.message.author
			print(player1) #4 testing
			player2 = user
			print(player2) #4 testing 2
			
			found1 = True
			if player1.id in already_playing:
				await self.client.say("Shuttit, you are already playing with somebody else. Finish that game first!")
				return
			else:
				fount1 = False
			
			found2 = True
			if player2.id in already_playing:
				await self.client.say("Looks like your opponent is already playing a game. Wait for them to finish.")	
				return
			else:
				fount2 = False
		
			already_playing.append(player1.id) 
			already_playing.append(player2.id)	
		
			await self.client.say(intro)	
			
			task1 = asyncio.ensure_future(self.winz(player1, player2))
			task2 = asyncio.ensure_future(self.winz(player2, player1))
			
			
			m1 = await task1
			m2 = await task2
			
			if m2 == None and m1 == None:
				await self.client.send_message(player1, boring)
				await self.client.send_message(player2, boring)
				await self.client.say(givup3)
				already_playing.remove(player1.id) 
				already_playing.remove(player2.id) 
			
				return
			elif m1 == None:
				await self.client.send_message(player1, toolate1)
				await self.client.send_message(player2, toolate2)
				await self.client.say(givup1)
				already_playing.remove(player1.id) 
				already_playing.remove(player2.id) 
			
				return
			elif m2 == None:
				await self.client.send_message(player2, toolate1)
				await self.client.send_message(player1, toolate2)
				await self.client.say(givup2)
				already_playing.remove(player1.id) 
				already_playing.remove(player2.id) 
			
				return
			
			await self.client.say("\n>%s uses %s\n>%s uses %s\n" % (player1, m1.content, player2, m2.content ))
		
			win = self.winner(m1.content, m2.content, player1, player2)
			await self.client.say(win)
			
			already_playing.remove(player1.id) 
			already_playing.remove(player2.id) 
			
			
def setup(client):
	client.add_cog(games(client))
	
