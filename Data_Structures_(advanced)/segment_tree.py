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
			self.tree[node]=Node(start,end,self.array[start-1], self.array[start-1])
		else:
			mid = (start + end)//2
			self.buildTree(2*node, start, mid)
			self.buildTree(2*node+1, mid+1, end)
			low = min(self.tree[2*node].low,self.tree[2*node+1].low)
			high = max(self.tree[2*node].low,self.tree[2*node+1].low)			
			self.tree[node] = Node(start,end,high,low)	

	def query(self, node, start, end):
		if(self.tree[node].start >= start and self.tree[node].end <= end):
			print(self.tree[node].low)	
			return		
		if(self.tree[node].start == self.tree[node].end):
			return
		if(self.tree[node].start > end or self.tree[node].end < start):
			return
		self.query(node*2, start, end)
		self.query(node*2+1, start, end)


t=Tree([1,3,5,7,9,11])
t.query(1,2,5)