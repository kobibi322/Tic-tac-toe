from validations import validate_choice

# prints
def display_board(board):
    b = board
    print(f"""
 [1]{b[0]}| [2]{b[1]}| [3]{b[2]}
-------+-------+-------
 [4]{b[3]}| [5]{b[4]}| [6]{b[5]}
-------+-------+-------
 [7]{b[6]}| [8]{b[7]}| [9]{b[8]}
""")

def print_win_results(board, player):
        display_board(board)
        print(f"Player {player} wins!")

def print_draw_results(board):
    display_board(board)
    print("It's a draw!")

# input   
def input_player(player, board):
    choice = input(f"Player {player}, choose a cell (1-9):").strip()
    val = validate_choice(choice, board)
    return val

# logics
def turn_of(player)->str:
    if player == "O":
        return "X"
    return "O"

def is_winner(board, player):
    WINNING_LINES = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
            ]
    for line in WINNING_LINES:
        first, second, third = line
        if board[first].strip() == player and board[first].strip() == board[second].strip() and board[second].strip() == board[third].strip():
            return True