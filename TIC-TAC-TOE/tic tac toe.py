"""TIC-TAC-TOE-GAME"""

import random

def print_grid(grid):
    for i in range(0, 9, 3):
        print(" | ".join(grid[i:i+3]))
        if i < 6:
            print("-" * 9)

def find_winner(grid, person):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if all(cell == person for cell in grid[i:i+3]):
            return True

    for i in range(3):
        if all(grid[j] == person for j in range(i, 9, 3)):
            return True

    if all(grid[i] == person for i in range(0, 9, 4)) or all(grid[i] == person for i in range(2, 7, 2)):
        return True

    return False

def is_grid_full(grid):
    return all(cell != ' ' for cell in grid)

def person_move(grid):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9 and grid[move - 1] == ' ':
                return move
            else:
                print("Invalid move.Please Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 to 9.")

def computer_move(grid):
    empty_cells = [i for i in range(9) if grid[i] == ' ']
    return random.choice(empty_cells) + 1

def tic_tac_toe():
    grid = [' ' for _ in range(9)]
    current_person = 'X'

    while True:
        print_grid(grid)

        if current_person == 'X':
            move = person_move(grid)
        else:
            print("Computer's move:")
            move = computer_move(grid)

        grid[move - 1] = current_person
    

        if find_winner(grid, current_person):
            print_grid(grid)
            print(f"{current_person} \U0001f604 wins!")
            break

        if is_grid_full(grid):
            print_grid(grid)
            print("It's a tie \U0001f603 !")
            break

        if current_person == 'X':
            current_person = 'O'
        else:
            current_person = 'X'

if __name__ == "__main__":
    tic_tac_toe()
