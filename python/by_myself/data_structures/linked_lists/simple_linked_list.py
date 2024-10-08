class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self) -> None:
        self.head = None

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None") 


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display() 