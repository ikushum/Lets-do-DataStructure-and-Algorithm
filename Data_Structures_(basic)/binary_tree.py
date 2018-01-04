class Node:
	def __init__(self, data):
		self.data=data
		self.left_child=None
		self.right_child=None

	def insert(self, data):
		if(self.data == data):
			print(str(data) + ' already exists')
		elif(self.data > data):
			if(self.left_child):
				self.left_child.insert(data)
			else: 
				self.left_child = Node(data)
				print(str(data)+' was inserted')
		else:
			if(self.right_child):
				self.right_child.insert(data)
			else: 
				self.right_child = Node(data)
				print(str(data)+' was inserted')

	def find(self, data):
		if(data == self.data):
			print(str(data) + ' is present')
			return True
		elif(data < self.data):
			self.left_child.find(data) if self.left_child else print(str(data) + ' not found')
		elif(data > self.data) :
			self.right_child.find(data) if self.right_child else print(str(data) + ' not found')
		return False

	def delete():
		return

class Tree:
	def __init__(self):
		self.parent = None

	def insert(self, data):
		if(self.parent): 
			self.parent.insert(data)
		else:
			self.parent = Node(data)
			print(str(data) + ' was inserted')

	def find(self, data):
		if(self.parent):
			if(self.parent.find(data)==True):
				return True 
			elif(self.parent.find(data)==False):
				return False
		else:
			print(str(data) + ' not found') 
			return False

	def delete():
		return 

bst = Tree()
choice = 0
while(choice != 4):
	print("\n1) Press 1 to insert\n2) Press 2 to search\n3) Press 3 to Delete\n4) Press 4 to Quit")
	choice = int(input("Enter your choice: "))
	if(choice==1):
		data = input("\nEnter number to insert: ")
		bst.insert(data)
	elif(choice==2):
		data = input("\nEnter number to find: ")
		print(bst.find(data))
	elif(choice==3):
		choice = 3