class Node:
	def __init__(self, data):
		self.data=data
		self.left_child=None
		self.right_child=None

	def insert(self, data):
		if(self.data == data):
			print(str(data) + ' already exists')
			return False
		elif(self.data > data):
			if(self.left_child):
				return self.left_child.insert(data)
			else: 
				self.left_child = Node(data)
				print(str(data)+' was inserted')
				return True
		else:
			if(self.right_child):
				return self.right_child.insert(data)
			else: 
				self.right_child = Node(data)
				print(str(data)+' was inserted')
				return True

	def find(self, data):
		if(data == self.data):
			print(str(data) + ' is present')
			return True
		elif(data < self.data):
			self.left_child.find(data) if self.left_child else print(str(data) + ' not found')
		elif(data > self.data) :
			self.right_child.find(data) if self.right_child else print(str(data) + ' not found')
		return False

	def delete(self, data, parent=None):
		if(data == self.data):
			nodeToDelete = self
			if(nodeToDelete.left_child == nodeToDelete.right_child == None):
				if(parent.left_child == nodeToDelete):
					parent.left_child=None
				else:
					parent.right_child=None
			elif(nodeToDelete.left_child == None):
				if(parent.left_child == nodeToDelete):
					parent.left_child=nodeToDelete.right_child
				else:
					parent.right_child=nodeToDelete.right_child
			elif(nodeToDelete.right_child == None):
				if(parent.left_child == nodeToDelete	):
					parent.left_child=nodeToDelete.left_child
				else:
					parent.right_child=nodeToDelete.left_child
			else:
				min_node = nodeToDelete.findMinNode()
				nodeToDelete.data = min_node.data
				self = nodeToDelete.right_child
				self.delete(min_node.data, parent=nodeToDelete)
			return(data)
		elif(data < self.data):
			return(self.left_child.delete(data,parent=self)) if self.left_child else print(str(data) + ' not found')
		elif(data > self.data) :
			return(self.right_child.delete(data,parent=self)) if self.right_child else print(str(data) + ' not found')

	def inorder(self):
		if self:
			if self.left_child:
				self.left_child.inorder()
			print (self.data)
			if self.right_child:
				self.right_child.inorder()

	def findMinNode(self):
		min_node = self.right_child
		while(min_node.left_child != None):
			min_node = min_node.left_child
		return min_node

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
			search_result = self.parent.find(data)
			if search_result==True:
				return True
			else:
				return False
		else:
			print(str(data) + ' not found') 
			return False

	def delete(self,data):
		if(self.parent):
			deleted_element = self.parent.delete(data,parent=self.parent)
			print(str(deleted_element) + ' was deleted')	
		else:
			print('Tree is empty')

	def inorder(self):
		if(self.parent):
			self.parent.inorder()
		else:
			print('Tree is empty')

choice = 0
while(choice != 5):
	print("\n1) Press 1 to insert\n2) Press 2 to search\n3) Press 3 to Delete\n4) Press 4 to display inorder\n5) Press 5 to Quit")
	choice = int(input("Enter your choice: "))
	if(choice==1):
		data = int(input("\nEnter number to insert: "))
		bst.insert(data)
	elif(choice==2):
		data = int(input("\nEnter number to find: "))
		bst.find(data)
	elif(choice==3):
		data = int(input("\nEnter number to delete: "))
		bst.delete(data)
	elif(choice==4):
		bst.inorder()		