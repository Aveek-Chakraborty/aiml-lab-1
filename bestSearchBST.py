import heapq

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    """Insert a key into the binary search tree."""
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def best_first_search(root, target, heuristic_values):
    """Best-First Search algorithm implementation."""
    if root is None:
        return False, []

    frontier = [(heuristic_values[root.val], root, [root.val])]  # Priority queue for nodes
    explored = set()  # Set to keep track of explored nodes

    while frontier:
        _, node, path = heapq.heappop(frontier)  # Pop node with lowest heuristic value

        if node.val == target:  # Check if target is found
            return True, path

        explored.add(node)  # Add current node to explored set

        # Add left child to frontier if not explored
        if node.left and node.left not in explored:
            heapq.heappush(frontier, (heuristic_values.get(node.left.val, float('inf')), node.left, path + [node.left.val]))

        # Add right child to frontier if not explored
        if node.right and node.right not in explored:
            heapq.heappush(frontier, (heuristic_values.get(node.right.val, float('inf')), node.right, path + [node.right.val]))

    return False, []

# Creating the binary search tree based on user input
keys = input("Enter keys for the binary search tree separated by spaces: ").split()
keys = list(map(int, keys))
root = None
for key in keys:
    root = insert(root, key)

# Asking for heuristic values
heuristic_values = {}
for key in keys:
    heuristic = int(input(f"Enter heuristic value for node {key}: "))
    heuristic_values[key] = heuristic

# Performing best-first search
target = int(input("Enter target value to search: "))
found, path = best_first_search(root, target, heuristic_values)
if found:
    print("Path found:", path)
else:
    print("Target value not found in the tree.")
