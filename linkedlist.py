class LinkedList:
	class Iter:
		def __init__(self, p, parent):
			self.p = p
			self.parent = parent
		def next(self):
			if self.p is not self.parent:
				v = self.p
				self.p = self.p.next
				return v
			raise StopIteration
	class ReversedIter:
		def __init__(self, p, parent):
			self.p = p
			self.parent = parent
		def __iter__(self):
			return self
		def next(self):
			if self.p is not self.parent:
				v = self.p
				self.p = self.p.prev
				return v
			raise StopIteration
	class Node:
		def __init__(self, elem, parent=None, prev=None, next=None):
			self.elem = elem
			self.prev = prev
			self.next = next
			self.parent = parent
		def detach(self):
			if self.parent:
				self.parent.count -= 1
			if self.prev is not None:
				self.prev.next = self.next
			if self.next is not None:
				self.next.prev = self.prev
		def __iter__(self):
			return LinkedList.Iter(self.next, self.parent)
		def __reversed__(self):
			return LinkedList.ReversedIter(self.prev, self.parent)
		
	def __init__(self, l=[]):
		self.count = 0
		self.prev = self
		self.next = self

		for elem in l:
			self.append(elem)
		
	def append(self, elem):
		node = self.Node(elem, parent=self, prev=self.prev, next=self)
		self.prev.next = node
		self.prev = node
		self.count += 1
		
	def __getitem__(self, idx):
		p = self.next
		if idx >= self.count:
			raise IndexError
		elif idx < 0:
			idx = idx + self.count
			if idx >= self.count or idx < 0:
				raise IndexError
			
		count = 0
		while count < idx:
			p = p.next
			count += 1
		return p
	
	def __len__(self):
		return self.count

	def __iter__(self):
		return self.Iter(self.next, self)

	def __reversed__(self):
		return self.ReversedIter(self.prev, self)

