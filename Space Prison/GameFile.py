# -*- coding: utf-8 -*-
from pathlib import Path
import textwrap

from Chunkify import Encode, Decode
import Scene
import Stats

saveGameFileExtension = "."
# Generate the savegame file extension. The initial letters of the game title, plus "sg"
# So, "Space Prison" will be ".spsg"
for initial in Scene.gameTitle().split():
	saveGameFileExtension += initial[0].lower()
saveGameFileExtension += "sg"
saveGameHeader = "Heyooo! This is a valid " + Scene.gameTitle() + " save game file!"

lastSaved = ""

def ListGames():
	dird = Path(".")
	games = []

	# Check the game folder for any saved games and return a list of them
	if (dird.is_dir()):
		for file in dird.glob("*" + saveGameFileExtension):
			games += [str(file).split(saveGameFileExtension)[0]]
	return games


def Load(reload = False):
	"Load game (no args)"

	availableGames = ListGames()
	chosenGame = ""

	if (len(availableGames) == 0):
		# No games to load, so the operation will abort.
		print("No saved games available, sorry.")
		return False

	if (not reload or lastSaved == ""):
		print("\tSaved games:\n")

		for gameNumber, game in enumerate(availableGames):
			# List out the available saved games
			# Limit to 3 games per line
			print("\t" + (str(gameNumber + 1) + ":  " + game).ljust(28), end="")
			if ((gameNumber + 1) % 3 == 0):
				# So for every 3, new-line
				print()
			availableGames[gameNumber] = game.lower()
			# Add the filenames to a list, for easy retrieval when chosen

		chosenGame = input("\n\tWhich game would you like to load? (leave empty if you don't want to load a game after all.)\n : ").strip()

		if (chosenGame == ""):
			# Player chose nothing, so just go back to the game
			return False

		if (chosenGame.isdigit() and int(chosenGame) > 0 and int(chosenGame) <= len(availableGames)):
			# If the player typed a number to load a game, find the filename in the list
			chosenGame = availableGames[int(chosenGame) - 1]
	elif (reload and lastSaved != ""):
		chosenGame = lastSaved
	else:
		# In case something is wrong, just abort.
		return False

	if (chosenGame.lower() in availableGames):
		# If the chosen filename is in the list of available games,
		# open it, and..
		file = open(chosenGame.lower() + saveGameFileExtension, "rb")
		# ..load the contents, and send them to the Decode function..
		contents = Decode(file.readlines())
		# ..and then close the file
		file.close()

		if (len(contents) > 0 and contents[0] == saveGameHeader):
			# If the loaded contents are valid, slice the header off and send it
			# back to the main
			contents = contents[1:]
			loadWasSuccessful = contents
		else:
			print("Sorry, this does not appear to be a valid save game.")
			loadWasSuccessful = False
	else:
		print("No such savegame.")
		loadWasSuccessful = False

	return loadWasSuccessful

def Save(currentScene):
	"Save game (map position, player inventory, active events, other information)"

	global lastSaved
	saveWasSuccessful = False
	overWrite = False

	while (not overWrite):
		fileName = input("Please name your save game (leave empty if you don't want to save after all.) : ").strip()[:12]

		if (fileName == ""):
			return False

		file = Path("./" + fileName + saveGameFileExtension)
		if (file.exists()):
			print("A saved game already exists with that name. Do you wish to overwrite it?")
			overWrite = input(" : ")

			if (str(overWrite).lower() in ["y", "yes", "yeah", "yea", "yup", "sure"]):
				overWrite = True
			elif (overWrite == ""):
				return False
			else:
				overWrite = False
		else:
			overWrite = True

	if (overWrite):
		lastSaved = fileName
		saveWasSuccessful = True
		file = open("./" + fileName + saveGameFileExtension, "wb")

		file.write(Encode("hdr", saveGameHeader))
		file.write(Encode("scn", currentScene))

		stats = Stats.listOut()
		for stat in stats:
			file.write(Encode("stat", stat, stats[stat]))
		file.close()

	return saveWasSuccessful

print("'GameFile' Loaded")