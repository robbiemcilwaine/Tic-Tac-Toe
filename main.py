import random

board = """
 | | 
-*-*-
 | | 
-*-*-
 | | 
"""

numbers = ['1', '2', '3']

board_points = {'1, 1': 1, '1, 2': 3, '1, 3': 5, '2, 1': 13, '2, 2': 15,
                '2, 3': 17, '3, 1': 25, '3, 2': 27, '3, 3': 29}

winning_positions = [[1, 3, 5], [13, 15, 17], [25, 27, 29], [1, 13, 25],
                     [3, 15, 27], [5, 17, 29], [1, 15, 29], [5, 15, 25]]

user_moves_array = []

opponent_moves_array = []

game_end = False
user_result = False
opponent_result = False

while not game_end:

    # break the loop if either the user/opponent has won, printing message
    if user_result:
        game_end = True
        print("You win!")
        break
    elif opponent_result:
        game_end = True
        print("You lose!")
        break

    # check if the opponents X's are in any of the winning positions
    opponent_result = any(all(value in opponent_moves_array for value in subarray) for subarray in winning_positions)

    # get input from user, then place the letter on the correct position based off of this
    if not opponent_result:
        user_move = str(input("Please input a row and column (row, column): "))
    else:
        game_end = True
        print("You lose!")
        continue

    move_check = []
    # check if characters are valid numbers, and add to move_check array
    for character in user_move:
        if character not in numbers:
            continue
        else:
            move_check.append(character)

    user_move = f"{move_check[0]}, {move_check[-1]}"

    # format for dictionary retrieval
    user_row, user_column = user_move.split(', ')
    user_key = f"{user_row}, {user_column}"

    # check if user has provided valid input, then retrieve the index from dictionary and add this to array
    if user_key:
        user_index = board_points[user_key]
        user_moves_array.append(user_index)
    else:
        print("Invalid input.")
        continue

    # split user input into row and column
    # user_row, user_column = user_move.split(', ')
    # user_key = f"{user_row}, {user_column}"

    # check if the key exists in board_points
    if user_key in board_points:
        user_index = board_points[user_key]
        user_moves_array.append(user_index)
        board = board[:board_points[user_move]] + 'O' + board[board_points[user_move] + 1:]
        del board_points[user_key]
    else:
        print("Invalid input.")
        continue

    print(f'\nUsers move:\n{board}')

    # check if the users O's are in any of the winning positions
    user_result = any(all(value in user_moves_array for value in subarray) for subarray in winning_positions)

    # use random library to generate the opponents move randomly from the indices
    # split the move and put it back together w/ f string so that it is formatted properly for later retrieval
    opponent_move = random.choice(list(board_points))
    opponent_row, opponent_column = opponent_move.split(', ')
    opponent_key = f"{opponent_row}, {opponent_column}"

    if opponent_key in board_points and not user_result:
        opponent_index = board_points[opponent_key]
        opponent_moves_array.append(opponent_index)
        board = board[:opponent_index] + 'X' + board[opponent_index + 1:]
        del board_points[opponent_key]
    elif user_result:
        continue
    else:
        print("Invalid input.")
        continue

    print(f"\nOpponent's move:\n{board}")
