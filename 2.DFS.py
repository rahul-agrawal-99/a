
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def printPreorder(root):
 
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
		

root = Node("S")
root.left = Node("A")
root.right = Node("H")
root.left.left = Node("B")
root.left.left.left = Node("D")
root.left.left.right = Node("E")
root.left.right = Node("C")
root.left.right.right = Node("G")
root.right.right = Node("J")
root.right.left = Node("I")
root.right.left.right = Node("K")

print("\nInorder traversal of binary tree is")
printPreorder(root)
