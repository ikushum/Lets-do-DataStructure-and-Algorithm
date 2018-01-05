class Node:
	def __init__(self, data):
		self.data=data
		self.left_child=None
		self.right_child=None

class Tree:
	def __init__(self, data):
		self.parent = Node(data)

	def insert(self, data):
		if not(self.parent.data): 
			self.parent.data = data
			print(str(data) + ' was inserted')
		else:
			if(self.parent.data == data):
				print(str(data) + ' already exists')
				return False
			elif(self.parent.data > data):
				if(self.parent.left_child):
					return self.parent.left_child.insert(data)
				else: 
					self.parent.left_child = Tree(data)
					print(str(data)+' was inserted')
					return True
			else:
				if(self.parent.right_child):
					return self.parent.right_child.insert(data)
				else: 
					self.parent.right_child = Tree(data)
					print(str(data)+' was inserted')
					return True			

	def find(self, data):
		if(self.parent.data):
			if(data == self.parent.data):
				print(str(data) + ' is present')
				return True
			elif(data < self.parent.data):
				self.parent.left_child.find(data) if self.parent.left_child else print(str(data) + ' not found')
			elif(data > self.parent.data) :
				self.parent.right_child.find(data) if self.parent.right_child else print(str(data) + ' not found')
			return False
		else:
			print('Tree is empty') 
			return False

	def delete(self,data,delNodeParent=None):
		if(self.parent.data):
			if(data == self.parent.data):
				delNode = self.parent
				if(delNode.left_child== delNode.right_child == None):
					if(delNodeParent.left_child == self):
						delNodeParent.left_child=None
					else:
						delNodeParent.right_child=None
				elif(delNode.left_child == None):
					if(delNodeParent.left_child == self):
						delNodeParent.left_child=delNode.right_child
					else:
						delNodeParent.right_child=delNode.right_child
				elif(delNode.right_child == None):
					if(delNodeParent.left_child == self):
						delNodeParent.left_child=delNode.left_child
					else:
						delNodeParent.right_child=delNode.left_child
				else:
					min_node = self.findMinNode()
					delNode.data = min_node.parent.data
					self = delNode.right_child
					self.delete(min_node.parent.data, delNodeParent=self)
				return True
			elif(data < self.parent.data):
				return self.parent.left_child.delete(data,delNodeParent=self.parent) if self.parent.left_child else False
			elif(data > self.parent.data) :
				return self.parent.right_child.delete(data,delNodeParent=self.parent) if self.parent.right_child else False
		else:
			return False

	def inorder(self):
		if(self.parent.data):
			if self.parent.left_child:
				self.parent.left_child.inorder()
			print (self.parent.data)
			if self.parent.right_child:
				self.parent.right_child.inorder()
		else:
			print('Tree is empty')

	def findMinNode(self):
		min_node = self.parent.right_child
		while(min_node.parent.left_child != None):
			min_node = min_node.parent.left_child
		return min_node		

bst = Tree(None)
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
		if(bst.delete(data)):
			print(str(data) + ' was deleted')
		else:
			print(str(data) + ' was not deleted')			
	elif(choice==4):
		bst.inorder() 	