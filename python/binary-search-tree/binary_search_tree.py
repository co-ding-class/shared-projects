class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data): # ['4']
        self.root = None
        for leaf in (tree_data):
            pass

    def data(self):
        return 

    def sorted_data(self):
        pass
		
	def inorder(self, root, left, right):
	    if root == None: return
		
		
		
		
