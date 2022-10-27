# -*- coding: utf-8 -*-
from os import system
from time import sleep

from Story import story

system('mode con: cols=100 lines=48')	# Set the output window to a proper size
system('color 0A')	# Makes the output green text on black background

defaultStats = ["score", "fear", "awareness", "fatigue", "intelligence", "thirst"]

def Join(inputList):
	outputList = []
	for element in inputList:
		outputList.append(str(element))
	return "".join(outputList)

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

def StatCheck(segment):
	if (segment[0] in ["!", "?"]):
		section = Split(segment, ["<", "<=", "=", ">=", ">", "+", "-"])
		type = False

		if (len(section) > 1):
			if ((segment[0] == "?" and section[1] in ["<", "<=", "=", ">=", ">"]) or (segment[0] == "!" and section[1] in ["+", "-", "="])):
				type = True
		else:
			section = [segment]

		return [section[0], type]
	else:
		# This should never happen
		return [False, False]


def Main():
	print("Check the story module...\n")

	defined = {
		"scenes":			[],
		"stats":			[],
		"inventory":	[],
		"switches":		[]
	}

	used = {
		"scenes":			[],
		"stats":			[],
		"inventory":	[],
		"switches":		[]
	}

	errors = {
		"undefined_object":		[],
		"empty_choice":				[],
		"stat_modifier":			[],
		"stat_checker":				[],
		"missing_scenes":			[],
		"unused_scenes":			[],
		"hyphen_scenes":			[],
		"missing_stats":			[],
		"unused_stats":				[],
		"nondefault_stats":		[],
		"missing_inventory":	[],
		"unused_inventory":		[],
		"missing_switches":		[],
		"unused_switches":		[],
		"text_goto":					[],
		"text_modifier":			[],
		"improper_option":		[],
		"unused_option":			[],
		"missing_option":			[],
		"nocheck_option":			[]		
	}

	hasTitle = "title" in story
	hasStart = "start" in story

	if (hasStart):
		used["scenes"].append(story["start"])

	for item in story:
		if (item not in ["title", "start"]):
			defined["scenes"].append(item)

	for scene in defined["scenes"]:
		if (type(story[scene]) != dict):
			errors["undefined_object"].append(scene)
			continue
		for elementNumber, element in enumerate(story[scene]["choice"]):
			if (len(element) == 1):
				errors["empty_choice"].append([scene, element[0]])
			else:
				for segmentNumber, segment in enumerate(element):
					if (segmentNumber > 0):
						# Skip the choice-text, focus on the actions
						segCheck = segment.lower()
						statCheck = StatCheck(segCheck)

						if (segCheck[0:2] == ">>"):
							# GoTo
							if (segCheck[2:] not in used["scenes"] and segCheck[2:] != "restart"):
								used["scenes"].append(segCheck[2:])
						elif (segCheck[0] == "!"):
							# Change
							if (statCheck[1]):
								if (segCheck[1] == "@"):
									# Switch
										if (statCheck[0][2:] not in defined["switches"]):
											defined["switches"].append(statCheck[0][2:])
								elif (segCheck[1] == "#"):
									# Inventory
									if (statCheck[0][2:] not in defined["inventory"]):
										defined["inventory"].append(statCheck[0][2:])
								else:
									# Stat
									if (statCheck[0][1:] not in defined["stats"]):
										defined["stats"].append(statCheck[0][1:])
							else:
								errors["stat_modifier"].append([scene, statCheck[0][1:]])
						elif (segCheck[0] == "?"):
							# Check
							if (statCheck[1]):
								if (segCheck[1] == "@"):
									# Switch
									if (statCheck[0][2:] not in used["switches"]):
										used["switches"].append(statCheck[0][2:])
								elif (segCheck[1] == "#"):
									# Inventory
									if (statCheck[0][2:] not in used["inventory"]):
										used["inventory"].append(statCheck[0][2:])
								else:
									# Stat
									if (statCheck[0][1:] not in used["stats"]):
										used["stats"].append(statCheck[0][1:])
							else:
								errors["stat_checker"].append([scene, statCheck[0][1:]])

		mainText = []
		mainOptions = []
		for elementNumber, element in enumerate(story[scene]["text"]):
			if (elementNumber == 0):
				mainText = Join(element)
				for place, symbol in enumerate(mainText):
					if (symbol == "%"):
						mainOptions.append(mainText[place:place+2])
			else:
				switches = 0
				for segmentNumber, segment in enumerate(element):
					if (segmentNumber > 0 and type(segment) == str):
