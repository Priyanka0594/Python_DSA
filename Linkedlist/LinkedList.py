class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_end(root, item):
    temp = Node(item)
    if root is None:
        return temp
    
    last = root
    while last.next is not None:
        last = last.next
    
    last.next = temp
    return root

def array_to_list(arr):
    root = None
    for item in arr:
        root = insert_end(root, item)
    return root

# Function to convert a singly linked list to an array
def linked_list_to_array(head):
    arr = []
    curr = head

    while curr is not None:
        arr.append(curr.data)
        curr = curr.next

    return arr

def display(root):
    while root is not None:
        print(root.data, end=" ")
        root = root.next

def deleteTail(head) :
    # // Check if the linked list is empty or has only one node
    if head is None or head.next is None : 
        return None
    # // Create a temporary pointer for traversal
    temp = head

    # // Traverse the list until the second-to-last node
    while temp.next.next != None :
        temp = temp.next
    # // Nullify the connection from the second-to-last node to delete the last node
    temp.next = None

    # // Return the updated head of the linked list
    return head

def length_of_linked_list(head):
    cnt = 0
    temp = head
    
    # Traverse the linked list and count nodes
    while temp is not None:
        temp = temp.next
        cnt += 1
  
    return cnt

# Function to check if a given element is present in the linked list
def check_if_present(head, desired_element):
    temp = head

    # Traverse the linked list
    while temp is not None:
        # Check if the current node's data is equal to the desired element
        if temp.data == desired_element:
            return 1  # Return 1 if the element is found# 
        #Move to the next node
        temp = temp.next

    return 0  # Return 0 if the element is not found in the linked list


def middle_element(head):
    if head is None or head.next is None:
        return head
    
    n = length_of_linked_list(head)
    temp = head 

    if n%2 == 0:
        mid = n//2 + 1
    else :
        mid = n//2
    
    while temp is not None :
        temp = temp.next
        mid -= 1
    
        if mid == 0:
            # break out of the loop
            # to return temp
            break
            
    # Move temp ahead
    temp = temp.next


    # Return the middle node.
    return temp
        
#Optimised Function to find the middle 
# node of a linked list
def find_middle(head):
    # Initialize the slow pointer to the head.
    slow = head   
    
    # Initialize the fast pointer to the head.
    fast = head   

    # Traverse the linked list using
    # the Tortoise and Hare algorithm.
    while fast and fast.next and slow:
        # Move fast two steps.
        fast = fast.next.next 
        # Move slow one step.
        slow = slow.next       

    # Return the slow pointer,
    # which is now at the middle node.
    return slow     
            
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    root = array_to_list(arr)
    display(root)
    # Find the middle node
    middle_node = middle_element(root)
    
    middle_node1 = find_middle(root)

    # Display the value of the middle node
    print("The middle node value is:", middle_node.data)
    
    print("The middle node using optimal value is:", middle_node1.data)
   
