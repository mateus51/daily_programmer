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

def scrabble(rack, word):
	rack = list(rack)

	for letter in word:
		if letter in rack:
			rack.remove(letter)
			print(letter)
		else:
			return False
	return True

scrabble("mateos", "mateus")	