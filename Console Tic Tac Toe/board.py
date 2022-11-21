# Nathaniel Schainblatt
# July, 11, 2022
# This program creates a tic-tac-toe game for 2 players and determines the winner or draw.
import sqlite3
import random


def main():
    print("Printing board...")
    game_board = [['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']]
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])
    current = game_board
    while True:
        # Player 1
        player1(game_board, current)
        # Player 2
        player2(game_board, current)


def player1(game_board, current):
    player = 1
    print("Player 1, make your move")
    row = int(input("Enter row nos (0-2): "))
    col = int(input("Enter col nos (0-2): "))

    # row and col validation
    while row < 0 or row >= 3 or col < 0 or col >= 3:
        print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
        print_board(current)
        print()
        print("Player 1, make your move")
        row = int(input("Enter row nos (0-2): "))
        col = int(input("Enter col nos (0-2): "))

    taken = check_existing(row, col, game_board)

    while taken:
        print(f"**** Board [{row}][{col}] has already been selected. Please somewhere else on the board ****")
        print("**** Invalid choice. Please mark again! ****")
        print_board(current)
        print()
        print("Player 1, make your move")
        row = int(input("Enter row nos (0-2): "))
        col = int(input("Enter col nos (0-2): "))
        while row < 0 or row >= 3 or col < 0 or col >= 3:
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
            print_board(current)
            print()
            print("Player 1, make your move")
            row = int(input("Enter row nos (0-2): "))
            col = int(input("Enter col nos (0-2): "))
        taken = check_existing(row, col, game_board)

    print()
    print(f"Player 1 added mark at the location {row}, {col}")
    current = board_changes(player, row, col, game_board)
    print_board(current)
    print()


def player2(game_board, current):
    player = 2
    row = random.randint(1, 2)
    col = random.randint(1, 2)
    check = check_ai(row, col, game_board)
    while check:
        row = random.randint(1, 2)
        col = random.randint(1, 2)
        check = check_ai(row, col, game_board)
    print()
    print(f"Player 2 added mark at the location {row}, {col}")
    current = board_changes(player, row, col, game_board)
    print_board(current)
    print()


def check_existing(r, c, b):
    if b[r][c] == 'X' or b[r][c] == 'O':
        return True
    else:
        return False


def check_ai(r, c, b):
    if b[r][c] == 'X' or b[r][c] == 'O':
        return True
    else:
        return False


def board_changes(p, r, c, b):
    if p == 1:
        b[r][c] = 'X'
    if p == 2:
        b[r][c] = 'O'
    winner(b)
    return b


def print_board(b):
    print("Printing board...")
    print(b[0])
    print(b[1])
    print(b[2])


def winner(board):
    overall_winner = ""
    # Checking Horizontal
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and \
            board[1][2] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print_board(board)
        print("Player 1 wins!")
        overall_winner = "Player 1"
        database(overall_winner, board)

    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or board[1][0] == 'O' and board[1][
        1] == 'O' and board[1][2] == 'O' or board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        print_board(board)
        print("Player 2 wins!")
        overall_winner = "Player 2"
        database(overall_winner, board)

    # Checking Vertical
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][1] == 'X' and board[1][
        1] == 'X' and board[2][1] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print_board(board)
        print("Player 1 wins!")
        overall_winner = "Player 1"
        database(overall_winner, board)

    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or board[0][1] == 'O' and board[1][
        1] == 'O' and board[2][1] == 'O' or board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print_board(board)
        print("Player 2 wins!")
        overall_winner = "Player 2"
        database(overall_winner, board)

    # Checking Diagonal
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][
        1] == 'X' and board[2][0] == 'X':
        print_board(board)
        print("Player 1 wins!")
        overall_winner = "Player 1"
        database(overall_winner, board)

    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or board[0][2] == 'O' and board[1][
        1] == 'O' and board[2][0] == 'O':
        print_board(board)
        print("Player 2 wins!")
        overall_winner = "Player 2"
        database(overall_winner, board)

    # Nobody wins
    elif board[0][0] != '-' and board[0][1] != '-' and board[0][2] != '-' and board[1][0] != '-' and board[1][
        1] != '-' and board[1][2] != '-' and board[2][0] != '-' and board[2][1] != '-' and board[2][2] != '-':
        print_board(board)
        print("Nobody wins!")
        overall_winner = "Nobody  "
        database(overall_winner, board)


def database(win, b):
    connection = sqlite3.connect('score_data.db')
    cursor = connection.cursor()
    print("Successfully connected to SQLite!")

    cursor.execute('''CREATE TABLE IF NOT EXISTS Scores (Winner TEXT, Board)''')
    cursor.execute(f'''INSERT INTO Scores Values("{win}", "{b[0]}")''')
    cursor.execute(f'''INSERT INTO Scores Values("        ", "{b[1]}")''')
    cursor.execute(f'''INSERT INTO Scores Values("        ", "{b[2]}")''')

    connection.commit()
    print("Record inserted successfully into Scores Table")
    connection.close()
    exit()


main()
