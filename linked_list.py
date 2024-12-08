class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    
    def insertAtIndex(self,data,index):
        if(index ==0):
            self.insertAtBegin(data)
            return
        
        position=0

        current_node=self.head
        while(current_node!=None and position+1!=index):
            position=position+1
            current_node=current_node.next
        
        if current_node!= None:
            new_node=Node(data)
            new_node.next=current_node.next
            current_node.next=new_node
        else:
            print("Index is not Present")
        
    def insertAtEnd(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next

        current_node.next=new_node

    def removeFirstNode(self):
        if self.head is None:
            return
        self.head=self.head.next

    def removeLastNode(self):
        if self.head is None:
            return
        #checking if the linked list only contains one node
        if self.head.next is None:
            self.head=None
            return
        
        #Traversing to the second last node
        current_node=self.head
        while(current_node.next and current_node.next.next):
            current_node=current_node.next
        
        current_node.next=None

    def removeAtIndex(self, index):
        if(self.head.next is None):
            return
        
        if index == 0:
            self.removeFirstNode()
            return
        
        position=0
        current_node=self.head
        while current_node is not None and current_node.next is not None and position+1<index:
            position+=1
            current_node=current_node.next
        
        if current_node is not None and current_node.next is not None:
            current_node.next=current_node.next.next
        else:
            print("index not present to remove")

    
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


llist=LinkedList()
llist.insertAtBegin('a')
llist.insertAtEnd('z')
llist.insertAtIndex('b',1)
llist.removeAtIndex(1)
llist.printLL()