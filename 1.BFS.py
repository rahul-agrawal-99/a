
class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def BFS(root):
	h = height(root)
    
	for i in range(1, h+1):
		printCurrentLevel(root, i)

def printCurrentLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.data, end=" -> ")
	else:
		printCurrentLevel(root.left, level-1)
		printCurrentLevel(root.right, level-1)

def height(node):
	if node is None:
		return 0
	else:
		lheight = height(node.left)
		rheight = height(node.right)
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(7)
root.right.left = Node(5)


print("height of tree is:", height(root)-1)
print("BFS traversal of binary tree is -")
BFS(root)

