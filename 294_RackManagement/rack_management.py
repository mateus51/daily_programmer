'''
#294 - Rack Management 1
Given a set of 7 letter tiles and a word, determine whether you
can make the given word using the given tiles.

Bonus 1 - Handle blank tiles (represented by "?"). 
These are "wild card" tiles that can stand in for any single letter.

Bonus 2 - Given a set of up to 20 letter tiles, 
determine the longest word from the enable1 English
word list that can be formed using the tiles.
'''
import csv

def scrabble(rack, word):
	print("scrabble({0}, {1})".format(rack, word))
	rack = list(rack)

	points_dict = get_punctuation_dict()
	points = 0

	# Let's go through every single letter in the word
	for letter in word:
		if letter in rack:	# If the current letter is in our rack, remove it
			points += int(points_dict[letter])
			rack.remove(letter)
		else:
			if "?" in rack:	# A wildcard can be used to match any letter
				rack.remove("?")
			else:
				print(" -> false (0 points)")
				return False # If there's a letter in the word that's not on the rack
	print(" -> true ({0} points)".format(points))
	return True   # if we were able to remove all the right letters from the rack

def get_punctuation_dict():
	points_dict = {}
	file = open('points.csv', 'r')

	try:
		reader = csv.reader(file)
		for row in reader:
			points_dict[row[0]] = row[1]
	finally:
		file.close()

	return points_dict


get_punctuation_dict()
scrabble("mateos", "mateus")	
scrabble("seutam", "mateus")
scrabble("udud", "dudu")
scrabble("mariaeduarda", "dudu")
scrabble("d?du", "dudu")
scrabble("????", "dudu")
scrabble("jaquelin?rrrr", "jaqueline")