class Stack:
	def __init__(self):
		self.data = []

	def push(self, item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def top(self):
		return self.data[-1]

	def size(self):
		return len(self.data)

	def isEmpty(self):
		return self.size() == 0

	def __str__(self):
		return ", ".join([str(i) for i in self.data])
