class Stack:

	def __init__(self,size):
		self.size = size
		self.top = -1
		self.array = [None] * self.size

	def isEmpty(self):
		if(self.top == -1):
			return True
		else:
			return False

	def top(self):
		return self.array[self.top]

	def push(self, data):
		if not (self.top < self.size-1):
			print('Stack is full')
			return
		self.top+=1
		self.array[self.top] = data
		print(str(data) + ' was inserted')

	def pop(self):
		if (self.top == -1):
			print('Stack is empty')
			return None
		else:
			print(str(self.array[self.top]) + ' was deleted')
			obj = self.array[self.top]
			self.array[self.top] = None	
			self.top-=1			
			return obj

	def display(self):
		if (self.top == -1):
			print('Stack is empty')
		else:
			print('Stack is : ' + str(self.array) )

