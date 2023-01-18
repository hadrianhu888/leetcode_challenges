class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self, data) -> str:
        self.data = data
        return self.data

    def list_length(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count


"""     def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return "-> ".join(nodes) """

"""     def iter_append_left(self,l1,l2):
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
                l1[i].add_left(['0']) """
