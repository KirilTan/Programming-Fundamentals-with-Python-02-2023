def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == 1 for j in range(3)):
            return "First player won"
        elif all(board[j][i] == 1 for j in range(3)):
            return "First player won"
        elif all(board[i][j] == 2 for j in range(3)):
            return "Second player won"
        elif all(board[j][i] == 2 for j in range(3)):
            return "Second player won"

    # Check diagonals
    if all(board[i][i] == 1 for i in range(3)):
        return "First player won"
    elif all(board[i][2 - i] == 1 for i in range(3)):
        return "First player won"
    elif all(board[i][i] == 2 for i in range(3)):
        return "Second player won"
    elif all(board[i][2 - i] == 2 for i in range(3)):
        return "Second player won"

    return "Draw!"


# Input
board = [list(map(int, input().split())) for _ in range(3)]

# Output
result = check_winner(board)
print(result)

