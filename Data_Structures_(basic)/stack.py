class Stack:
	max = 5
	top = -1
	array = [None] * max

	def isEmpty(self):
		if(self.top == -1):
			print(True)
		else:
			print(False)

	def topOfStack(self):
		print('First data in stack is : ' + str(self.array[self.top]))

	def push(self, data):
		if (self.top == 4):
			print('Stack is full')
			return
		self.top+=1
		self.array[self.top] = data
		print(str(data) + ' was inserted')

	def pop(self):
		if (self.top == -1):
			print('Stack is empty')
		else:
			print(str(self.array[self.top]) + ' was deleted')
			self.array[self.top] = None	
			self.top-=1			

	def display(self):
		if (self.top == -1):
			print('Stack is empty')
		else:
			print('Stack is : ' + str(self.array) )