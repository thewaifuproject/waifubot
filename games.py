######### GAMES #########
import discord
from discord.ext import commands
import numpy as np
import asyncio
import aiohttp
from io import BytesIO
import random
import json

#If a user is in a game, he will be put in here. No double gamin' allowed in this christian code
already_playing = []

#STD Columns and Rows for CONNECT4
ROW_COUNT = 6
COLUMN_COUNT = 7

#Moves/symbol for p1 and p2
# ♣ ♦ ♥
#:o: :x:
p1_m = ":o:"
p2_m = ":x:"
		

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
				await self.client.say("%s was heavily hurt after being ignored by Chain." % (sucker))
			#she will play with you, and win, dont worry.
		
		#this is caller against himself, maybe if you have split personality it could work...
		elif (ctx.message.author.id == user.id): 
			await self.client.say("Awww, you don't have any friends to play rps...? C'on, play with me instead!")
		#this is two players against each other.
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
				await self.client.say("Shuttit, you are already playing. Finish that other game first!")
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
			

	
	###CONNECT 4###
	'''This is important: if you are reading this, never (and when I say never, I mean NEVER) play against Shower, he is good, he is too good at c4 4 u.'''

	@staticmethod
	def create_board():
		board = np.zeros((ROW_COUNT, COLUMN_COUNT)) #uses numpy
		return board
	
	#def print_board(board):
	#	print(np.flip(board, 0))
	

	async def print_board(self, p1, p2, board, e0, e1, e2, turn):
	
		
		msg="**%s** vs. **%s** \n" % (p1, p2)
		temp=np.flip(board, 0)
		for i in range(ROW_COUNT):
			for j in range(COLUMN_COUNT):
				if temp[i][j] == 0:
					msg += e0
				if temp[i][j] == 1:
					msg += e1
				if temp[i][j] == 2:
					msg += e2
					
			msg+="\n"
		msg+="**%s** symbol's: %s. \n **%s** symbol's: %s \n" % (p1, e1, p2, e2)
		msg+="*%s* has to pick a column! \n (type `1`-`2`-`3`-`4`-`5`-`6`-`7`)" % (p1 if turn%2==0 else p2)
		await self.client.say(msg)
		
		
	async def print_winning_board(self, p1, p2, board, e0, e1, e2, turn):
		msg="**%s** vs. **%s** \n" % (p1, p2)
		temp=np.flip(board, 0)
		for i in range(ROW_COUNT):
			for j in range(COLUMN_COUNT):
				if temp[i][j] == 0:
					msg += e0
				if temp[i][j] == 1:
					msg += e1
				if temp[i][j] == 2:
					msg += e2
			msg+="\n"
		await self.client.say(msg)
		
		
	
	async def confirmation(self, p1, p2):
		await self.client.say("**%s** has challenged **%s** to play a game of *CONNECT 4*.\n**%s** do you accept the invitation? `y/n`" % (p1, p2, p2))
			
		m = await self.client.wait_for_message(author=p2, timeout=30)
                
                if m == None:
			await self.client.say("Timed out.")
			return False
		if m.content == 'y':
			await self.client.say("**STARTING GAME**")
			return True
		elif m.content == 'n':
			await self.client.say("**GAME CANCELED**")
			return False
		else:
			await self.client.say("I asked for a `y/n`... run again the command if you want to play.")
			return False
			
	@staticmethod
	def drop_piece(board, row, col, piece):
		board[row][col] = piece
	
	#def is_valid_location(board, col):
	#	return board[ROW_COUNT-1][col] == 0
	
	@staticmethod
	def get_next_open_row(board, col):
		for r in range(ROW_COUNT):
			if board[r][col] == 0:
				return r
	@staticmethod		
	def winning_move(board, piece):
		#Checkin' horizontal locations 
		for c in range(COLUMN_COUNT-3):
			for r in range(ROW_COUNT):
				if (board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece):
					return True
		
		#Checkin' vertical locations
		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT-3):
				if (board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece):
					return True
					
		#Checki' effin diagolas part1 (down to up)
		for c in range(COLUMN_COUNT-3):
			for r in range(ROW_COUNT-3):
				if (board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece):
					return True
		
		#Checki' effin diagolas part2 (up to down)
		for c in range(COLUMN_COUNT-3):
			for r in range(3, ROW_COUNT):
				if (board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece):
					return True

	async def valid_move(self, player, channel, board):
		bad = "Ehem, writting a number from `0 to 6` is not that difficult... \nChoose a column \n (type `1`-`2`-`3`-`4`-`5`-`6`-`7`)"
		good = "**%s** has made their move." % player
		invalid = "That is not a valid move.\n **%s** has to pick a column! \n(type `1`-`2`-`3`-`4`-`5`-`6`-`7`)" % player
		valid = False
		
		while(valid == False):
			print("Checking valid move.")
			m = await self.client.wait_for_message(author=player, timeout=30)
			if m == None:
				return (m, valid)
			while m!= None and m.channel != channel:
				m = await self.client.wait_for_message(author=player, timeout=30)
				if m == None:
					return (m, valid)
			if (m.content == "1" or m.content == "2" or m.content == "3" or m.content == "4" or m.content == "5" or m.content == "6" or m.content == "7"):
				if board[ROW_COUNT-1][int(m.content)-1] == 0:
					valid = True
				else:
					await self.client.send_message(channel, invalid)	
			else:
				await self.client.send_message(channel, bad)
				
		return (int(m.content)-1, valid)
		
	async def valid_player(self, player1, player2):
		if player1.id in already_playing:
			await self.client.say("Shuttit, you are already playing. Finish that other game first!")
			return False
		
		if player2.id in already_playing:
			await self.client.say("Looks like your opponent is already playing a game. Wait for them to finish.")	
			return False
		else:
			already_playing.append(player1.id) 
			already_playing.append(player2.id)		
			return True
		
	def getEmojis(self, p1, p2):
		emotes0 = [":stop_button:", ":record_button:", ":arrows_counterclockwise:", ":white_circle:", ":large_blue_circle:", ":red_circle:", ":white_circle:", ":black_circle:", ":black_medium_square:", ":white_medium_square:", ":negative_squared_cross_mark:"]
		emotes1 = [":grinning:", ":sweat_smile:", ":innocent::heart_eyes:", ":yum:", ":smile:", ":rofl:", ":upside_down:", ":kissing_heart:", ":laughing:", ":stuck_out_tongue_closed_eyes:", ":blush:", ":kissing_smiling_eyes:", ":pensive:", ":persevere:", ":smirk:", ":confused:", ":sob:", ":flushed:", ":cold_sweat:", ":imp:", ":japanese_ogre:", ":japanese_goblin:", ":clown:", ":dog:", ":fox:", ":lion_face:", ":monkey_face:", ":chicken:", ":tropical_fish:", ":blowfish:", ":dragon_face:", ":dragon:", ":waning_gibbous_moon:", ":apple:", ":pear:", ":tangerine:", ":lemon:", ":melon:", ":grapes:", ":grapes:", ":watermelon:", ":8ball:", ":volleyball:", ":tennis:", ":red_car:", ":taxi:", ":blue_car:", ":police_car:"]
		emotes2 = [":kissing_closed_eyes:", ":smiley:", ":joy:", ":slight_smile:", ":stuck_out_tongue:", ":grin:", ":relaxed:️", ":wink:", ":kissing:", ":relieved:", ":stuck_out_tongue_winking_eye:", ":cry:", ":scream:", ":worried:", ":confounded:", ":sob:", ":fearful:", ":unamused:", ":disappointed_relieved:", ":slight_frown:", ":poop:", ":smiley_cat:", ":smile_cat:", ":joy_cat:", ":crying_cat_face:", ":hatched_chick:", ":cat:", ":bear:", ":cow:", ":see_no_evil:", ":penguin:", ":mouse:",":panda_face:", ":crescent_moon:", ":earth_americas:", ":earth_africa:", ":green_apple:", ":banana:", ":cherries:", ":peach:", ":pineapple:", ":soccer:️", ":basketball:", ":football:", ":baseball:️", ":no_entry:️", ":x:", ":o:️", ":name_badge:", ":children_crossing:", ":ok:", ":up:", ":cool:", ":new:", ":free:"]
			
		e0 = random.choice(emotes0)
		
		if (p1.id == "352209747824476170"):
			e1 = ":shower:"
		elif (p1.id == "479246167910252565"):
			e1 = ":kitamismirk:"
		else:
			e1 = random.choice(emotes1)
		
		if (p2.id == "352209747824476170"):
			e2 = ":shower:"
		elif (p1.id == "479246167910252565"):
			e2 = ":kitamismirk:"
		elif (p2.id == "424221454490402816"):
			e2 = ":chains: "
		else:
			e2 = random.choice(emotes2)
		
		return e0, e1, e2
		
	
	
	@commands.command(pass_context=True)
	async def c4(self, ctx, user : discord.Member):
	
		global ROW_COUNT 
		global COLUMN_COUNT
		global already_playing
		
		player1 = ctx.message.author
		player2 = user
		channel = ctx.message.channel
		
		#playing against the bot
		if (player2.id == "520667105499152385"): 
			if (player1.id == "352209747824476170"): #showy is dangerous in c4, out of 1k games, he has lost only 3, and I suspect he felt pity for his opponnent. 
				await self.client.say("No way I am playing against you Showey. \n :shower:")
			else:			
				await self.client.say("Sorry but no thanks. I don't like connect 4, I am more of a Tic-Tac-Toe fan.")

		#p1 vs p1, yeah, I know, this is retarded.
		elif (ctx.message.author.id == user.id): 
		
			await self.client.say("Are you sure about this? `y/n`")
			
			m = await self.client.wait_for_message(author=player1, timeout=20)
			
			if m.content == 'y':
				await self.client.say("**%s** played against himself and won! What ei surprise, what a plot twist, no one saw this comming! \n(I am currently learning to use my sarcasm module, I am doing good, right?)" % (player1))
			elif m.content == 'n':
				await self.client.say("Thought so.")
			else:
				await self.client.say("Too bad.")
	
		#This is the real stuffo
		if True:
			if await self.valid_player(player1, player2) == False:
				return
			else:
				
				(p_0_e, p_1_e, p_2_e) = self.getEmojis(player1, player2)
				
				if await self.confirmation(player1, player2):
					game_over = False
					turn = 0				
					board = self.create_board()
					await self.print_board(player1, player2, board, p_0_e, p_1_e, p_2_e, turn)
					
					
					while not game_over:
					
						if turn == 0:
							(col, valid) = await self.valid_move(player1, channel, board)
							if valid != True:
								await self.client.say("**%s** did not make a selection in time" % (player1))
								already_playing.remove(player1.id) 
								already_playing.remove(player2.id)
								return
							else:
								if True:
									row = self.get_next_open_row(board, col)
									self.drop_piece(board, row, col, 1)
									
									if self.winning_move(board, 1):
										await self.print_winning_board(player1, player2, board, p_0_e, p_1_e, p_2_e, turn)
										await self.client.say("**%s** HAS WON!" % (player1))
										print("Player1 wins")
										game_over = True
										already_playing.remove(player1.id) 
										already_playing.remove(player2.id)
										return						
						else:
							(col, valid) = await self.valid_move(player2, channel, board)
							if valid != True:
								await self.client.say("**%s** did not make a selection in time" % (player2))
								already_playing.remove(player1.id) 
								already_playing.remove(player2.id)
								return
							else:
								if True:
									row = self.get_next_open_row(board, col)
									self.drop_piece(board, row, col, 2)
									
									if self.winning_move(board, 2):
										await self.print_winning_board(player1, player2, board, p_0_e, p_1_e, p_2_e, turn)
										await self.client.say("**%s** HAS WON!" % (player2))
										print("Player1 wins")
										game_over = True
										already_playing.remove(player1.id) 
										already_playing.remove(player2.id)
										return
										
						turn += 1
						turn = turn % 2 #This is true hackz
						
						await self.print_board(player1, player2, board, p_0_e, p_1_e, p_2_e, turn)
						
						
			
def setup(client):
	client.add_cog(games(client))
	
