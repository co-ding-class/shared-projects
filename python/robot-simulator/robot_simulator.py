# Globals for the bearings
# Change the values as you see fit
EAST = None
NORTH = None
WEST = None
SOUTH = None


class Robot(object):

	def __init__(self, bearing=NORTH, x=0, y=0):
		coordinates = (x, y)
		self.bearing = bearing
	def advance(self):
		pass

	def simulate(self, direction):
		pass