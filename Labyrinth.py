import random
import math

Menu = True
gameStart = False
instructionStart = False
aboutStart = False
""" This is the "about" page; essentially a credits page """
def About():
	leaveAbout = False
	while leaveAbout == False:
		print('u uglee')
		leaveAbout = input('type anything to leave lmao :')
		if leaveAbout == 'yes':
			leaveAbout = True

""" This function asks for the player's class."""

def charClass(selection):
	character = "nothing"
	while selection == "nothing":
		if selection == 'knight':
			print('The knight has great defense and average attack. They lack critical chance and dodge, but are very versatile because they can switch swords during battle.')
			confirmation1 = input('Would you like to select this class?')
			if confirmation1 == "yes":
				Zone = 1
				character = 'knight'
				break
			else:
				selection = "nothing"
		
		elif selection == 'assassin':
			print('The assassin has high potential for dps and has a great amount of dodge, but requires a lot of luck and mana management. Their special abilites are poisons.')
			confirmation2 = input('Would you like to select this class?')
			if confirmation2 == "yes":
				Zone = 1
				character = 'assassin'
				break
			else:
				selection = "nothing"
			
		elif selection == 'brawler':
			print('The brawler specializes in martial arts, they are the jack-of-all-trades and are cost efficent since they can fight without weapons.')
			confirmation1 = input('Would you like to select this class?')
			if confirmation1 == "yes":
				Zone = 1
				character = "brawler"
				break
			else:
				selection = "nothing"
	
		elif selection == 'mage':
			print('The mage has good burst damage and utility but lack defensive capabilities and requires mana management. Their special abilites are a set of high damage abilities.')
			confirmation1 = input('Would you like to select this class?')
			if confirmation1 == "yes":
				Zone = 1
				character = 'mage'
				break
			else:
				selection = "nothing"
			
		elif selection == 'necromancer':
			print('The necromancer has low dps an burst but have great defensive capabilites. They rely on minions for main damage and ues health as a resource.')
			confirmation1 = input('Would you like to select this class?')
			if confirmation1 == "yes":
				Zone = 1
				character = "necromancer"
				break
			else:
				selection = "nothing"
		
		else:
			print('That is not an avaliable class')
			selection = "nothing"

def Game():
	zone = 0
	health = 0
	mana = 0
	dodge = 0
	armor = 0
	crit = 0
	gold = 500
	selection = 'nothing'
	selection = input('Select your character's role [Knight, Assassin, Brawler, Mage, Necromancer]: ')
	while selection == 'nothing':
		charClass(selection)
		print(selection)
	

while Menu == True:
	print('This is the endless Labyrinth')
	print('Type \"start\" to start the game')
	print('Type \"instructions\" if this is your first time playing')
	print('Type in \"about\" to learn about the development of the game')
	interfaceInput = input(":")
	if interfaceInput == 'start':
		gameStart = True
		Menu = False
	elif interfaceInput == 'instructions':
		instructionStart = True
	elif interfaceInput == 'about':
		aboutStart = True
	else:
		print('Not a valid response.')
		continue
	
	if gameStart == True:
		Game()
	elif instructionStart == True:
		Instructions()
	elif aboutStart == True:
		About()
