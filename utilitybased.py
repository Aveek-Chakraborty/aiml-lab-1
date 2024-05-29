def clean(floor):
    row, col = len(floor), len(floor[0])
    # Create a list of all dirty cells with their coordinates and dirt level (utility)
    dirty_cells = [(i, j, floor[i][j]) for i in range(row) for j in range(col) if floor[i][j] > 0]
    # Sort dirty cells by their utility (dirt level) in descending order
    dirty_cells.sort(key=lambda x: x[2], reverse=True)
    
    while dirty_cells:
        # Get the dirtiest cell with the highest utility
        i, j, dirt = dirty_cells.pop(0)
        print(f"Moving to cell ({i}, {j}) with dirt level {dirt}")
        # Print floor state before cleaning the current cell
        print_F(floor, i, j)
        # Clean the cell
        floor[i][j] = 0
        # Print floor state after cleaning the current cell
        print_F(floor, i, j)

def print_F(floor, row, col):
    print("The Floor matrix is as below:")
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            if r == row and c == col:
                # Highlight the current cell being cleaned
                print(f" >{floor[r][c]}< ", end='')
            else:
                print(f" {floor[r][c]} ", end='')
        print()
    print()

# Directly handle input and run the cleaning process
floor = []
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
print("Enter dirt level for each cell (0 for clean, 1-5 for dirty level)")
for i in range(m):
    # Read each row's dirt levels
    f = list(map(int, input().split()))
    floor.append(f)
print()
# Start the cleaning process
clean(floor)
