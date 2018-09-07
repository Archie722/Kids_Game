import random
import time
import sys
from sys import exit
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep (0.25)
def dead():
	print "Try again another time"
	exit (0)



def test():
    print "you enter the room and see a big monster sat by a door sleeping"
    print "point a stick at the monter - 1"
    print "Fight the monter - 2"
    print "Run away - 3"
    answer = raw_input("> ")
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
            aw_input("Press ENTER to roll \n ")

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
    elif answer == "3":
    	print "You have run away!! Try again and dont be such a scardie cat!"
    	dead()
    else:
    	dead()
test()
