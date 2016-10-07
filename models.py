import random

class Player:
	def __init__(self, _id, name):
		self.name = name
		self._id = _id
		self.score = 0


class Dice:
	def __init__(self, name, faces):
		self.name = name
		self.faces = faces
	def __repr__(self):
		return self.name
	def roll(self):
		return self.faces[random.randint(0,5)]
		# return self.faces[0]

class Cup:
	def __init__(self, name, dice):
		self.name = name
		self.dice = dice
	def shuffle(self):
		random.shuffle(self.dice)
	def shake(self):
		self.shuffle()
		return self.dice.pop()

