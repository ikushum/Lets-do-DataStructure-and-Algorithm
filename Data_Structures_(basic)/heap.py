# Priority Queue and Heaps are pretty similar. The only difference 
# here in this code is in the delete method. In heap, we pass the 
# index of element to be deleted instead of just deleting the element 
# at the base index.

class Heap:
	def __init__(self, size):
		self.array = [0] * size
		self.size=size
		self.maxIndex = -1

	def insert(self, data):
		if(self.maxIndex+1==self.size):
			print('Queue is full')
			return False
		else:
			print(str(data) + ' was inserted')
			self.maxIndex+=1			
			self.array[self.maxIndex]=data
			self.heapyfyUp()
			return True

	def popAtIndex(self, index):
		if(self.maxIndex==-1):
			print('Queue is empty')
			return False
		elif(index>self.maxIndex):
			print('Index out of range')
		else:
			print(str(self.array[index]) + ' was deleted')
			self.array[index] = self.array[self.maxIndex]
			self.array[self.maxIndex] = 0
			self.maxIndex-=1
			self.heapyfyDown(index)
			return True

	def heapyfyUp(self):
		index=self.maxIndex
		parentIndex = self.getParentIndex(index)
		while(self.hasParent(index) & (self.array[index] > self.array[parentIndex])):
			self.array[index], self.array[parentIndex] = self.array[parentIndex], self.array[index]
			index=parentIndex
			parentIndex =self.getParentIndex(index)
		return True

	def heapyfyDown(self, index):
		index=index
		while(self.hasLeftChild(index)):
			greaterChildIndex = self.getGreaterChildIndex(index)
			if(self.array[index] < self.array[greaterChildIndex]):
				self.array[index], self.array[greaterChildIndex] = self.array[greaterChildIndex], self.array[index]
			else:
				return True

	# Helper Methods			
	def getParentIndex(self, index): return ((index+1)//2)-1
	def getLeftChildIndex(self,index): return ((index+1)*2)-1
	def hasLeftChild(self, index): return True if self.size-1 >= self.getLeftChildIndex(index) else False
	def hasRightChild(self, index): return True if self.size-1 >= self.getLeftChildIndex(index)+1 else Falses
	def hasParent(self, index): return True if index > 0 else False
	def getGreaterChildIndex(self, index):
		greaterChildIndex = self.getLeftChildIndex(index)
		if(self.hasRightChild(index) & (self.array[greaterChildIndex] > self.array[greaterChildIndex+1])):
			return greaterChildIndex
		else:
			return greaterChildIndex+1