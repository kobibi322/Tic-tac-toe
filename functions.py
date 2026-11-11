from validations import validate_choice

# prints
def display_board(board_to_show: list):
    b = board_to_show
    print(f"""
 [1]{b[0]}| [2]{b[1]}| [3]{b[2]}
-------+-------+-------
 [4]{b[3]}| [5]{b[4]}| [6]{b[5]}
-------+-------+-------
 [7]{b[6]}| [8]{b[7]}| [9]{b[8]}
""")

def print_win_results(board_to_show: list, player: str):
        display_board(board_to_show)
        print(f"Player {player} wins!")

def print_draw_results(board_to_show: list):
    display_board(board_to_show)
    print("It's a draw!")

# input   
def input_player(player: str, board: list) -> int:
    choice = input(f"Player {player}, choose a cell (1-9):").strip()
    return validate_choice(choice, board)

# logics
def turn_of(player: str) -> str:
    if player == "O":
        return "X"
    return "O"

def is_winner(board: list, player: str) -> bool:
    WINNING_LINES = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
            ]
    for first, second, third in WINNING_LINES:
        if board[first] == board[second] == board[third] == player:
            return True