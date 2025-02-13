def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*9)

def check_winner(board , player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
    all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False