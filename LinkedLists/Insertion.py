"""
 Linked list are Nodes that has a data and next, Next points from one node to another
 * Start of the list is referred to as head
 * THe end of linked list is called Null(None)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # Get the first node in the list
        first_node = self.head
        while first_node:
            # Print the data of the first node
            print(first_node.data)
            # move the first node to the next node
            first_node = first_node.next

    def append(self, data):
        # Create the node
        new_node = Node(data)
        # Check if the Linked list is empty
        # Remember head points to the start of the start of the linked list, so if the start of the linked list
        # is None, the Linked list is empty
        if not self.head:
            self.head = new_node
            return

        # Since we are going to add the node at the end of the linked list, we need to get the first node then iterate
        # until we get to the end
        last_node = self.head
        while last_node.next:
            # This is iterating from the start to the end of the linked it
            last_node = last_node.next
        # If the condition fails, i.e last_node.next is None, the make that node next component the new node
        last_node.next = new_node

    def prepend(self, data):
        """
        Add a node as the first node i.e head
        :param data:
        :return:
        """
        # Create the node
        new_node = Node(data)
        # Make the next of the new node the current first node
        new_node.next = self.head
        # switch the current head to the new node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous Node does not exist')
            return
        # Create the node
        new_node = Node(data)
        # Set the new node next as the prev node next
        new_node.next = prev_node.next
        # Set the prev node next to new node
        prev_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node(llist.head.next, 'F')
llist.print_list()
