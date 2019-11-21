class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
#Insertion in linked list

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next


    def append(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def prepend(self, data):
        newNode =  Node(data)

        newNode.next = self.head
        self.head = newNode

    def insertAfterNode(self, previousNode, data):
        if not previousNode:
            print("previous node is not in the list")
            return
        newNode = Node(data)
        newNode.next = previousNode.next
        previousNode.next = newNode

#Deletion in linked list
    def deleteNode(self, data):
        currentNode = self.head
        if currentNode and currentNode.data == data:
            self.head = currentNode.next
            currentNode = None
            return

        prev = None
        while currentNode and currentNode.data != data:
            prev = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            return

        prev.next = currentNode.next
        currentNode = None

#Deletion Node at position
    def deleteNodePosition(self, pos):
        
        currentNode = self.head
        
        if pos == 0:
            self.head = currentNode.next
            currentNode = None
            return

        prev = None
        count = 0
        while currentNode and count != pos:
            prev = currentNode
#s            currentNode = curretNode.next
            count += 1

        if currentNode is None:
            print("enter valid address")
            return

        prev.next = currentNode.next
        currentNode = None



llist = linkedList()
llist.append("A")
llist.append("B")
llist.append("c")
llist.append("d")

print(llist.head.data)
llist.prepend("f")
llist.insertAfterNode(llist.head.next, "E")
#llist.deleteNodePosition(2)
print(llist.head.data)
llist.deleteNode("f")
llist.printList()
