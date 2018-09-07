
import random
import time
import sys
from sys import exit


def weapon_response (weapon_answer):
	""" handles the response when choosing a weapon """
	if "sword" in weapon_answer:
		return  "Ah the mighty sword, good choice %s." % name

	elif "wand" in weapon_answer:
		return  "Ah we have a wizard do you %s?" % name

	elif "axe" in weapon_answer:
		return "The Axe, good for chopping down trees, and maybe some heads!"

	elif "bat" in weapon_answer:
		return "Bat, good choice %s" % name

	elif "knife" in weapon_answer:
		return "Be carfull %s, its sharp!" % name

	elif "spoon" in weapon_answer:
		return "How did I know you would choose this %s? Always thinking with your stomach!" % name

	elif "bow" in weapon_answer:
		return "Well, you are %s Archer afterall" % name

	elif "gun" in weapon_answer:
		return "Be careful %s, you only have 1 bullet!" % name

	elif "lipstick" in weapon_answer:
		return "Why would you need lipstick %s, we are going on an adventure!" % name

	elif "flamethrower" in weapon_answer:
		return "Carefull you dont set yourself on fire!"

	else:
		return "Sorry, thats not in the list, so you cant have it."

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep (0.25)

def dead():
	print "Try again another time"

def room_1():
	print "you enter the room 1 and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an EVEN number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an even number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()
				break
			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an even number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()
				break
			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
					break
				else:
					print " You lose!!"
					dead()
					break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_1()

def room_2():
	print "you enter the room 2 and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_2()

def room_3():
	print "you enter the room 3 and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an EVEN number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an even number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an even number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_3()

def room_4():
	print "you enter the room 4 and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_4()

def room_5():
	print "you enter the room 5 and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an EVEN number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an even number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an even number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an even number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 0:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_5()

def room_6():
	print "you enter the room 6 and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_6()

def room_7():
    print "you enter the room and see a big monster sat by a door sleeping"
    print "point a stick at the monter - 1"
    print "Fight the monter - 2"
    print "Run away - 3"
    answer = raw_input("> ")
    while True:
		if answer == "1":
			print "You poke the stick at the monster and it moves away from the door"
			print "What do you want to do now?"
			print "Go through the door - 1"
			print "poke the monster again - 2"
			print "fight the monster - 3"
			question_answer = raw_input("> ")
			if question_answer == "1":
				print "well done you got out alive!"
			elif question_answer == "2":
				print "You made him angry this time and he eats you up!"
				dead()
			elif question_answer == "3":
				print "You ran away!"
				dead()
			else:
				print "test"
		elif answer == "2":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")
				print "Rolling\n"
				delay_print("....dont be scared........\n\n")
				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")
				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")
				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()
			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")
				print "Rolling\n"
				delay_print("....dont be scared........\n\n")
				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()
			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")
				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")
				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "3":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_7()

def room_8():
	print "you enter the room and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_8()

def room_9():
	print "you enter the room and see a princess held captive"
	print "Do you want to try and save her or run away?"
	print "Save her - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were brave, choose your weapon! %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_9()

def room_10():
	print "you enter the room and see a new iphone lying on the floor, you think it belongs to someone else."
	print "Do you take it or leave throught the door?"
	print "Take the Iphone - 1"
	print "Leave throught the door - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nIts wrong to steal! That was a test! %\n"
			dead()
			break
		elif answer == "2":
			print "Well done that was a test, you passed!\n"
			break
		else:
			print "Enter a valid number\n"
			room_10()

def room_11():
	print "you enter the room with lava all over the floor"
	print "There is a bridge to the left and a bridge to the right"
	print "Which one do you take?"
	print "Left - 1"
	print "Right - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nThe bridge on the left you say, you walk accross safley.\n"
			break
		elif answer == "2":
			print "Oh no! The bridge collapes and you fall in the lava!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_11()

def room_12():
	print "you enter the room and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	while True:
		if answer == "1":
			print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
			chosen_weapon = raw_input ("> ")
			if chosen_weapon in weapon_list and chosen_weapon == "sword":
				print "\nAh, the sword good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "wand":
				print "\nAh, the wand good choice, now you need to roll an ODD number to cas a magic spell"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "knife":
				print "\nAh, the knife good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "axe":
				print "\nAh, the axe good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"

			elif chosen_weapon in weapon_list and chosen_weapon == "spoon":
				print "\nAh, the spoon, hungry at a time like this???"
				print "your dead"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "gun":
				print "\nAh, the gun good choice, but you only have one bullet!"
				print "You need an ODD number to shoot him!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
				print "\nAh, the lipstick, not the best weopon against a monster"
				dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bat":
				print "\nAh, the bat good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "bow":
				print "\nAh, the bow good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()

			elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
				print "\nAh, the flamethrower good choice, now you need to roll an ODD number to win"
				print "Otherwise you will die!\n"
				raw_input("Press ENTER to roll \n ")

				print "Rolling\n"
				delay_print("....dont be scared........\n\n")

				room1_sword = random.randint(1,6)
				print " You got a : %d \n " % room1_sword
				if room1_sword % 2 == 1:
					print "You Win!!!"
					weapon_list.remove(chosen_weapon)
				else:
					print " You lose!!"
					dead()
			break
		elif answer == "2":
			print "You have run away!! Try again and dont be such a scardie cat!"
			dead()
			break
		else:
			print "Enter a valid number\n"
			room_12()

