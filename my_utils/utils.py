# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    items = []
    current = head
    while current:
        items.append(str(current.val))
        current = current.next
    print(" -> ".join(items))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to create a binary tree from a list (level order)
def create_binary_tree(items):
    if not items:
        return None
    
    root = TreeNode(items[0])
    queue = [root]
    i = 1
    while queue and i < len(items):
        node = queue.pop(0)
        
        if i < len(items) and items[i] is not None:
            node.left = TreeNode(items[i])
            queue.append(node.left)
        i += 1
        
        if i < len(items) and items[i] is not None:
            node.right = TreeNode(items[i])
            queue.append(node.right)
        i += 1
        
    return root

# Helper function to print a binary tree (in-order)
def print_binary_tree(root):
    if not root:
        return
    print_binary_tree(root.left)
    print(root.val, end=' ')
    print_binary_tree(root.right)

