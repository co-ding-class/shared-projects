class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
       self.value = value
	   self.next = succeeding
	   self.back = previous

class LinkedList(object):
    def __init__(self):
        pass

	def push(self, value):
		self.value = value
		node = Node()