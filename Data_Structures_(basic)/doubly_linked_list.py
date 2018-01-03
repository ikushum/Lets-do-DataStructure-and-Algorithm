class Node:
	def __init__(self, data=None):
		self.data = data
		self.next=None
		self.prev=None

class DoubleLinkedList:
	def __init__(self):
		self.head = Node()

	def append(self, data):
		newNode = Node(data)
		currentNode = self.head
		while(currentNode.next != None):
			currentNode = currentNode.next
		currentNode.next = newNode
		newNode.prev = currentNode
		print(str(data) + ' was appended')

	def prepend(self, data):
		newNode = Node(data)
		newNode.prev = self.head
		newNode.next = self.head.next
		if(self.head.next!=None):
			newNode.next.prev = newNode
		self.head.next = newNode
		print(str(data) + ' was prepended')

	def addByPosition(self, data, position):
		if(position > self.length()):
			print('Position out of range')
			return
		newNode =  Node(data)
		currentNode = self.head
		for i in range(position):
			currentNode = currentNode.next
		print(str(data) + ' was added to position ' +str(position))
		newNode.next = currentNode
		newNode.prev = currentNode.prev
		currentNode.prev = newNode	
		newNode.prev.next = newNode	

	def removeByPosition(self, position):
		if(position > self.length()):
			print('Position out of range')		
			return
		currentNode = self.head
		for i in range(position):
			currentNode = currentNode.next
		print(str(currentNode.data) + ' was removed was removed from position ' + str(position))
		currentNode.prev.next = currentNode.next
		currentNode.next.prev = currentNode.prev 

	def length(self):
		length=0
		currentNode = self.head 		
		while not(currentNode.next == None):
			currentNode = currentNode.next
			length+=1
		return length			
		
	def display(self):
		if(self.head.next == None):
			print('List is empty')
			return []
		else:
			elements=[]
			print('The list is : ')
			currentNode = self.head 
			while not(currentNode.next == None):
				currentNode = currentNode.next
				elements.append(currentNode.data)
			print(elements)		

	def reverseDisplay(self):
		if(self.head.next == None):
			print('List is empty')
			return []
		else:
			currentNode = self.head 
			while not(currentNode.next == None):
				currentNode = currentNode.next
			elements=[]	
			while not(currentNode.prev == None):
				elements.append(currentNode.data)
				currentNode = currentNode.prev
			print('The list is : ')
			print(elements)		




