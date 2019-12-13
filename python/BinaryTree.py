# Binary Tree Implementation with different
#  traversals types



# Stack dataStructure class
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()
    
    def is_empty(self):
        return len(self.items) == 0


#Class Queue
class Queue(object):
    def __init__(self):
        self.items = []

#Enter value in queue
    def enqueue(self, item):
        return self.items.insert(0, item)
#Pop values from queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
 #Redefine length function   
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)
#-----------------------------------------------


#Binary Tree
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
        elif traversal_type == "levelorder":
            return self.levelOrder_print(tree.root)
        elif traversal_type == "levelorder":
            return self.levelOrder_print(tree.root)
        elif traversal_type == "reverseLeveOrder":
            return self.reverselevel_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) 
            + " is not supported")
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

#Method for level order traversal
    def levelOrder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return traversal

#Reverse Level order traversal
#I used stack and queue data structures to implement
#reverse-level-order traversal BinaryTree
#

    def reverselevel_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
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
print("Pre-order\t" + tree.print_tree("preorder"))
print("Post-order\t" + tree.print_tree("postOrder"))
print("In-order\t" + tree.print_tree("inorder"))
print("Level-order\t" + tree.print_tree("levelorder"))
print("Reverse-Level-order " + tree.print_tree("reverseLeveOrder"))