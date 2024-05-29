import heapq

def astar(graph, start, goal, heuristic):
    # Initialize the priority queue with the start node and priority 0
    open_list = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_list:
        # Pop the node with the lowest priority
        current_cost, current_node = heapq.heappop(open_list)
        
        # Print the priority queue after popping the current node
        print("Priority queue after pop:", open_list)
        
        if current_node == goal:
            # Reconstruct the path from start to goal
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            print("Path found:", ' -> '.join(path))
            return
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                # Push the neighbor into the priority queue with the calculated priority
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current_node
                
                # Print the priority queue after pushing a new node
                print("Priority queue after push:", open_list)
    
    print("No path found between", start, "and", goal)

# Directly execute the setup and call the astar function
graph = {}
heuristic = {}

n = int(input("Enter the number of edges: "))
for _ in range(n):
    u, v, w = input("Enter edge and weight (format: source destination weight): ").split()
    w = int(w)
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    graph[v][u] = w

for node in graph.keys():
    heuristic[node] = int(input(f"Enter heuristic value for node {node}: "))

start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

print("A* Search:")
astar(graph, start_node, end_node, heuristic)














