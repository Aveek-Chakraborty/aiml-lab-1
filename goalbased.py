def clean(floor):
    row, col = len(floor), len(floor[0])
    for i in range(row):
        if i % 2 == 0:
            print("Moving RIGHT")
            for j in range(col):
                if floor[i][j] == 1:
                    print_F(floor, i, j)
                    floor[i][j] = 0
                    print_F(floor, i, j)
        else:
            print("Moving LEFT")
            for j in range(col-1, -1, -1):
                if floor[i][j] == 1:
                    print_F(floor, i, j)
                    floor[i][j] = 0
                    print_F(floor, i, j)
        if i < row - 1:
            print("Moving DOWN")

def print_F(floor, row, col):
    print("The Floor matrix is as below:")
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            if r == row and c == col:
                print(f" >{floor[r][c]}< ", end='')
            else:
                print(f" {floor[r][c]} ", end='')
        print()
    print()

# Setup the floor matrix
floor = []
m = int(input("Enter the No. of Rows: "))
n = int(input("Enter the No. of Columns: "))
print("Enter clean status for each cell (1 - dirty, 0 - clean)")
for i in range(m):
    f = list(map(int, input().split()))
    floor.append(f)
print()

# Clean the floor
clean(floor)
