class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None


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

            


llist = linkedList()
llist.append("A")
llist.append("B")
llist.append("c")
llist.append("d")

print(llist.head.data)
llist.prepend("f")
llist.insertAfterNode(llist.head.next, "E")

print(llist.head.data)

llist.printList()
