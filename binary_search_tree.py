"""
Binary Search Tree 
"""
class Node():
	def __init__(self, data=None):
	    self.data = data
	    self.left = None
	    self.right = None


class BST():
	def __init__(self):

		self.root = None

	def insert(self, data):

		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(data, self.root)

	def _insert(self, data, curr_node):

		if data < curr_node.data:
			if curr_node.left is None:
				curr_node.left = Node(data)
			else:
				self._insert(data, curr_node.left)

		elif data > curr_node.data:
			if curr_node.right is None:
				curr_node.right = Node(data)
			else:
				self._insert(data, curr_node.right)
		else:
			print(f"Element {data} is already present in Tree.")

	def print_tree(self, traversal_mode):
		if self.root == None:
			print ("Empty Tree.")
			return

		if traversal_mode == 'preorder':
			curr_node = self.root
			traversal = ""
			traversal = str(self._print_tree(curr_node, traversal)) 
		print(traversal)

	def _print_tree(self, curr_node, traversal, marker="ROOT"):
		#traversal += " * "
		if curr_node:
			
			traversal += str(curr_node.data) + str(marker) 
			
			traversal += " --> "
			traversal = self._print_tree(curr_node.left, traversal, "L")

			#traversal += " <-- "
			traversal = self._print_tree(curr_node.right, traversal, "R")
			#traversal += " --> "

		#traversal += " $ "
		return traversal

tree = BST()
tree.insert(5)
tree.insert(7)
tree.insert(11)
tree.insert(2)
tree.insert(9)
tree.insert(1)
tree.insert(10)
tree.insert(4)
tree.insert(3)
tree.insert(0)

tree.print_tree("preorder")









