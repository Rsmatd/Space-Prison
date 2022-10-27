# -*- coding: utf-8 -*-

from Story import story
import Stats

def Split(inputString, delimiters = []):
	"Splits the query string into a 3-element list: [stat, operator, value]"
	# Sort the list of delimiters by the size of their strings
	delimiters.sort(key = lambda s: len(s))
	# Reset default variables
	finalDelimiter = ""
	outputList = []

	for delimiter in delimiters:
		# Loop through delimiters
		if (delimiter in inputString):
			# If the delimiter is found, split the string where it is, and insert the delimter in the
			# middle. BUT continue, in case a larger delimiter, which may contain the first one, is found.
			outputList = inputString.split(delimiter, 1)
			outputList.insert(1, delimiter)
	# Maybe I need to use tuples here in some way. Check that out.
	return outputList

def QualifyStat(statCheck):
	"Identifies the stat requirement and returns whether it is met (True) or not (False)."
	# First, split the statCheck by the comparators
	statCheck = Split(statCheck, ["<", "<=", "=", ">=", ">"])
	# Then, get the current value for the stat in question
	statLevel = Stats.check(statCheck[0])
	# Reset the status to default (False)
	statStatus = False

	if ("<" in statCheck[1]):
		# If the comparator is "<", assign the result of stat < check to statStatus
		# i.e. if stat less than check, statStatus = True
		# i.e. if stat NOT less than check, statStatus = False
		statStatus = (statLevel < int(statCheck[2]))
	if (">" in statCheck[1]):
		# If the comparator is ">", assign the result of stat > check to statStatus
		statStatus = (statLevel > int(statCheck[2]))
	if ("=" in statCheck[1] and not statStatus):
		# If the comparator is "=", and statStatus hasn't already proven True, 
		# assign the result of stat == check to statStatus
		statStatus = (statLevel == int(statCheck[2]))

	return statStatus

def gameTitle():
	return story["title"]

def startScene():
	return story["start"]

def load(sceneID):
	"Finds the desired scene and builds the relevant 'move' data from it."

	if (sceneID not in story):
		# If a scene is called that does not exist, report an error and exit.
		print("Whoops. \"" + sceneID + "\" not found. Call the game dev, 'cos that's not supposed to happen!")
		return False

	for dataType in ["text", "choice"]:
		if (dataType not in story[sceneID]):
			# If a scene is missing one of the required data types.
			print("Uh-oh. \"" + sceneID + "\" is missing the \"" + dataType + "\" data type. I can't work like this!")
			return False


	# Here we find the story for the scene
	textLines = len(story[sceneID]["text"]) # How many optional lines apply to this scene?
	displayText = story[sceneID]["text"][0].copy() # Main display text for the scene
	# Notice, because this is a serious caveat about Dicts (Objects), which you might as well
	# be aware off.
	# When you have a Dict (i.e. thing = {"blah": "bluh"}), and you want to COPY that dict,
	# you can't just go "anotherThing = thing".
	# I mean, you can. That will work. print(thing) and print(anotherThing) will both show
	# the data.
	# However, you haven't copied anything. You've just made a new reference to the same object.
	# Which means, if you CHANGE something in "anotherThing", then the change will also be
	# true for "thing". So, to make a new, UNIQUE copy of a Dict, you have to use .copy(),
	# like I've done above.
	for line in range (1, textLines): # Loop through all optional lines for the scene
		optionalText = story[sceneID]["text"][line][0] # First, grab the optional text itself
		optionalTruthTable = [] # Reset truth table
		placeID = 0 # Reset the position for the optional text
		for textOption in range (1, len(story[sceneID]["text"][line])):
			# Loop through each element of each optional line
			if (story[sceneID]["text"][line][textOption][0] == "%"):
				# Does the element start with "%"?
				# If True, then store the number as the placeID for the optional text
				placeID = int(story[sceneID]["text"][line][textOption][1])
			elif (story[sceneID]["text"][line][textOption][0] == "?"):
				# If not, does it start with "?"?
				# If True, then check if the condition is met, and store that result in the truth table
				optionalTruthTable.append(QualifyStat(story[sceneID]["text"][line][textOption][1:]))
			else:
				# If not, then we don't know what to do with the element.
				print("Unknown element \"" + story[sceneID]["text"][line][textOption] + "\"")
		# Once all elements for an optional line are processed, check the truth table
		for segment in range (0, len(displayText)):
			# For each line in the display text
			if (type(displayText[segment]) is str):
				# If it's a string (and not a "wait" number)
				if (optionalTruthTable.count(True) == len(optionalTruthTable) and len(optionalTruthTable) > 0):
					# If the table is not empty, and all values are True, then replace the %# placeholders
					# in the main display text with the optional text.
					displayText[segment] = displayText[segment].replace("%" + str(placeID), optionalText)
	for segment in range (0, len(displayText)):
		# Once all optional text(s) have been inserted, clean up any remaining placeholders
		if (type(displayText[segment]) is str):
			for placeID in range (0, 10):
				displayText[segment] = displayText[segment].replace("%" + str(placeID), "")

	# Here we find the choices available in the scene
	choiceAmount = len(story[sceneID]["choice"]) # How many choices are in the scene?
	displayChoices = [] # Reset choice list
	for choice in range (0, choiceAmount):
		# Loop through all choices to build a list for the game engine only containing the
		# choices that will be available (depending on stats)
		optionalTruthTable = [] # Reset truth table
		goTo = "" # Reset the variable for the sceneID to go to on choice
		performChanges = [] # Reset list of stat changes to perform on choice
		for choiceOption in range (1, len(story[sceneID]["choice"][choice])):
			# Loop through all choice elements
			if (story[sceneID]["choice"][choice][choiceOption][0] == "?"):
				# Does an element start with "?"?
				# If True, then add the result of the condition to the truth table
				optionalTruthTable.append(QualifyStat(story[sceneID]["choice"][choice][choiceOption][1:]))
			elif (story[sceneID]["choice"][choice][choiceOption][0] == "!"):
				# Does an element start with "!"?
				# If so, add the stat change to the list of changes for this choice
				performChanges.append(story[sceneID]["choice"][choice][choiceOption][1:])
			elif (story[sceneID]["choice"][choice][choiceOption][0:2] == ">>" and goTo == ""):
				# Does an element start with ">>"?
				# If so, put it into the goTo variable
				# If goTo already has somethine in it, don't change that
				# In other words, if more than one ">>" element is in one choice, only the
				# first one will be used.
				goTo = story[sceneID]["choice"][choice][choiceOption][2:]
		if (optionalTruthTable.count(True) == len(optionalTruthTable)):
			# If all conditions are met, or no conditions were made, add the choice to the list.
			displayChoices.append([story[sceneID]["choice"][choice][0], performChanges, goTo])

	return [displayText, displayChoices]

print("'Scene' Loaded")