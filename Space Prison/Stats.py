# -*- coding: utf-8 -*-
#Stats

def clear():
	global statObject
	# This object will contain all the initialized player stats
	statObject = {
		"score": 0, # Score will always be there. Any other stats will be initialized from
								# the Main module.
	}

def display(justify = 0, inventory = False, switches = False):
	# Display stats in a pretty box.
	keys = list(statObject) # Get a List with the keys from the stats Dict.
	just = "".ljust(justify, " ") # Create a string to space between left edge.

	if (switches):
		# This first part is to list the "switches", i.e. the ones with @ in them.
		print(just + "──" + " Switches ".ljust(12, "─") + "───")
		nothing = True
		for key in sorted(keys):
			if ("@" in key and statObject[key] > 0):
				# If "#" is in the key, it's an inventory item.
				nothing = False
				print(just + " " + key.replace("_", "-").replace("#", "").ljust(11))
		if (nothing):
				print(just + " " + "-none-")

	elif (inventory):
		# This first part is to list the "inventory" items, i.e. the ones with # in them.
		print(just + "──" + " Inventory ".ljust(12, "─") + "───")
		nothing = True
		for key in sorted(keys):
			if ("#" in key and statObject[key] > 0):
				# If "#" is in the key, it's an inventory item.
				nothing = False
				print(just + " " + key.replace("_", "-").replace("#", "").title().ljust(11))
		if (nothing):
				print(just + " " + "-empty-")

	else:
		# Otherwise, regular stats, so show them in the box. Fancy graphix
		print(just + "╓──" + " Stats ".ljust(14, "─") + "───┐")
		print(just + "║ " + "SCORE".title().ljust(13) + str(statObject["score"]).rjust(4) + " │")
		# Score first, 'cos we keep that separated from the rest.
		print(just + "╟".ljust(20, "─") + "┤")
		for key in sorted(keys):
			if (key.lower() != "score" and "#" not in key and "@" not in key):
				# Print it if it's a stat.
				# I.e. if it doesn't have "#" or "@" in it.
				print(just + "║ " + key.replace("_", "-").title().ljust(13) + str(statObject[key]).rjust(4) + " │")
		print(just + "╙".ljust(20, "─") + "┘")


def listOut():
	"Returns the statObject"
	# So we can save it in a save-game.
	return statObject

def set(stat, value = 0):
	"Create a stat if it doesn't exist, and set a stat to a specific value"
	global statObject
	if (str(value).isdigit() == False or stat == ""):
		# If value is not a number, or stat-name is empty, then do nothing.
		return False
	# Create stat if necessary, set value of stat
	statObject[stat.lower()] = value
	if (("#" in stat or "@" in stat) and value == 0 and stat.lower() in statObject):
		# If inventory(#) or switch(@) exists, but is set to 0, then just
		# remove it altogether (to save memory and savegame size).
		del statObject[stat.lower()]
		# Return True
		return True
	# Return value of stat
	return statObject[stat.lower()]

def inc(stat, amount = 1):
	"Increase stat"
	# Add "amount" to stat..
	global statObject
	if (stat.lower() in statObject and (type(amount) == int or str(amount).isdigit())):
		# If the stat exists, and the amount is a number, go ahead increase it
		statObject[stat.lower()] += int(amount)
		if (statObject[stat.lower()] > 255):
			# But stats can't be higher than 255
			statObject[stat.lower()] = 255
		return statObject[stat.lower()]
	else:
		# If not, then whoops!
		return False

def dec(stat, amount = 1):
	"Decrease stat"
	global statObject
	# Subtract "amount" from stat..
	if (stat.lower() in statObject and (type(amount) == int or str(amount).isdigit())):
		# If the stat exists, and the amount is a number, go ahead decrease it
		statObject[stat.lower()] -= int(amount)
		if (statObject[stat.lower()] < 0):
			# But stats can't be lower than 0.
			statObject[stat.lower()] = 0
		return statObject[stat.lower()]
	else:
		# If not, then whoops!
		return False

def check(stat):
	"Returns value of stat"
	if (stat in statObject):
		return statObject[stat]
	else:
		return False

clear()
print("'Stats' Loaded")
