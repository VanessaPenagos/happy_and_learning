class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.next
        print("None")

    def display_reverse(self):
        current_node = self.head
        if not current_node:
            print("None")
            return
        
        while current_node.next:
            current_node = current_node.next
        
        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.prev
        print("None")

doubly_linked_list = DoublyLinkedList()

doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

doubly_linked_list.display()  
