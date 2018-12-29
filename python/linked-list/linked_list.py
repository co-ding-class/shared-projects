class Node(object):
	def __init__(self, value, succeeding=None, previous=None):
		self.value = value
		self.next = succeeding
		self.back = previous

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.last = None

	def push(self, value):
		node = Node(value)
		node.back = self.last
		self.last.next = node 
		self.last = node
		
	def pop(self):
		self.last = self.last.back
		destruction = self.last.next
		self.last.next = None
		return destruction.value
	
	def shift(self):
		pass
		
	def unshift(self, value):
		node = Node(value)
		node.next = self.first
		if self.first:
			self.first.back = node
		else:
			self.last = node
		self.first = node
		
		
#self.last is the end, self.first is the front
"""***** NO SELF.TESS!!!!!!****"""