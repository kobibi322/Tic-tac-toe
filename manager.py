from functions import *

def manager():
    player = "X"
    board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    for i in range(len(board)):
        finish = False
        while not finish:
            display_board(board)
            try:
                choice = input_player(player, board)    
            except ValueError as e:
                print(f"{e} try again")
            else:
                board[choice-1] = f" {player} "
                finish = True 
        if is_winner(board, player): 
            print_win_results(board,  player)
            return
        player = turn_of(player)
    print_draw_results(board)