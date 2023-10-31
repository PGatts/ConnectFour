# Param Gattupalli
# COP 3502C Lab 5: Connect Four

def print_board(board):
    for row in board:
        for spot in row:
            print(spot, end = ' ')
        print()

def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append('-')
        board.append(row)
    return board

def insert_chip(board, col, chip_type):
    row = len(board) - 1
    while board[row][col] != '-':
        row -= 1

    board[row][col] = chip_type
    return row

def check_if_winner(board, col, row, chip_type):
    # Check if there are four in a row on the row
    right_matches, left_matches = 0, 0
    while col + right_matches < len(board[row]) and board[row][col + right_matches] == chip_type:
        right_matches += 1
    while col - left_matches >= 0 and board[row][col-left_matches] == chip_type:
        left_matches += 1
    if right_matches + left_matches - 2 >= 3:
        return True

    # Check if there are four in a row on the column
    down_matches = 0
    while row + down_matches < len(board) and board[row + down_matches][col] == chip_type:
        down_matches += 1
    if down_matches > 3:
        return True

    # Check if there are four in a row going diagonally
    
    # Return False if there is no winner
    return False

def main():
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows,num_cols)
    print_board(board)
    print('\nPlayer 1: x\nPlayer 2: o\n')

    chips_played, col, row, player = 0, 0, 0, False
    player_chip_dict = {1:'x', 2:'o'}
    bool_player_dict = {True:1, False:2}

    # Play game by adding chips until board if full or there is a winner
    while chips_played < num_rows * num_cols and not check_if_winner(board, col, row, player_chip_dict[bool_player_dict[player]]):
        player = not player
        print("Player " +  str(bool_player_dict[player]) + ": Which column would you like to choose?", end =' ')
        col = int(input())
        row = insert_chip(board, col, player_chip_dict[bool_player_dict[player]])
        print_board(board)
        print()
        chips_played += 1

    if chips_played >= num_rows * num_cols:
        print("Draw. Nobody wins.")
    else:
        print("Player", bool_player_dict[player], "won the game!")

if __name__ == '__main__':
    main()