# -*- coding: utf-8 -*-
# Import modules
from os import system
import textwrap
from random import random
from time import sleep

import Stats
import GameFile
import Scene

currentScene = Scene.startScene()
pauseAtAll = True
gameSaved = True

def resetStats():
	# Clear the stats..
	Stats.clear()
	# ..and then create the ones we have for the game and set them to 0.
	Stats.set("fear", 0)
	Stats.set("awareness", 0)
	Stats.set("fatigue", 0)
	Stats.set("intelligence", 0)
	Stats.set("thirst", 0)

def DrawScene(pause = True):
	system('cls') # Clear the screen (doesn't work if run from IDLE)
	# Draw fancy graphix
	print (" ─────────╢ " + Scene.gameTitle() + " ├───────────")
	print ("    ╙" + "".rjust(len(Scene.gameTitle()) + 2, "─") + "┘")
	# Show stats
	Stats.display(65)
	print()
	# Load scene data from the Scene module
	sceneData = Scene.load(currentScene)

	if (not sceneData):
		# If nothing's there, then something odd happened
		return False

	for displayParagraph in sceneData[0]:
		# Parse through all the paragraphs of the loaded scene
		if (type(displayParagraph) is str and len(displayParagraph) > 0):
			# If it's a string, textwrap it to the desired width
			displayChapter = textwrap.wrap(displayParagraph[0].upper() + displayParagraph[1:], 80)
			for line in displayChapter:
				# Print each line of the paragraph
				# Always make sure first character is uppercase.
				print("   " + line)
			if (displayParagraph != ""):
				print()
		elif (pause and (type(displayParagraph) in [int, float]) and pauseAtAll):
			#	If it's not a string, but a number, pause for the desired time
			sleep(displayParagraph)
	print()

	if (pauseAtAll and pause):
		sleep(0.75)

	displayChoices = sceneData[1]
	choiceNumber = 0
	for choice in displayChoices:
		# Parse through and list all the choices of the loaded scene
		if (pauseAtAll):
			sleep(0.05)
		choiceNumber += 1
		print("     ·" + str(choiceNumber) + "·", choice[0][0].upper()+choice[0][1:], "\n")

	return displayChoices

def ChangeStats(statList):
	for stat in statList:
		# Parse through the stats to change
		statChange = Scene.Split(stat, ["+", "-", "="])
		# Split each change by operator
		if (statChange[1] == "+"):
			# + -> Add value to stat
			Stats.inc(statChange[0], int(statChange[2]))
		if (statChange[1] == "-"):
			# + -> Subtract value from stat
			Stats.dec(statChange[0], int(statChange[2]))
		if (statChange[1] == "="):
			# + -> Set stat to exact value
			Stats.set(statChange[0], int(statChange[2]))

def GameSaved():
	# Checks if a game is saved, before operations like Restart, Exit, or Load
	if (not gameSaved):
		# If game is not saved, ask player if they're sure about their operation
		playerAnswer = input("\nYou are leaving behind unsaved game progress.\nDo you really want to do that? ").lower()
		if (playerAnswer == "n" or playerAnswer == "no"):
			# They're not, so return to game
			return False
		else:
			# They are, so continue with operation
			return True
	else:
		# Game is saved, so we can safely continue with operation
		return True

