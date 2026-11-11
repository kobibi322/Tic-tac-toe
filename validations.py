def validate_choice(choice, board):
    try:
        val = int(choice)
    except ValueError:
        raise ValueError("choice is not integer")
    else:
        if val > 9 or val < 1:
            raise ValueError("must be 1-9")
        elif board[val-1] == "X" or board[val-1] == "O":
            raise ValueError("it's Taken")
    return val
