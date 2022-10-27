# -*- coding: utf-8 -*-
def ByteShift(text, up = True):
	# Really shitty "encryption".. *cough-cough*
	direction = -1
	if (up):
		direction = 1
	code = ""
	for a, d in enumerate(text):
		c = ord(d)
		if (a % 2 == 0):
			# Every other digit has 1 either added to or subtracted from it
			code += chr(c + direction)
		else:
			code += chr(c - direction)
	return code

class Checksum:
	def __init__(self):
		# Not a good use of a class; I just wanted functions that were interrelated
		"init"

	def generate(data):
		"Returns the average byte value of a string, rounded down to integer"
		sum = 0
		for symbol in data:
			sum += ord(symbol)
		sum = int(sum / len(data))
		return sum

	def verify(data, checksum):
		return (Checksum.generate(data) == checksum)

# First byte of every data-chunk is the ID Header;
# The first three bits is the actual ID:
# 100	-	Scene
# 101	-	Stat
# 110	-	Inventory item
# 111 - Scene switch
# Next 5 bits is the length of the data, followed by so many bytes of the actual data.
# Last two bytes is the value, and a checksum.
# Checksum is calculated as the byte value of the data, averaged to the number of bytes.

def Encode(dataType, data, value = 0):
	# There's no real reason to encode anything in a project like this, but I like doing it.
	if (value > 255):
		# A stat can't be higher than 255, I've decided
		return False
	chunk = ""
	saveValue = ""

	if (dataType == "hdr"):
		# If it's the header, just encode it with the length and a checksum
		chunk = chr(len(data)) + ByteShift(data) + chr(Checksum.generate(data))

	if (dataType == "scn"):
		# 100	-	Scene
		# If it's a scene, encode it and add a byte header to it
		if (len(data) > 30):
			print("scene name too long")
			return False
		chunk = chr(len(data) + 0b10000000) + ByteShift(data) + chr(Checksum.generate(data))

	if (dataType == "stat"):
		# If it's a stat, encode it and add a byte header to it, as well as...
		if (len(data) > 30):
			print("stat name too long")
			return False
		if (data[0] == "#"):
			# 110	-	Inventory item
			# If it's an inventory item, encode the boolean value of the item into the
			# first character of the item name
			data = data[1:]
			statID = chr(len(data) + 0b11000000)
			data = chr(ord(data[0]) | (128 * value)) + data[1:]
		elif (data[0] == "@"):
			# 111 - Scene switch
			# Like inventory; encode the value into the first character
			data = data[1:]
			statID = chr(len(data) + 0b11100000)
			data = chr(ord(data[0]) | (128 * value)) + data[1:]
		else:
			# 101	-	Stat
			# If it's an actual stat, instead add the value as a separate byte after the name
			statID = chr(len(data) + 0b10100000)
			saveValue += chr(value)

		chunk = statID + ByteShift(data)
		if (saveValue != ""):
			chunk += saveValue
		chunk += chr(Checksum.generate(data))

	return bytes(chunk, 'utf-8')

def Decode(data):
	decoded = []
	symbolCount = 0
	chunkType = False
	chunk = ""
	for datum in data:
		for position, symbol in enumerate(datum.decode('utf-8')):
			chunk += symbol
			if (not chunkType):
				chunk = ""
				if (ord(symbol) >> 5 == 0b111):
					symbolCount = ord(symbol) - (0b111 << 5) + 2
					chunkType = "swt"
				elif (ord(symbol) >> 5 == 0b110):
					symbolCount = ord(symbol) - (0b110 << 5) + 2
					chunkType = "inv"
				elif (ord(symbol) >> 5 == 0b101):
					symbolCount = ord(symbol) - (0b101 << 5) + 3
					chunkType = "stat"
				elif (ord(symbol) >> 5 == 0b100):
					symbolCount = ord(symbol) - (0b100 << 5) + 2
					chunkType = "scn"
				elif (position == 0):
					symbolCount = ord(symbol) + 2
					chunkType = "hdr"
			symbolCount -= 1

			if (symbolCount == 0):
				stat = ""
				value = ""
				if (chunkType in ["stat"]):
					stat = ByteShift(chunk[0:-2], False)
					if (not Checksum.verify(stat, ord(chunk[-1]))):
						return False
					value = ord(chunk[-2:-1])
				else:
					stat = ByteShift(chunk[0:-1], False)
					if (not Checksum.verify(stat, ord(chunk[-1]))):
						return False
					if (chunkType in ["inv", "swt"]):
						chunkHdr = ["#", "@"][["inv", "swt"].index(chunkType)]
						first = ord(stat[0])
						value = first >> 7
						if (value == 1):
							stat = chr(first ^ 1 << 7) + stat[1:]
						stat = chunkHdr + stat
				if (value == ""):
					decoded.append(stat)
				else:
					decoded.append([stat, value])
				chunkType = False
	return decoded

print("'Chunkify' Loaded")