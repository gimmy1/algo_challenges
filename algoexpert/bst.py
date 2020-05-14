class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
	def insert(self, value):
		if value < self.value:
			if not self.left:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if not self.right:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self

	def contains(self, value):
		if value < self.value:
			if not self.left:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if not self.right:
				return False
			else:
				return self.right.contains(value)
		else:
			return True
	
	def remove(self, value, parent=None):
		if value < self.value:
			if self.left:
				self.left.remove(value, self)
		if value > self.value:
			if self.right:
				self.right.remove(value, self)
		else: # you found the cookie
			if self.left and self.right:
				self.value = self.right.get_min_value()
				self.right.remove(self.value, self)
			elif parent is None:
				if self.left:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else: # single node tree and pass
					pass
			elif parent.left == self:
				parent.left = self.left if self.left else self.right
			elif parent.right == self:
				parent.right = self.left if self.left else self.right
		return self
				
	def get_min_value(self):
		if not self.left:
			return self.value
		else:
			return self.left.get_min_value()
		
if __name__ == "__main__":
    print(BST(4).insert(5).value)