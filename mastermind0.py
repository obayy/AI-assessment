import random
import itertools

secret = []
letters = ["A", "B", "C", "D", "E", "F"]
board = [["X" for x in range(4)] for y in range(10)]
turn = 0
vs_computer = True
all_combinations = sorted(list(itertools.product("ABCDEF", repeat=4)))
algorithm = 0


def guess():
    letters_combinations = sorted(list(itertools.product("ABCDEF", repeat=4)))
    return random.sample(letters_combinations, k=1)


def check_answer(question, key):
    black = 0
    white = 0
    visited_guess = []
    visited_secret = []

    for index in range(len(key)):
        if question[index] == key[index]:
            visited_guess.append(index)
            visited_secret.append(index)
            black += 1

    for index in range(len(key)):
        for secret_index in range(len(key)):
            if question[index] == key[secret_index] and secret_index not in visited_secret and index not in visited_guess:
                visited_guess.append(index)
                visited_secret.append(secret_index)
                white += 1

    return (black, white)


def show_gameplay():
    for y in board:
        print(y)


def input_move():
    move = input("\nInput 4 colors: ").upper().split()
    for letter in move:
        if len(move) != 4 or letter not in letters:
            return input_move()
    return move


def game_loop():
    global turn
    current_move = input_move()
    board[turn] = current_move
    pins = check_answer(current_move, secret)
    show_gameplay()
    print(f"You have {pins[0]} red pin(s) and {pins[1]} white pin(s).")
    turn += 1
    if turn == 10 or board[turn - 1] == secret:
        print("The game is over!")
        exit()


def game_loop2():
    global turn

    if algorithm == 0:
        current_move = simple(all_combinations[0])
    elif algorithm == 1:
        current_move = worst()
    elif algorithm == 2:
        current_move = heuristic()

    board[turn] = current_move
    turn += 1
    print("The computer guessed: ", list(board[turn - 1]))
    if turn == 10 or list(board[turn - 1]) == secret:
        print("The game is over!")
        exit()


def simple(move_to_do):
    global secret
    new_all_combinations = []
    new_all_combinations.extend(all_combinations)
    move = move_to_do
    feedback = check_answer(move, secret)

    for combination in new_all_combinations:
        if check_answer(move, combination) != feedback:
            all_combinations.remove(combination)

    return move


def heuristic():
    return None


def worst():
    possible_combinations = {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}}
    question_combinations = [['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'B'], ['A', 'A', 'B', 'B'], ['A', 'A', 'B', 'C'],
                             ['A', 'B', 'C', 'D']]

    for com_ind in range(len(question_combinations)):
        for color_index in range(len(all_combinations)):
            if str(check_answer(question_combinations[com_ind], all_combinations[color_index])) \
                    not in possible_combinations[str(com_ind)]:
                possible_combinations[str(com_ind)][str(check_answer(question_combinations[com_ind],
                                                                     all_combinations[color_index]))] = 1
            else:
                possible_combinations[str(com_ind)][str(check_answer(question_combinations[com_ind],
                                                                     all_combinations[color_index]))] += 1

    largest_partition = [0, 0, 0, 0, 0]
    for combo in possible_combinations:
        for possibility in possible_combinations[combo]:
            if possible_combinations[combo][possibility] > largest_partition[int(combo)]:
                largest_partition[int(combo)] = possible_combinations[combo][possibility]

    if largest_partition.index(min(largest_partition)) == 0:
        return simple(all_combinations[0])
    else:
        return simple(question_combinations[largest_partition.index(min(largest_partition))])


if not vs_computer:
    secret = guess()

else:
    secret = input_move()


print("-------------------------------------------")
print("Rule: differentiate the letters with spaces!")
print("-------------------------------------------")


while True:
    if not vs_computer:
        game_loop()
    else:
        game_loop2()

