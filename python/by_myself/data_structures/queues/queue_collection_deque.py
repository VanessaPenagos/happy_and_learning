from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return None
        
    def size(self):
        return len(self.items)
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
