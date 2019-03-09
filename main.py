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
            door_display += f"| {doors[door_num].title()} | "
        else:
            door_display += f"| Door {door_num + 1} | "
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


def reveal_results(doors: list, selected_door_num: int):
    result = "Win!" if doors[selected_door_num] == 'car' else "Lose."
    print('')
    print(f"Your choice: {selected_door_num + 1}, {doors[selected_door_num].title()}")
    print(f"Result: {result}")
    print('')


def game():
    # Set up and display initial game board
    doors = set_doors()
    print(display_doors(doors))
    # Allow player to select a door
    player_choice = select_door(doors)
    # Reveal all unselected goat doors and display new game board
    goat_door_nums = reveal_goat(doors, selected_door=player_choice)
    print(display_doors(doors, revealed_door_nums=goat_door_nums))
    # Allow player to swap to the last unrevealed door
    player_choice = offer_swap(doors, player_choice, goat_door_nums)
    # Display results of game
    print(display_doors(doors, revealed_door_nums=list(range(len(doors)))))
    reveal_results(doors, player_choice)


if __name__ == '__main__':
    playAgain = True
    while playAgain:
        game()
        while True:
            playAgain = input("Play again? [y/n]\n> ")
            if playAgain in ['y', 'n']:
                if playAgain == 'y':
                    playAgain = True
                else:
                    playAgain = False
                break
            else:
                print("Please select a valid option. [y/n]")
