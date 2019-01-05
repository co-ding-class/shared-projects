class Node(object):
	def __init__(self, value, succeeding=None, previous=None):
		self.value = value
		self.next = succeeding
		self.back = previous

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.last = None
		self.total = 0

	def push(self, value):
		node = Node(value)
		if self.last != None:
			node.back = self.last
			self.last.next = node 
			self.last = node
		else:
			self.last = self.first = node

	def __len__(self):
		return self.total

	def pop(self):
		destruction = self.last
		self.last = self.last.back
		if self.last != None:
			self.last.next = None
		return destruction.value
	
	def shift(self):
		destruction = self.first
		self.first = self.first.next
		if self.first != None:
			self.first.back = None
		return destruction.value
		
	def unshift(self, value):
		node = Node(value)
		node.next = self.first
		if self.first:
			self.first.back = node
		else:
			self.last = node
		self.first = node
		#have each separate moevment say whether to take away or add from the self.total
		
		
#self.last is the end, self.first is the front
"""***** NO SELF.men!!!!!!****"""