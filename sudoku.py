board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Check if valid position
def valid(board,num,pos):
    # Check row
    for i in range(len(board[0])):
        # Check row passed from findEmpty (which is i in the tuple),
        # pos[1] != i to check if it's not the element we just inserted
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3 # Column
    box_y = pos[0] // 3 # Row

    # Now we have the box we are looking at
    # Checking in specific box
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 +3):
            if board[i][j] == num and (i, j) != pos:
                # Find duplicate
                return False


    return True

def solve(board):
    # Get coords of empty spot
    find = findEmpty(board)    

    # Found solution
    if not find:
        return True
    # If not found solution
    else:
        row, col = find

    for i in range(1,10):
        # //Insert into board
        if valid(board, i, (row, col)):
            board[row][col] = i

            if (solve(board) is True):
                return True

            # Reset if fail
            board[row][col] = 0

    return False



def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - - -")
    
        # Gets length of rows
        for j in range(len(board[0])):
            # If it's 3rd or 6th element, print "|"
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # No newline

            # Print normally if last, and add newline
            if j == 8:
                print (board[i][j])
            else:
                # Adds space between numbers
                print(str(board[i][j]) + " ", end="")


# Find empty square
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column 

    return None

printBoard(board)
solve(board)
print("__________________")
printBoard(board)
