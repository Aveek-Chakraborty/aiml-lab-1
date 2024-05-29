import heapq

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.cost = 0  # Initialize cost for RBFS

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

def rbfs(node, f_limit, heuristic_values, target):
    """
    Recursive Best-First Search (RBFS) algorithm implementation.
    """
    def rbfs_helper(node, f_limit):
        if node is None:
            return float('inf'), []

        f_value = node.cost + heuristic_values[node.val]
        if node.val == target:
            return f_value, [node.val]

        successors = []
        if node.left:
            node.left.cost = node.cost + 1  # Assuming uniform cost for simplicity
            successors.append(node.left)
        if node.right:
            node.right.cost = node.cost + 1  # Assuming uniform cost for simplicity
            successors.append(node.right)

        if not successors:
            return float('inf'), []

        print("Exploring node:", node.val)
        while True:
            successors.sort(key=lambda x: x.cost + heuristic_values[x.val])  # Sort by f_value
            print("Successors:", [n.val for n in successors])
            best = successors[0]
            alternative = successors[1] if len(successors) > 1 else None

            if alternative:
                alternative_cost = alternative.cost + heuristic_values[alternative.val]
            else:
                alternative_cost = float('inf')

            result, path = rbfs_helper(best, min(f_limit, alternative_cost))
            if result == float('inf'):
                return float('inf'), []
            if result <= f_limit:
                path.insert(0, node.val)
                return result, path

            # Update f_limit based on the best alternative node's f_value
            f_limit = min(f_limit, result)
            heuristic_values[best.val] = result
            print("Updated heuristic for node", best.val, ":", heuristic_values[best.val])

    node.cost = 0
    result, path = rbfs_helper(node, f_limit)
    return path if result != float('inf') else None

# Example data
keys = [10, 5, 15, 2, 7, 12, 18]
root = None
for key in keys:
    root = insert(root, key)

# Heuristic values for each node
heuristic_values = {
    10: 3,
    5: 6,
    15: 2,
    2: 9,
    7: 4,
    12: 5,
    18: 1
}

target = 7
path = rbfs(root, float('inf'), heuristic_values, target)
if path:
    print("Path found:", path)
else:
    print("Target value not found in the tree.")
