def print_board(board):  # Prints the board in the correct order by reversing the 2d list.
    for i in reversed(range(len(board))):
        print(" ".join(board[i]))


def initialize_board(num_rows, num_cols):  # Initializes the board.
    board = [["-"] * num_cols for _ in range(num_rows)]  # Initially used two (*). Gave me a headache.
    return board


def insert_chip(board, col, chip_type):  # Inserts a chip at the lowest spot in the desired colum.
    for row in range(len(board)):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row


def check_if_winner(board, col, row, chip_type):  # Checks if there is a winner.
    won = False
    recurring = 1
    for i in range(len(board[row])-1):  # Checks horizontal.
        if board[row][i+1] == board[row][i] and board[row][i] == chip_type:
            recurring += 1
        else:
            recurring = 1
        if recurring == 4:
            won = True
            break
    if won:
        return won
    recurring = 1
    for i in range(len(board)-1):  # Checks vertical.
        if board[i+1][col] == board[i][col] and board[i][col] == chip_type:
            recurring += 1
        else:
            recurring = 1
        if recurring == 4:
            won = True
            break
    return won


def main():   # Prints menu and calls initial functions.
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    board = initialize_board(height, length)
    print_board(board)
    print("\nPlayer 1: x\nPlayer 2: o")

    count = 0
    winner = False
    even = False
    while not winner:  # Main loop for the game.
        count += 1
        even = not even
        col = int(input(f"Player {'1' if even else '2'}: Which column would you like to choose? "))
        winner = check_if_winner(board, col, insert_chip(board, col, ("x" if even else "o")), ("x" if even else "o"))
        print_board(board)
        if winner:
            print(f"\nPlayer {'1' if even else '2'} won the game!")
        elif count == (length*height):  # Checks for draw.
            print("\nDraw. Nobody wins.")
            winner = True


if __name__ == "__main__":
    main()
