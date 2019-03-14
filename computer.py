import random
import main


def swap_doors(door_nums, selected_door_num, revealed_door_nums):
    revealed_door_nums.append(selected_door_num - 1)
    door_nums = list(range(len(door_nums)))
    # Converting lists to sets makes it possible to get the difference between them
    available_door_num = int(list(set(door_nums) - set(revealed_door_nums))[0])
    return available_door_num


def auto_play(num_doors, rounds, wins, losses):
    # Set up and display initial game board
    print(f"{'=' * 18}Round {rounds}{'=' * 18}")
    doors = main.set_doors(num_doors)
    print(main.display_doors(doors), end="\n\n")
    # Computer guesses a random door
    player_first_choice = random.randint(0, len(doors) - 1)
    # Reveal all unselected goat doors and display new game board
    goat_door_nums = main.reveal_goat(doors, selected_door=player_first_choice)
    print(main.display_doors(doors, revealed_door_nums=goat_door_nums), end="\n\n")
    # Allow player to swap to the last unrevealed door
    player_second_choice = swap_doors(doors, player_first_choice, goat_door_nums)
    # Display results of game
    print(main.display_doors(doors, revealed_door_nums=list(range(len(doors)))), end="\n\n")
    results = main.reveal_results(doors, player_second_choice, doors, rounds, wins, losses)
    print(f"\nFirst Choice: |Door {player_first_choice + 1}, {doors[player_first_choice]}|\n\n{results[0]}")
    return [results[1], results[2]]


def start():
    num_rounds = int(input("How many rounds?\n> "))
    while True:
        num_doors = int(input("How many doors? (min 3)\n> "))
        if num_doors < 3:
            continue
        else:
            break
    current_round = 0
    wins = 0
    losses = 0
    while num_rounds > 0:
        current_round += 1
        print('')
        score = auto_play(num_doors, current_round, wins, losses)
        wins = score[0]
        losses = score[1]
        num_rounds -= 1


if __name__ == '__main__':
    start()
