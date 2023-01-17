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
    def l_length(self):
        temp=self.head
        count = 0
        while (temp):
            count+=1
            temp = temp.next
        return count
    def iter_append_left(self,l1,l2):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_length = l1.l_length()
        l2_length = l2.l_length()
        l1_sub_l2 = l1_length - l2_length
        l2_sub_l1 = l2_length - l1_length
        if l1_sub_l2 > 0:
            for i in l1_sub_l2:
                l2[i].add_left(['0'])
        else:
            for i in l2_sub_l1:
                l1[i].add_left(['0'])

