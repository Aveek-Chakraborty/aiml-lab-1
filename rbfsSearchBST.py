class TreeNode:
    def __init__(self, key):
        self.val = key  # Value of the node
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node

class RBFSNode:
    def __init__(self, node, f):
        self.node = node  # Reference to the TreeNode
        self.f = f  # f-value for the node

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

def recursive_best_first_search(root, f_limit):
    return rbfs(root, f_limit)

def rbfs(node, f_limit):
    if node is None:
        return None

    if node.val == f_limit:
        return node

    children = [node.left, node.right]
    children = [RBFSNode(child, max(child.val, node.val)) for child in children if child is not None]

    if not children:
        return None

    while True:
        children.sort(key=lambda x: x.f)
        best = children[0]
        if best.f > f_limit:
            return None
        alternative = children[1].f if len(children) > 1 else float('inf')
        result = rbfs(best.node, min(f_limit, alternative))
        if result is not None:
            return result

def search(root, key):
    """Search for a key in the binary search tree using RBFS."""
    if root is None:
        # If the root is None, the key does not exist in the tree
        return None

    f_limit = float('inf')  # Initial f-limit
    result = recursive_best_first_search(root, f_limit)

    return result

# Example usage:

# Construct the binary search tree
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
root = None
for key in keys:
    root = insert(root, key)

# Perform RBFS on the binary search tree to search for a key
search_key = 6
result = search(root, search_key)

# Print the result
if result:
    print(f"Key {result.val} found in the binary search tree.")
else:
    print(f"Key {search_key} not found in the binary search tree.")
