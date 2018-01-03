class Node:
	def __init__(self, data=None):
		self.data = data
		self.next=None

class SingleLinkedList:
	def __init__(self):
		self.head = Node()

	def append(self, data):
		newNode = Node(data)
		currentNode = self.head
		while(currentNode.next != None):
			currentNode = currentNode.next
		currentNode.next = newNode
		print(str(data) + ' was appended')

	def prepend(self, data):
		newNode = Node(data)
		newNode.next = self.head.next
		self.head.next = newNode
		print(str(data) + ' was prepended')

	def addByPosition(self, data, position):
		if(position > self.length()):
			print('Position out of range')
			return
		newNode =  Node(data)
		currentNode = self.head
		for i in range(position-1):
			currentNode = currentNode.next
		print(str(data) + ' was added to position ' +str(position))
		newNode.next = currentNode.next
		currentNode.next = newNode		

	def removeByPosition(self, position):
		if(position > self.length()):
			print('Position out of range')		
			return
		currentNode = self.head
		for i in range(position-1):
			currentNode = currentNode.next
		print(str(currentNode.next.data) + ' was removed was removed from position ' + str(position))
		currentNode.next = currentNode.next.next

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