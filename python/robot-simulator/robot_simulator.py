# Globals for the bearings
# Change the values as you see fit
EAST = None
NORTH = None
WEST = None
SOUTH = None
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
		pass

	def turn_left(self):
		pass
		
	def turn_right(self):
		pass