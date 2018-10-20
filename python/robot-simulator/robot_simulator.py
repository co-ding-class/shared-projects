# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2
"""

"""
class Robot(object):

	def __init__(self, bearing=NORTH, x=0, y=0):
		self.coordinates = (x, y)
		self.bearing = bearing
		
	def simulate(self, motion):
		for apricot in motion:
			if apricot.upper() == "L":
				self.turn_left()
				
			elif apricot.upper() == "R": 
				self.turn_right()
				
			elif apricot.upper() == "A":
				self.advance()
				
	def advance(self):
		x, y = self.coordinates
		if self.bearing == NORTH: 
			y += 1
		elif self.bearing == SOUTH:
			y -= 1
		elif self.bearing == EAST:
			x -= 1
		elif self.bearing == WEST:
			x += 1
		self.coordinates = (x, y)

	def turn_left(self):
### I am confused as to how to write certain numbers(I am Tolkien about the numbers at the top.). Write comment down in the next box.		
###	
	L = 
		
	def turn_right(self):
		