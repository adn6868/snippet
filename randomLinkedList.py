class Node:
	def __init__(self,x: int, nxt: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.nxt = nxt
		self.random = random

	def __str__(self):
		rv1 = str(self.val) + '->'
		rv2 = ''
		if self.random:
			rv3 = str(self.random.val) + '--'
		else:
			rv3 = 'N--'
		ite = self.nxt
		while ite is not None:
			rv1 += str(ite.val) + '->'
			rv2 += '|  '
			if ite.random:
				rv3 += str(ite.random.val) +'--'
			else:
				rv3 +='N--'
			ite = ite.nxt


		return rv1 + '\n' + rv2 + '\n' + rv3



def firstCopy(head: 'Node') -> 'Node':
	rv = Node(head.val)
	ite1 = head
	ite2 = rv
	# print(ite1)
	# print(type(ite1))
	# print(head)
	while ite1.nxt is not None:
	    ite2.nxt = Node( ite1.nxt.val )
	    ite1 = ite1.nxt
	    ite2 = ite2.nxt
	return rv
    
def randCopy(first: 'Node', head : 'Node') ->  'Node':
	ite1 = first
	ite2 = head
	while ite1.nxt is not None:
		if ite2.random is None:
			ite1.random = None
		else:
			target = ite2.random
			tmp = ite1
			while tmp.val != target.val and tmp.nxt != target.nxt:
				tmp = tmp.nxt
			ite1.random = tmp
		ite1 = ite1.nxt
		ite2 = ite2.nxt
	return ite1

def copyRandomList(head: 'Node') -> 'Node':
	first = firstCopy(head)
	return first
	# return randCopy(first,head)

def test():
	
	Node4 = Node(4)
	Node3 = Node(3,Node4)
	Node2 = Node(2,Node3)
	Node1 = Node(1,Node2)
	Node0 = Node(0,Node1)

	Node0.random = Node3
	Node1.random = Node0
	Node2.random = Node0
	Node3.random = Node4
	Node4.random = Node1
	
	print(Node0)

	copied = copyRandomList(Node0)
	print(copied)

test()