def Main():
	"Where all things come together!"
	global currentScene
	global gameSaved
	global pauseAtAll

	system('mode con: cols=102 lines=48')	# Set the output window to a proper size
	system('color 0A')	# Makes the output green text on black background
	# system commands only work from real shell; they have no effect if run from IDLE.
	# (Also they don't appear to be Mac compatible. Sorry about that. :/)
	resetStats()

	availableChoices = DrawScene()

	while(availableChoices):
		print()
		doPause = False
		choiceMade = input("   Choose what to do (or type HELP for more options): ").lower().strip()
		if (choiceMade.isdigit()):
			# The player entered a number, so it must be a choice
			if (0 != int(choiceMade) <= len(availableChoices)):
				# If the choice is within the available ones...
				gameSaved = False
				if (availableChoices[int(choiceMade) - 1][1]):
					# Take the list of stat-changes (if any) and apply them
					ChangeStats(availableChoices[int(choiceMade) - 1][1])
				if (availableChoices[int(choiceMade) - 1][2]):
					# Then, if there's a GoTo in the choice, go to the new scene
					doPause = True
					if (availableChoices[int(choiceMade) - 1][2].lower() == "restart"):
						# If the GoTo is >>restart, which is a special GoTo that restarts the game.
						resetStats()
						gameSaved = True
						currentScene = Scene.startScene()
					else:
						currentScene = availableChoices[int(choiceMade) - 1][2]
				# Draw the new scene
				availableChoices = DrawScene(doPause)
			else:
				# If the choice was 0, or higher than the number available, fail.
				print("\tThat choice does not seem to be available. Try again.")
		else:
			if (choiceMade == "help"):
				# This just prints out the commands the game understands.
				print("\n\t ── INSTRUCTIONS ─Θ──")
				print("\n\t - In each scene, type the number to the left of the action you want to take (1, 2, 3, etc.)")
				print("\t - HELP: Show this.")
				print("\t - INVENTORY: Show what you are carrying.")
				print("\t - SAVE: Save your current game to disk.")
				print("\t - LOAD: Load a saved game.")
				print("\t - RELOAD: Load last saved game.")
				print("\t - PAUSE ON/OFF: Enable/disable pauses in text display.")
				print("\t - RESTART: Restart the game from the beginning.")
				print("\t - CREDITS: Who did this?")
				print("\t - QUIT: Exit the game.")
			elif (choiceMade == "credits"):
				# This just prints out the commands the game understands.
				whichCredit = int(random() * 10)
				print("\n\t ── CREDITS ─Θ──")
				print("\n\t\t Θ── SPACE PRISON ───")
				print("\t ─(Or '500 Ways To Die In Space')─")
				if (whichCredit < 5):
					print("\n\t This game was put together by:\n"),
					print("\t", "Sargis Nersisyan".center(32)),
				else:
					print("\n\t", "VOICE ARTIST:".ljust(18), "Sargis Nersisyan".rjust(18))
					print("\t", "BACKGROUNDS:".ljust(18), "Sargis Nersisyan".rjust(18))
					print("\t", "CATERING:".ljust(18), "Sargis Nersisyan".rjust(18))
					print("\t", "STORYBOARDS:".ljust(18), "Sargis Nersisyan".rjust(18))
					print("\t", "ANIMAL WRANGLER:".ljust(18), "Sargis Nersisyan".rjust(18))

			elif (choiceMade.replace(" ", "") == "pauseoff"):
				# Disables the pauses in the game, for faster display
				pauseAtAll = False
				print("\tText pauses disabled.")
			elif (choiceMade.replace(" ", "") == "pauseon"):
				# Enables the pauses in the game, for full effect
				pauseAtAll = True
				print("\tText pauses enabled.")
			elif (choiceMade == "load" or choiceMade == "reload"):
				if (GameSaved()):
					# Load game
					loadStatus = GameFile.Load(choiceMade == "reload")
					if (loadStatus):
						# If the load-game function returns something, then ...
						# First, reset game stats..
						resetStats()
						# Then, set the current scene to the scene in the loaded game..
						currentScene = loadStatus[0]
						for stat in loadStatus[1:]:
							# Then, look through each loaded stat, and apply it to the game..
							Stats.set(stat[0], stat[1])
						gameSaved = True
						# And finally, redraw the new, current game.
						availableChoices = DrawScene()
					else:
						print("Load game aborted.")
			elif (choiceMade == "save"):
				# Save game
				# Sending the current scene to the save-game function. No need to send stats,
				# it'll grab those itself.
				gameSaved = GameFile.Save(currentScene)
				if (gameSaved):
					print("Game saved succesfully.")
				else:
					print("Game not saved.")
			elif (choiceMade == "inv" or choiceMade == "inventory"):
				# Lists the player's inventory. Remember, these are "stats" that start with #.
				Stats.display(10, True)
			elif (choiceMade == "sw"):
				# This displays the switches. For debugging only.
				Stats.display(10, False, True)
			elif (choiceMade == "restart"):
				# Player chose to restart. So, reset stats, set the current
				# scene to the beginning, and go again...
				if (GameSaved()):
					resetStats()
					gameSaved = True
					currentScene = Scene.startScene()
					availableChoices = DrawScene()
			elif (choiceMade == "exit" or choiceMade == "quit"):
				# Quit the game. BUT WAIT!! Did the player save their game??
				if (GameSaved()):
					print("\nBuhbye!\n")
					break
			elif (choiceMade == ""):
				# Player didn't type anything, so just reset the screen.
				DrawScene(False)
			else:
				# The player entered something we don't understand.
				snarkyRemarks = ["I'm sorry, what?", "That doesn't make any sense..", "Care to try again?", "Fat fingers?", "You kiss your mother with that mouth?", "I'm sorry, I don't speak - uh - whatever that is.."]
				# We're picking one at random from the list above.
				print("\t", snarkyRemarks[int(random() * len(snarkyRemarks))])


Main()
