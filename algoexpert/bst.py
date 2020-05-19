class Node:
	def __init__(self, v):
		self.v = v
		self.left = None
		self.right = None
	
	def insert(self, v):
		if v < self.v:
			if self.left:
				return self.left.insert(v)
			else:
				self.left = Node(v)
				return
		else: # input value is larger
			if self.right:
				return self.right.insert(v)
			else:
				self.right = Node(v)
				return

	def search(self, v):
		if v < self.v:
			if self.left:
				return self.left.search(v)
			else:
				return False
		else:
			if self.right:
				return self.right.search(v)
			else:
				return False

	def remove(self, v):
		if v < self.v:
			if self.left:
				self.left.remove(v)
			else:
				return None
		elif v > self.v:
			if self.right:
				self.right.remove(v)
			else:
				return None
		
		if self.left is None and self.right is None: # is a left Node
			self.v = None
		elif self.left is None: # only a right child
			curr = self.v
			self.v = self.right.v
			return curr
		elif self.right is None:
			curr = self.v
			self.v = self.left.v
			return curr
		else:
			while self.right:
				curr = self.right
			self.v = curr.v
			self.right = self.right.delete(curr.value)
		return self

class BST:
	def __init__(self):
		self.root = None

	def insert(self, v):
		if self.root:
			return self.root.insert(v)
		self.root = Node(v)
		return
	
	def search(self, v):
		if self.root:
			return self.root.search(v)
		return False

	def remove(self, v):
		# 6 scenarios
		# a. no root
		# b. no child
		# c. child
			# -> only left child
			# -> only right child
				# -> two children
		if self.root:
			self.root.remove(v)