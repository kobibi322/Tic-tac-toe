from functions import (
    display_board, 
    print_win_results, 
    print_draw_results, 
    input_player, 
    turn_of, 
    is_winner
)

def manager():
    player = "X"
    board = [None] * 9
    board_to_show = ["   "] * 9
    for turn in range(9):
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