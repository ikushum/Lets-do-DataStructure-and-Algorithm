class Node:
	def __init__(self, start, end, high, low):
		self.start=start 
		self.end= end 
		self.high=high 
		self.low=low

class Tree:
	def __init__(self,array):
		self.array = array
		n=len(array)
		self.tree = [None] * (4*n)
		self.buildTree(1, 1, n)

	def buildTree(self, node, start, end):
		if(start==end):
			print(node)
			self.tree[node]=Node(start,end,self.array[start-1], self.array[start-1])
		else:
			print(node)
			mid = (start + end)//2
			self.buildTree(2*node, start, mid)
			self.buildTree(2*node+1, mid+1, end)
			low = min(self.tree[2*node].low,self.tree[2*node+1].low)
			high = max(self.tree[2*node].low,self.tree[2*node+1].low)			
			self.tree[node] = Node(start,end,high,low)	

t=Tree([1,3,5,7,9,11])
print(t.tree[6].high)