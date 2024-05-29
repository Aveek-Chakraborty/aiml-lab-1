class TreeNode:
    def __init__(self, key):
        self.val = key  # Value of the node
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node

def insert(root, key):
    """Insert a key into the binary search tree."""
    if root is None:
        # If the tree is empty, create a new node with the given key
        return TreeNode(key)
    else:
        # If the tree is not empty, recursively insert the key in the appropriate subtree
        if root.val < key:
            # If the key is greater than the current node's value, insert it into the right subtree
            root.right = insert(root.right, key)
        else:
            # If the key is less than or equal to the current node's value, insert it into the left subtree
            root.left = insert(root.left, key)
    return root

def search(root, key, path=[]):
    """Search for a key in the binary search tree using DFS with recursion."""
    if root is None:
        # If the root is None, the key does not exist in the tree
        return None, []

    path.append(root.val)  # Add current node to the path

    if root.val == key:
        # If the key is found at the current node, return the node and the path
        return root, path

    if root.val < key:
        # If the key is greater than the current node's value, search in the right subtree
        return search(root.right, key, path)
    else:
        # If the key is less than the current node's value, search in the left subtree
        return search(root.left, key, path)

# Take input keys for the binary search tree
keys = input("Enter keys for the binary search tree separated by spaces: ").split()
keys = list(map(int, keys))
root = None
for key in keys:
    # Insert each key into the binary search tree
    root = insert(root, key)

# Take input for the key to search
search_key = int(input("Enter the key to search for: "))
# Perform the search operation
result, path = search(root, search_key)
if result:
    # If the key is found, print the result and the path
    print(f"Key {search_key} found in the binary search tree.")
    print("Path:", path)
else:
    # If the key is not found, print a message indicating it
    print(f"Key {search_key} not found in the binary search tree.")
