class Node(object):
	def __init__(self, value, succeeding=None, previous=None):
		self.value = value
		self.next = succeeding
		self.back = previous

class LinkedList(object):
	def __init__(self):
		self.tess = None
		self.last = None

	def push(self, value):
		node = Node(value)
		
		self.last = node 
		
		
		
		#self.last is the end, self.tess is the front