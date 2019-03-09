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

		for leaf in (tree_data):
	
	
	def add(self):
		inserted = False
		while not inserted:
			if cur_node.left:
				
			else:

		el
				
	def data(self):
		return 

	def sorted_data(self):
		pass
		
	def inorder(self, root, left, right):
		if root == None: return
		
		def recursive_function(root):
			if root.left == None and root.right == None: return
			recursive_function(root.left)
			# TODO: process the data
			recursive_function(root.right)
