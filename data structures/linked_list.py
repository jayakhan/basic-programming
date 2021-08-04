class LinkedList(object):
    """ Initialize a linked list """
    def __init__(self, head=None)
        self.head = head

    """ Create a node and then insert data """
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    """ Return size of linked list """
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return current

    