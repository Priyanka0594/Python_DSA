# Node of a doubly linked list
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # reference to next node in DLL
        self.next = next
        # reference to previous node in DLL
        self.prev = prev
        self.data = data

def traverse(head):
    # Traverse the doubly linked list and print its elements
    current = head
    while current:
      # Print current node's data
        print(current.data, end=" <-> ")
        # Move to the next node
        current = current.next
    print("None")


def insert_at_beginning(head, data):
    # Insert a new node at the beginning of the doubly linked list
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Function to insert a node after a given node in a doubly linked list
def insert_after_node(node, data):
    if node is None:
        print("Error: The given node is None")
        return

    new_node = Node(data)
    new_node.prev = node
    new_node.next = node.next

    if node.next:
        node.next.prev = new_node

    node.next = new_node


# Function to insert a node before a given node in a doubly linked list
def insert_before_node(node, data):
    if node is None:
        print("Error: The given node is None")
        return

    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node

    if node.prev:
        node.prev.next = new_node

    node.prev = new_node

def insert_at_end(head, data):
    # Insert a new node at the end of the doubly linked list
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head

def delete_at_beginning(head):
    # Delete the first node from the beginning of the doubly linked list
    if head is None:
        print("Doubly linked list is empty")
        return None

    if head.next is None:
        return None

    new_head = head.next
    new_head.prev = None
    del head
    return new_head

def delete_at_position(head, position):
    # Delete the node at a given position from the doubly linked list
    if head is None:
        print("Doubly linked list is empty")
        return None

    if position < 0:
        print("Invalid position")
        return head

    if position == 0:
        if head.next:
            head.next.prev = None
        return head.next

    current = head
    count = 0
    while current and count < position:
        current = current.next
        count += 1

    if current is None:
        print("Position out of range")
        return head

    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next

    del current
    return head

def delete_at_end(head):
    # Delete the last node from the end of the doubly linked list
    if head is None:
        print("Doubly linked list is empty")
        return None

    if head.next is None:
        return None

    current = head
    while current.next.next:
        current = current.next

    del_node = current.next
    current.next = None
    del del_node
    return head



def reverse_dll(head):
    # If head is empty or there is only
    # one element, return the head directly
    if head is None or head.next is None:
        return head

    # Initialize a stack to store values
    st = []
    # Initialize the node pointer
    #'temp' at head
    temp = head

    # Traverse the doubly linked list
    # via the 'temp' pointer
    while temp is not None:
        # Insert the data of the current
        # node into the stack
        st.append(temp.data)
        # Traverse further
        temp = temp.next

    # Reinitialize 'temp' to head
    temp = head

    # Second iteration of the DLL
    # to replace the values
    while temp is not None:
        # Replace the value pointed to
        # by 'temp' with the value from
        # the top of the stack and pop it
        temp.data = st.pop()
        # Traverse further
        temp = temp.next

    # Return the updated doubly linked list
    # where the values of nodes from both
    # ends have been swapped
    return head