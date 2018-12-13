######### LOVE AND FRIENSHIP! #########
'''Sorry for this name, but i didnt know how to call it so i went random word generator,
 love appeared, one thing led to another and here we are now.'''	
import discord
from discord.ext import commands
import random
import json


		
class love:
	def __init__(self, client):
		self.client = client
	
	

	######### SHIP #########
	def pairStrenght(self, luf1, luf2):
		Aww1 = luf1.id
		Aww2 = luf2.id
		destiny = Aww1 + Aww2
		fate = hash(destiny)
		return (fate%10)
	
	def lovez(self, p1, p2, love):
		
			
		if (love != 0):
			if (love > 10):
				if (love > 20):
					if (love > 30):
						if (love > 40):		
							if (love > 50):
								if (love > 60):
									if (love > 70):
										if (love > 80):
											if (love > 90):
												if (love > 99):
													if (love == 100):
														lmao = "I can see your ship would be 100/100. That is a 1/100 chance so you both really are lucky. As a compensation, lemme teach you what is love: Love encompasses a variety of strong and positive emotional and mental states, ranging from the most sublime virtue or good habit, the deepest interpersonal affection and to the simplest pleasure. An example of this range of meanings is that the love of a mother differs from the love of a spouse, which differs from the love of food. Most commonly, love refers to a feeling of strong attraction and emotional attachment. Love can also be a virtue representing human kindness, compassion, and affection, as 'the unselfish loyal and benevolent concern for the good of another'."
														return lmao
													else:
														return "Your love is inmensurable"
												else:
													return "`>%s love` \n Wow, thats a super duper hight score... Uhhh, I dont have anything prepared for this situations... Not yet till I learn the `pls marry` command anyway." % (love)
											else: 
												return "`>%s love`\n Most of the people reading this would feel frustrated and jealous. Too bad for the cuse the love %s and %s share is unbreakable" % (love, p1, p2)
										else:
											return "`>%s love`\n As %s would say: 'Roses are red, Tulips are black. %s'd look great with a knife in their back.'" % (love, p2, p1)	
									else:
										return  "`>%s love` \n Thats a beautiful number, but more beautiful is %s, you should forget about %s and come with me :kissing_smiling_eyes:  " % (love, p2, p1)						
								else:
									return "`>%s love` \nAight, if this was a 'love exam', you would have passed, too bad it aint, so lemme do this: \n `>49.99 love` \n %s tell %s to stop crying." % (love, p1, p2)
							else:
								return "`>%s love` \nHeeey, that was close to 50! Maybe we can work something out, you two would look so cute together." % (love)
						else:
							return "`>%s love` \n Some things should never be together, be it pizza and pinneaple, be it a priest and a child, be it %s and %s." % (love, p1, p2)
					else:
						return "`>%s love` \n I just asked %s wife's what they thought bout %s... you better watch your back at night." % (love, p1, p2)
				else:
					return "`>%s love` \n This is the story of how %s and %s died alone. Sad." % (love, p1, p2)
			else:
				return "`>%s love`\n Thats super low and super sad, %s will watch %s as they leave with another, even better, person." % (love, p1, p2)
		else:
			return "`>%s love` \n Both %s and %s are really effed." % (love, p1, p2)
	
	@commands.command(pass_context=True)
	async def ranship(self, ctx, user1 : str, user2 : str):
		if (user1 == user2):
			await self.client.say("That is just same as masturbating... Sad.")
		else:
			love = random.randint(0, 100)
			msg = self.lovez(user1, user2, love)
			await self.client.say(msg)
			
	@commands.command(pass_context=True)
	async def ship(self, ctx, user1 : discord.Member, user2 : discord.Member):
		if (user1 == user2):
			await self.client.say("That is just same as masturbating... Sad.")
		else:
			love = self.pairStrenght(user1, user2)
			msg = self.lovez(user1, user2, love)
			await self.client.say(msg)
			
	
	
def setup(client):
	client.add_cog(love(client))
	
	