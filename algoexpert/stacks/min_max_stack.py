class MinMaxStack:
	def __init__(self):
		self.mmstack = []
		self.stack = []
    
	def peek(self):
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        self.mmstack.pop()
		return self.stack.pop()

    def push(self, number):
        # Write your code here.
        newmm = {"min": number, "max": number}
		if len(self.mmstack):
			lastmin_max = self.mmstack[-1]
			newmm["min"] = min(lastmin_max["min"], number)
			newmm["max"] = max(lastmin_max["max"], number)
		self.mmstack.append(newmm)
		self.stack.append(number)

    def getMin(self):
        # Write your code here.
        return self.mmstack[-1]["min"]
    
	def getMax(self):
        # Write your code here.
		return self.mmstack[-1]["max"]
