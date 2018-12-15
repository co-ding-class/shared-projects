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
		node.back = self.last
		self.last.next = node 
		self.last = node
	def pop(self):
		pass
		
	def shift(self):
		pass
		
	def unshift(self, value):
		node = Node(value)
		node.next = self.tess
		self.tess.back = node 
		self.tess = node
		
		
		#self.last is the end, self.tess is the front