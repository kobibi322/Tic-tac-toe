def validate_choice(choice: str, board: list):
    if not choice.isdigit():
        raise ValueError("Choice is not an integer")
    val = int(choice)
    if not (1 <= val <= 9):
        raise ValueError("Must be between 1 and 9")
    if board[val - 1] is not None:
        raise ValueError("It's already taken")
    return val
