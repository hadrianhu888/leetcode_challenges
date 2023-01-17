class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return "-> ".join(nodes)
    
