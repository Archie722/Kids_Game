Hello	
def weapon_response (weapon_answer):
	if "sword" in weapon_answer:
		return  "Ah the mighty sword, good choice."

	elif "wand" in weapon_answer:
		return  "Ah we have a wizard do we?"

	elif "axe" in weapon_answer:
		return "The Axe, good for chopping down trees, and maybe some heads!"

	elif "bat" in weapon_answer:
		return "Bat, good choice"

	elif "knife" in weapon_answer:
		return "Be carfull, its sharp!"

	elif "spoon" in weapon_answer:
		return "How did I know you would choose this? Always thinking with your stomach!"

	elif "bow" in weapon_answer:
		return "Well, we are Archers afterall"

	elif "gun" in weapon_answer:
		return "Be careful, you only have 1 bullet!"

	elif "lipstick" in weapon_answer:
		return "Why would you need lipstick, we are going on an adventure!"

	elif "flamethrower" in weapon_answer:
		return "Carefull you dont set yourself on fire!"

	else:
		return "Sorry, thats not in the list, so you cant have it."



print """"First you need to pick 6 out of the 10 weapons in the list:
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