def level_1():
	raw_input("Press ENTER to roll \n ")

	print "Rolling\n"
	delay_print("............\n\n")

	dice = 1 #random.randint(1,6)
	print " You got a : %d \n " % dice

	if dice == 1:
		print "So it looks like your heading into room 1"
		room_1()
	elif dice == 2:
		print "So it looks like your heading into room 2"
		room_2()
	elif dice == 3:
		print "So it looks like your heading into room 3"
		room_3()
	elif dice == 4:
		print "So it looks like your heading into room 4"
		room_4()
	elif dice == 5:
		print "So it looks like your heading into room 5"
		room_5()
	else:
		print "So it looks like your heading into room 6"
		room_6()

def level_2():
	raw_input("Press ENTER to roll \n ")

	print "Rolling\n"
	delay_print("............\n\n")

	dice = random.randint(1,6)
	print " You got a : %d \n " % dice

	if dice == 1:
		print "So it looks like your heading into room 7"
		room_7()
	elif dice == 2:
		print "So it looks like your heading into room 8"
		room_8()
	elif dice == 3:
		print "So it looks like your heading into room 9"
		room_9()
	elif dice == 4:
		print "So it looks like your heading into room 10"
		room_10()
	elif dice == 5:
		print "So it looks like your heading into room 11"
		room_11()
	else:
		print "So it looks like your heading into room 12"
		room_12()

def level_3():
	print "You are almost there!"
	print "you enter the last room with the big bad inside"

def big_bad():
	print "you enter the room and see the big bad"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	if answer == "1":
		print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
		print "He looks to big to fight hand to hand!"
		print "choose your weapon wisley"
		chosen_weapon = raw_input ("> ")
		if chosen_weapon in weapon_list and chosen_weapon == "sword":
			print "\nAh, the sword - bad choice"
			dead()
		elif chosen_weapon in weapon_list and chosen_weapon == "wand":
			print "\nAh, the wand, magic wont work against him!"
			dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "knife":
			print "\nAh, the knife bad choice"
			dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "axe":
			print "\nAh, the axe bad choice"
			dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "gun":
			print "\nAh, the gun good choice, but you only have one bullet!"
			print "You need an even number to shoot him!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
				weapon_list.remove(chosen_weapon)
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "lipstick":
			print "\nAh, the lipstick, not the best weopon against a monster"
			dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "bat":
			print "\nAh, the bat bad choice"
			dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "bow":
			print "\nAh, the bow good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
				weapon_list.remove(chosen_weapon)
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon in weapon_list and chosen_weapon == "flamethrower":
			print "\nAh, the flamethrower good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
				weapon_list.remove(chosen_weapon)
			else:
				print " You lose!!"
				dead()

name = raw_input("welcome to the game, whats your name? \n ")

print "Why hello %s! \n" % name

print """First you need to pick 6 out of the 10 weapons in the list:
			1. Sword
			2. Wand
			3. Axe
			4. Bat
			5. Knife
			6. Spoon
			7. Bow
			8. Gun
			9. Lipstick
			10. Flamethrower
			"""
viable_weapon = ["sword", "wand", "axe", "bat", "knife", "spoon", "bow", "gun", "lipstick", "flamethrower"]

while True:
	print "Enter your first choice"
	weapon_1 = raw_input("> ")
	if weapon_1 in viable_weapon:
		print weapon_response(weapon_1)
		viable_weapon.remove(weapon_1)
		break
	else:
		print "Sorry not an option"

while True:
	print "Enter your second choice"
	weapon_2 = raw_input("> ")
	if weapon_2 in viable_weapon:
		print weapon_response(weapon_2)
		viable_weapon.remove(weapon_2)
		break
	else:
		print "Sorry not an option"

while True:
	print "Enter your third choice"
	weapon_3 = raw_input("> ")
	if weapon_3 in viable_weapon:
		print weapon_response(weapon_3)
		viable_weapon.remove(weapon_3)
		break
	else:
		print "Sorry not an option"

while True:
	print "Enter your fourth choice"
	weapon_4 = raw_input("> ")
	if weapon_4 in viable_weapon:
		print weapon_response(weapon_4)
		viable_weapon.remove(weapon_4)
		break
	else:
		print "Sorry not an option"

while True:
	print "Enter your fifth choice"
	weapon_5 = raw_input("> ")
	if weapon_5 in viable_weapon:
		print weapon_response(weapon_5)
		viable_weapon.remove(weapon_5)
		break
	else:
		print "Sorry not an option"

while True:
	print "Enter your sixth choice"
	weapon_6 = raw_input("> ")
	if weapon_6 in viable_weapon:
		print weapon_response(weapon_6)
		viable_weapon.remove(weapon_6)
		break
	else:
		print "Sorry not an option"


print """Well done, so you chose:
		 %s
		 %s
		 %s
		 %s
		 %s
		 %s

		 """ % (weapon_1, weapon_2, weapon_3, weapon_4, weapon_5, weapon_6)


weapon_list = [weapon_1, weapon_2, weapon_3, weapon_4, weapon_5, weapon_6]

print "Ok, now you need to role a dice to choose a door:\n"


level_1()

print "Welcome to level 2! Now you need to role a dice to choose a door:\n"

level_2()
level_3()
big_bad()
