class TreeNode(object):
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		fmt = 'TreeNode(data={}, left={}, right={})'
		return fmt.format(self.data, self.left, self.right)

class BinarySearchTree(object):
	def __init__(self, tree_data):
		self.root = None
		for data in (tree_data):
			self.add(data)
	
	def add(self,data):
		if self.root is None:
			self.root = TreeNode(data,None, None)
			return 
		inserted = False
		cur_node = self.root
		
		while not inserted:
			if data <= cur_node.data:
				if cur_node.left:
					cur_node = cur_node.left
				else:
					cur_node.left = TreeNode(data, None, None)
					inserted = True
			elif data > cur_node.data:
				if cur_node.right:
					cur_node = cur_node.right
				else:
					cur_node.right = TreeNode(data, None, None)
					inserted = True

	def data(self):
		return self.root

	def sorted_data(self):
		elements = []
		self.inorder(self.root, elements)
		return elements
		
	def inorder(self, node, elements):
		if node is not None:
			self.inorder(node.left, elements)
			elements.append(node.data)
			self.inorder(node.right, elements)