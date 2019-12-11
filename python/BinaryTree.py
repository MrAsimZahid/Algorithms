#Node class/structure
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Binary tree class
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

#Choose traversal type
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inOrder_print(tree.root, "")
        elif traversal_type == "postOrder":
            return self.postOrder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False

#Method Pre-Order traversal 
    def preorder_print(self, start, traversal):
        """ Root->left->right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

#Method In-Order traversal
    def inOrder_print(self, start, traversal):
	    """ Left -> root -> right"""
	    if start:
	        traversal = self.inOrder_print(start.left, traversal)
	        traversal += (str(start.value) + "-")
	        traversal =  self.inOrder_print(start.right, traversal)
	    return traversal

#Method Post-Order traversal
    def postOrder_print(self, start, traversal):
        """ Left -> right -> root"""
        if start:
            traversal = self.inOrder_print(start.left, traversal)
            traversal =  self.inOrder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


#Main function
#Enter values in the tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


#print tree in different trversals
print(tree.print_tree("preorder"))
print(tree.print_tree("postOrder"))
print(tree.print_tree("inorder"))
