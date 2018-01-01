class Queue:
	max = 5
	head = -1
	tail = -1
	array = [None] * max

	def isEmpty(self):
		if (self.head == -1 & self.tail == -1):
			print(True)
		else:
			print(False)

	def peek(self):
		print('First data in queue is : ' + str(self.array[self.head]))

	def add(self, data):
		if (self.tail == 4):
			print('Queue is full')
			return
		if (self.head == -1 & self.tail == -1):
			self.head = 0
		self.tail+=1
		self.array[self.tail] = data
		print(str(data) + ' was inserted')

	def remove(self):
		if (self.head == -1 & self.tail == -1):
			print('Queue is empty')
		elif (self.head == self.tail ):
			self.head=self.tail= -1	
		else:
			print(str(self.array[self.tail]) + ' was deleted')
			self.array[self.tail] = None	
			self.tail-=1				

	def display(self):
		if (self.head == -1 & self.tail == -1):
			print('Queue is empty')
		else:
			print('Queue is : ' + str(self.array) )