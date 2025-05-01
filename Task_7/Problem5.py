class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def delete(self, value):
        currentNode = self.head
        previousNode = None
        while currentNode is not None:
            if currentNode.value == value:
                if previousNode is None:
                    self.head = currentNode.nextNode   
                else:
                         previousNode.nextNode = currentNode.nextNode  
                return
            previousNode = currentNode
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end= " ")
            currentNode = currentNode.nextNode


print(f"Initial Linked List:")
First_ll = LinkedList()
First_ll.insert(1)
First_ll.insert(2)
First_ll.insert(3)
First_ll.insert(4)
First_ll.printLinkedList( )

First_ll.insert(5)
print(f"\n After insert a new node (5):")
First_ll.printLinkedList( ) 
print("\n")
First_ll.delete(2)
print(f"After delete a existing node (2):")
First_ll.printLinkedList( ) 
print("\n")
