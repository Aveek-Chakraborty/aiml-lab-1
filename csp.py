def is_valid(map, region, color, color_assignment):
    """
    Check if the given color can be assigned to the region without
    conflicting with neighboring regions.
    """
    for neighbor in map[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def solve_map_coloring(map, regions, colors, color_assignment={}):
    """
    Solve the map coloring problem using backtracking.
    """
    # Base case: If all regions are colored, return the color assignment
    if len(color_assignment) == len(regions):
        return color_assignment
    
    # Choose the next region to color (the first uncolored region)
    current_region = [r for r in regions if r not in color_assignment][0]
    
    for color in colors:
        # Check if the color is valid for the current region
        if is_valid(map, current_region, color, color_assignment):
            # Assign the color to the current region
            color_assignment[current_region] = color
            print(color_assignment)
            
            # Recursively try to color the rest of the map
            result = solve_map_coloring(map, regions, colors, color_assignment)
            
            if result is not None:
                return result
            
            # If coloring fails, backtrack by removing the color assignment
            del color_assignment[current_region]
    
    # Return None if no valid coloring is found
    return None

if __name__ == "__main__":
    # Read the number of region
    map = {}
    regions = []
    num_regions = int(input("Enter the number of regions: "))
    
    # Read each region and its neighbors
    for _ in range(num_regions):
        region = input("Enter the name of the region: ")
        neighbors = input(f"Enter the neighbors of {region} (comma separated): ").split(',')
        map[region] = [neighbor.strip() for neighbor in neighbors]
        regions.append(region)
    
    # Read the available colors
    colors = input("Enter the available colors (comma separated): ").split(',')
    colors = [color.strip() for color in colors]
    
    # Solve the map coloring problem
    coloring = solve_map_coloring(map, regions, colors)
    
    # Print the result
    if coloring:
        print("\nValid coloring:")
        for region, color in coloring.items():
            print(f"{region}: {color}")
    else:
        print("No valid coloring found.") 