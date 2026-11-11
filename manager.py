from functions import *

def manager():
    player = "X"
    board = [None, None, None, None, None, None, None, None, None]
    board_to_show = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    for i in range(len(board)):
        finish = False
        while not finish:
            display_board(board_to_show)
            try:
                choice = input_player(player, board)    
            except ValueError as e:
                print(f"{e} try again")
            else:
                board_to_show[choice-1] = f" {player} "
                board[choice-1] = player
                finish = True 
        if is_winner(board, player): 
            print_win_results(board_to_show,  player)
            return
        player = turn_of(player)
    print_draw_results(board_to_show)