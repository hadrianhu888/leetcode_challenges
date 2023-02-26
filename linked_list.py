class Node:
    """Definition for singly linked list of nodes"""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

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
            raise Exception('Node with data %s is not found' % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception('Node with data %s is not found' % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception('Node with data %s not found' % target_node_data)

    def get_list_element_iter(self, target_node_data):
        current = self.head
        while current != None:
            if current.data == target_node_data:
                return True
            current = current.next
        return False

    def get_list_element_rec(self, target_node_data, key):
        if (not target_node_data):
            return False
        if (target_node_data.data == key):
            return True
        return self.get_list_element_rec(target_node_data.next, key)

    def list_length(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest
    """
    def list_queue(self, head):
        
        if head is None or head.next is None:
            return head
        if head is not None and head.next is not None:
            head.next = head
        raise Exception('Node with data %s is not found' % head)

    def list_deque (self,head):
        if head.tail is None or head.next is None: 
            return self.head
        if head is not None or head.next is not None:
            return self.tail 
        else:
            self.tail = self.head 
            self.head = self.tail
        raise Exception('Node with data %s is not found' % head)
    """
    def list_queue(self,head):
        """
        Queues a queue
        """
        if head is None or head.next is None:
            return head
        if head is not None and head.next is not None:
            head.next = head
        raise Exception('Node with data %s is not found' % head)
    def list_deque(self,head):
        """
        Deques a queue 
        """
        if head.tail is None or head.next is None:
            return self.head
        if head is not None or head.next is not None:
            return self.tail
        else:
            self.tail = self.head
            self.head = self.tail
        raise Exception('Node with data %s is not found' % head)



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


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print("->".join(nodes))
