# In this sort of normal Queue, we can insert elements until queue becomes full. But once queue becomes full, we can not insert the next element even if there is a space in front of queue. 

class Queue:
	def __init__(self,size):
		#max = 5
		self.size = size
		self.head = -1
		self.tail = -1
		self.array = [None] * size

	def isEmpty(self):
		if (self.head == -1 & self.tail == -1):
			return True
		else:
			return False

	def peek(self):
		if self.head >= 0:
			print('First data in queue is : ' + str(self.array[self.head]))
			return self.array[self.head]
		else:
			print("no element in queue")
			return None

	def add(self, data):
		if not (self.tail < self.size-1):
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
			
		else:
			print(str(self.array[self.head]) + ' was deleted')
			self.array[self.head] = None	
			self.head+=1			
			if (self.head == self.tail ):
				self.head=self.tail= -1
			

	def display(self):
		if (self.head == -1 & self.tail == -1):
			print('Queue is empty')
		else:
			print('Queue is : ' + str(self.array) )