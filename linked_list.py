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

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception('Node with data %s is not found' % target_node_data')

    def list_length(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count


"""     def __repr__(self, data) -> str:
        self.data = data
        return self.data """
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
