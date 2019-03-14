import random


# Set up the doors. Default is 3
def set_doors(num_doors: int = 3) -> list:
    doors = []
    # Determine prize door
    prize_door = random.randint(0, num_doors-1)
    # Set doors
    for num in range(num_doors):
        if num == prize_door:
            doors.append('car')
        else:
            doors.append('goat')
    return doors


# Show doors, revealing the specified door
def display_doors(doors: list, revealed_door_nums: list = []) -> str:
    door_display = ''
    for door_num in range(len(doors)):
        if door_num in revealed_door_nums:
            door_prize = doors[door_num].title()
            if len(revealed_door_nums) < len(doors):
                door_display += f"|{' . '}{door_prize}{' . '}| "
            else:
                door_display += f"| {door_prize}{'  ' if door_prize == 'Car' else ' '}| "
        else:
            door_display += f"| Door {door_num + 1:03} | "
        if (door_num + 1) % 10 == 0:
            door_display = door_display[:-1] + "\n"
    return door_display


# Player selects a door. If played by bot, selection can instead by passed.
def select_door(doors: list, selection: int = None) -> int:
    if not selection:
        while True:
            try:
                selection = input(f"Pick a door number (1-{len(doors)}):\n> ")
                selection = int(selection)

                if 0 < selection <= len(doors):
                    break
                else:
                    print(f"Please select an available door (1-{len(doors)})")
            except ValueError:
                print("Please select a number only.")
    else:
        pass
    return selection


# Determine the goat door to show
def reveal_goat(doors: list, selected_door: int) -> list:
    goat_doors = []
    for door in range(len(doors)):
        if (door + 1) != selected_door and doors[door] != 'car':
            goat_doors.append(door)
    if len(goat_doors) == len(doors) - 1:
        remove_door = random.randint(0,len(goat_doors)-1)
        goat_doors.pop(remove_door)
    return goat_doors


# Let the player swap doors if they want
def offer_swap(doors: list, selected_door_num: int, revealed_door_nums: list):
    revealed_door_nums.append(selected_door_num - 1)
    door_nums = list(range(len(doors)))
    # Converting lists to sets makes it possible to get the difference between them
    available_door_num = int(list(set(door_nums) - set(revealed_door_nums))[0])
    while True:
        swap_door = input(f"Would you like to swap to Door {available_door_num + 1}? [y/n]\n> ")
        if swap_door.lower() in ['y', 'n']:
            break
        else:
            print("Please select a valid option.")
    if swap_door.lower() == 'y':
        selected_door_num = available_door_num
    return selected_door_num


def reveal_results(doors: list,
                   selected_door_num: int,
                   doors_list: list,
                   num_rounds: int,
                   num_wins: int,
                   num_losses: int) -> list:
    result = "win" if doors[selected_door_num] == 'car' else "lose"
    if result == 'win':
        num_wins += 1
    else:
        num_losses += 1
    player_door = f"Your door:    |Door {selected_door_num + 1}, {doors[selected_door_num].title()}|"
    winning_door = f"Winning door: |Door {doors_list.index('car') + 1}, Car|"
    score = f"Total Rounds: {num_rounds}\n" \
        f"Wins: {num_wins} {(num_wins / num_rounds) * 100}%\n" \
        f"Losses: {num_losses} {(num_losses / num_rounds) * 100}%"
    results_screen = f"{player_door}\n{winning_door}\n\nResult: {result.title()}!\n\n{score}"
    return [results_screen, num_wins, num_losses]


def game(rounds: int, wins: int, losses: int, num_doors: int) -> list:
    # Set up and display initial game board
    print(f"{'='*18}Round {rounds}{'='*18}")
    doors = set_doors(num_doors)
    print(display_doors(doors), end="\n\n")
    # Allow player to select a door
    player_choice = select_door(doors)
    # Reveal all unselected goat doors and display new game board
    goat_door_nums = reveal_goat(doors, selected_door=player_choice)
    print(display_doors(doors, revealed_door_nums=goat_door_nums))
    # Allow player to swap to the last unrevealed door
    player_choice = offer_swap(doors, player_choice, goat_door_nums)
    # Display results of game
    print(display_doors(doors, revealed_door_nums=list(range(len(doors)))))
    results = reveal_results(doors, player_choice, doors, rounds, wins, losses)
    print(results[0])
    return [results[1], results[2]]


def main():
    while True:
        num_doors = int(input("How many doors? (min 3)\n> "))
        if num_doors < 3:
            continue
        else:
            break
    rounds = 0
    wins = 0
    losses = 0
    play_again = True
    while play_again:
        rounds += 1
        score = game(num_doors, rounds, wins, losses)
        wins = score[0]
        losses = score[1]
        while True:
            continue_game = input("Play again? [y/n]\n> ").lower()
            if continue_game not in ['y', 'n']:
                print("Please select a valid option. [y/n]")
                continue
            else:
                play_again = True if continue_game == 'y' else False
                break


if __name__ == '__main__':
    main()