#						print(segment)
						# Skip the main text, focus on the options
						segCheck = segment.lower()
						statCheck = StatCheck(segCheck)

						if (segCheck[0:2] == ">>"):
							# GoTo don't belong in text!
							errors["text_goto"].append([scene, segCheck[2:]])
						elif (segCheck[0] == "!"):
							# Change doesn't belong in text!
							errors["text_modifier"].append([scene, statCheck[0][1:]])
						elif (segCheck[0] == "%"):
							if (len(segCheck) != 2):
								errors["improper_option"].append([scene, segCheck])
							else:
								if (segCheck not in mainText):
									errors["unused_option"].append([scene, segCheck])
								else:
									if (segCheck in mainOptions):
										del mainOptions[mainOptions.index(segCheck)]
						elif (segCheck[0] == "?"):
							# Check
							switches += 1
							if (statCheck[1]):
								if (segCheck[1] == "@"):
									# Switch
									if (statCheck[0][2:] not in used["switches"]):
										used["switches"].append(statCheck[0][2:])
								elif (segCheck[1] == "#"):
									# Inventory
									if (statCheck[0][2:] not in used["inventory"]):
										used["inventory"].append(statCheck[0][2:])
								else:
									# Stat
									if (statCheck[0][1:] not in used["stats"]):
										used["stats"].append(statCheck[0][1:])
							else:
								errors["stat_checker"].append([scene, statCheck[0][1:]])
				if (switches == 0):
					errors["nocheck_option"].append([scene, segCheck])
		if (len(mainOptions) > 0):
			errors["missing_option"].append([scene, mainOptions])

	for scene in used["scenes"]:
		# Do all GoTo scenes exist?
		if (scene not in defined["scenes"]):
			errors["missing_scenes"].append(scene)

	for scene in defined["scenes"]:
		# Are all scenes in use?
		if (scene not in used["scenes"]):
			errors["unused_scenes"].append(scene)
		if ("-" in scene):
			errors["hyphen_scenes"].append(scene)

	for stat in used["stats"]:
		# Do all queried stats exist?
		if (stat not in defined["stats"]):
			errors["missing_stats"].append(stat)
		if (stat not in defaultStats):
			errors["nondefault_stats"].append(stat)

	for stat in defined["stats"]:
		# Are all stats queried?
		if (stat not in used["stats"] and stat != "score"):
			errors["unused_stats"].append(stat)
		if (stat not in defaultStats):
			errors["nondefault_stats"].append(stat)

	for inv in used["inventory"]:
		# Do all queried inventory exist?
		if (inv not in defined["inventory"]):
			errors["missing_inventory"].append(inv)

	for inv in defined["inventory"]:
		# Are all inventory queried?
		if (inv not in used["inventory"]):
			errors["unused_inventory"].append(inv)

	for switch in used["switches"]:
		# Do all queried switches exist?
		if (switch not in defined["switches"]):
			errors["missing_switches"].append(switch)

	for switch in defined["switches"]:
		# Are all switches queried?
		if (switch not in used["switches"]):
			errors["unused_switches"].append(switch)

	# This is where we run through the errors and output them
	errorDescriptions = {
		"undefined_object":		"Undefined object",
		"empty_choice":				"Choice has no function",
		"stat_modifier":			"Wrong or missing modifier for stat change",
		"stat_checker":				"Wrong or missing modifier for stat query",
		"missing_scenes":			"GoTo scene that doesn't exist",
		"unused_scenes":			"No choice ever goes to scene",
		"hyphen_scenes":			"Hyphen in scene name",
		"missing_stats":			"Stat queried, but never changed",
		"unused_stats":				"Stat changed, but never referenced",
		"nondefault_stats":		"Non-default stat",
		"missing_inventory":	"Inventory referenced, but never added",
		"unused_inventory":		"Inventory added, but never used",
		"missing_switches":		"Switch referenced, but never set",
		"unused_switches":		"Switch set, but never queried",
		"text_goto":					"GoTo doesn't belong in \"text\" segment",
		"text_modifier":			"Stat-changes don't belong in \"text\" segment",
		"improper_option":		"Optional text with improper number",
		"unused_option":			"Optional text with no place-holder",
		"missing_option":			"Optional text place-holder with no text to fill it",
		"nocheck_option":			"Optional text with no conditions set"
	}
	errorList = []
	if (not hasTitle):
		errorList.append("No story title")
	if (not hasStart):
		errorList.append("No start-scene pointer")

	for error in errors:
		if (len(errors[error]) > 0):
			errorMsg = errorDescriptions[error]
			for errorSet in errors[error]:
				if (type(errorSet) == str):
					errorList.append(errorMsg + " '" + errorSet + "'")
				elif (type(errorSet) == list):
					errorList.append(errorMsg + " '" + str(errorSet[1]) + "' in scene '" + errorSet[0] + "'")

	if len(errorList):
		for errorMsg in errorList:
			print(errorMsg)
	else:
		print("No errors found.")


Main()
