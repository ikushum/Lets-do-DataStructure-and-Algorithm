class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.parent = TrieNode()

	def add(self, key):
		if(len(key)==0):
			self.parent.isEndOfWord = True
			return
		index = ord(key[0])-ord('a')
		if(self.parent.children[index] == None):
			self.parent.children[index] = Trie()
		self.parent.children[index].add(key[1:])

	def search(self, key):
		if(len(key)==0):
			print(self.parent.isEndOfWord)
			return self.parent.isEndOfWord
		index = ord(key[0])-ord('a')
		if(self.parent.children[index] == None):
			print(False)
			return False
		self.parent.children[index].search(key[1:])		

	def displayWords(self,word=''):
		children = self.parent.children
		for subTree in children:	 		
			if(subTree):
				word+= chr(children.index(subTree) + ord('a'))	
				if(subTree.parent.isEndOfWord): print(word) 
				subTree.displayWords(word=word)
				word=word[:-1]
		word = ''
