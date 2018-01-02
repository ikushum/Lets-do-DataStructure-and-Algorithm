# In this sort of circular Queue, we can insert any number of elements until queue becomes full regardless of empty spaces in the front of the queue

class CircularQueue:
	def __init__(self,size):
		self.size = size
		self.head = -1
		self.tail = -1
		self.array = [None] * size

	def isEmpty(self):
		if (self.head == -1 & self.tail == -1):
			print(True)
		else:
			print(False)

	def peek(self):
		if (self.head == -1 & self.tail == -1):
			print('Queue is empty')
			return None
		else:
			print('First data in queue is : ' + str(self.array[self.head]))
			return self.array[self.head]


	def add(self, data):
		if ((self.tail+1) % self.size == self.head):
			print('Queue is full')
			return
		if (self.head == -1 & self.tail == -1):
			self.head = 0
		self.tail = (self.tail+1)%self.size
		self.array[self.tail] = data
		print(str(data) + ' was inserted')

	def remove(self):
		if (self.head == -1 & self.tail == -1):
			print('Queue is empty')
		elif (self.head == self.tail ):
			self.head=self.tail= -1	
		else:
			print(str(self.array[self.head]) + ' was deleted')
			self.array[self.head] = None	
			self.head = (self.head+1)%self.size

	def display(self):
		if (self.head == -1 & self.tail == -1):
			print('Queue is empty')
		else:
			print('Queue is : ' + str(self.array))


