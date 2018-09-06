
import random
import time
import sys

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
	print "you enter the room and see a big monster"
	print "Do you want to fight or run away?"
	print "fight - 1"
	print "Run away - 2"
	answer = raw_input("> ")
	if answer == "1":
		print "\nI knew you were a fighter, now choose a weapon from your list %s\n" % weapon_list
		chosen_weapon = raw_input ("> ")
		if chosen_weapon == "sword":
			print "\nAh, the sword good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon == "wand":
			print "\nAh, the wand good choice, now you need to roll an even number to cas a magic spell"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon == "knife":
			print "\nAh, the knife good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon == "axe":
			print "\nAh, the axe good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"

		elif chosen_weapon == "spoon":
			print "\nAh, the spoon, hungry at a time like this???"
			print "your dead"
			dead()

		elif chosen_weapon == "gun":
			print "\nAh, the gun good choice, but you only have one bullet!"
			print "You need an even number to shoot him!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon == "lipstick":
			print "\nAh, the lipstick, not the best weopon against a monster"
			dead()

		elif chosen_weapon == "bat":
			print "\nAh, the bat good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon == "bow":
			print "\nAh, the bow good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

		elif chosen_weapon == "flamethrower":
			print "\nAh, the flamethrower good choice, now you need to roll an even number to win"
			print "Otherwise you will die!\n"
			raw_input("Press ENTER to roll \n ")

			print "Rolling\n"
			delay_print("....dont be scared........\n\n")

			room1_sword = random.randint(1,6)
			print " You got a : %d \n " % room1_sword
			if room1_sword % 2 == 0:
				print "You Win!!!"
			else:
				print " You lose!!"
				dead()

	elif answer == "2":
		print "You have run away!! Try again and dont be such a scardie cat!"
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

raw_input("Press ENTER to roll \n ")

print "Rolling\n"
delay_print("............\n\n")

dice = 1 #random.randint(1,6)
print " You got a : %d \n " % dice

if dice == 1:
	print "So it looks like your heading into room1"
	room_1()
elif dice == 2:
	print "So it looks like your heading into room 2"
elif dice == 3:
	print "So it looks like your heading into room 3"
elif dice == 4:
	print "So it looks like your heading into room 4"
elif dice == 5:
	print "So it looks like your heading into room 5"
else:
	print "So it looks like your heading into room 6"
