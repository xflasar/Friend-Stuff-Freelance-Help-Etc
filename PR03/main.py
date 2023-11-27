#  
# Když se hra spustí, zeptá se zda chcete hrát sám, či odsimulovat hru, kde si můžete vybrat mezi jednou hrou a simulací tahů pole od 2 do 100. Dále si můžete vybrat zda chcete hrát s otraveným polem či nikoli.
# Minimální velikost pole je dva, tedy jen start a home.
# Maximální velikost pole není omezena ale pro velké počty (stovky) může hra trvat déle.
#

import random
import os

def roll_until_non_six(turn, sim, average_mode=False):
    total_dice_rolls = 0
    while True:
        dice_val = roll_die()
        if average_mode == False:
          print(f'You rolled this time: {dice_val}\n')

        total_dice_rolls += dice_val
        turn += 1
        if dice_val != 6:
            break

        if sim == False:
          input(f'Boring re-roll => SumRolls: {total_dice_rolls}. Press Enter to re-roll.\n')

    return [total_dice_rolls, turn]

def roll_die():
    return random.randint(1, 6)

def check_move(position, n, dice_val_turn, is_poisoned, sim, average_mode=False):
    next_hop = position + dice_val_turn[0][0] # document dice_val_turn - Worked like this having list in list -_-

    if next_hop > n:
        if sim == False:
          input('You overshot roll again. Press Enter to re-roll.\n')
        return check_move(position, n, [roll_until_non_six(dice_val_turn[0][1], sim, average_mode), dice_val_turn[0][1]], is_poisoned, sim, average_mode)
    else:
        if is_poisoned and next_hop != n and next_hop > 11:
          if check_poisoned(next_hop, average_mode):
            return [[-position + 1, dice_val_turn[0][1]],dice_val_turn[0][1]]

        return dice_val_turn

def move_piece(position, n, dice_val, is_poisoned):
    return position + dice_val

def draw_board(position, n, total_dice_rolls, turns):
    print(f'Turn: {turns} Throws: {total_dice_rolls}')
    board = ['.' for _ in range(n)]
    board[position - 1] = '#'
    print(' '.join(board))
    print(f'You moved to square {position}.\n')

def check_poisoned(position, average_mode=False):
    if (position) % 11 == 0:
      if average_mode == False:
        print('You landed on a poisoned square. You move back to start.')

      return True

    if average_mode == False:
      print('You landed on a non-poisoned square. You continue your turn.')

    return False

def check_board_size(n):
    if n < 2 or n > 120:
        return check_board_size(int(check_numeric_input(input(f'Board size must be at least 3 and maximum of 120. Please Enter number diferent than {n}.\n'))))

    return n

def check_input_true_false(sim):
    sim_lower = sim.lower()
    if sim_lower not in ['true', 'false']:
        return check_input_true_false(input('Input must be True or False. Please enter again.\n'))
    else:
        return sim_lower

def check_numeric_input(input_str):
    if input_str.isdigit():
        return int(input_str)
    else:
        return check_numeric_input(input('Input must be a numeric digit. Please enter again:\n'))

def check_win(position, n, turns):
    if position == n:
        print(f'Game finished in {turns} turns.')

def game(board, sim, average_mode=False, is_poisoned=False):
    position = 1
    turns = 0

    if board >= 13:
      if is_poisoned == False and average_mode == False and sim == False:
        is_poisoned = check_input_true_false(input('Do you want to play with poisoned tiles? (True/False)\n'))
        if is_poisoned.lower() == 'true':
          is_poisoned = True
        else:
          is_poisoned = False

        print(f'You chose {is_poisoned} for poisoned tiles.')

    while position < board:
        if sim == False:
          input('Press Enter to roll a dice.') # Optional if we want user interaction but ofc we need to slow game down (delay)

        total_dice_rolls = 0
        if sim == False:
          os.system('cls') # Used for clearing screen between runs ## Power hungry
          total_dice_rolls = check_move(position, board, [roll_until_non_six(turns, False), turns], is_poisoned, False)
        elif average_mode:
          total_dice_rolls = check_move(position, board, [roll_until_non_six(turns, True, True), turns], is_poisoned, True, True)
        else:
          total_dice_rolls = check_move(position, board, [roll_until_non_six(turns, True), turns], is_poisoned, True)
        
        turns = total_dice_rolls[0][1]
        position = move_piece(position, board, total_dice_rolls[0][0], is_poisoned)
        
        if average_mode == False:
          # Print the game board
          draw_board(position, board, abs(total_dice_rolls[0][0]), turns)
          check_win(position, board, turns)

    if average_mode:
        return turns
    


def main():
    sim = check_input_true_false(input('Do you want to Simulate or Self-play the Game? (True for simulate/False for self-play) => Simulation\n'))
    if sim.lower() == 'true':
      sim = True
    else:
      sim = False

    average_mode = False
    is_poisoned = False
    n = 0

    if sim:
      average_mode = check_input_true_false(input('Do you want to simulate only one game or average time of games ranging from 2 to 100 tiles? (True for one game/False for average time) => Average Mode\n'))
      if average_mode.lower() == 'true':
        average_mode = True
      else:
        average_mode = False

      if average_mode == False:
        n = check_board_size(int(check_numeric_input(input('Please enter the board size: '))))
      
      if n >= 13 or average_mode == True:
        is_poisoned = check_input_true_false(input('Do you want to use poisoned tiles in average-simulation? (True/False)\n'))
        if is_poisoned.lower() == 'true':
          is_poisoned = True
        else:
          is_poisoned = False

      average_mode_turns = []
      average_mode_min = 2
      average_mode_max = 100
    else:
      n = check_board_size(int(check_numeric_input(input('Please enter the board size: '))))
    

    if average_mode:
      print('Average Mode')
      print(f'Simulating {average_mode_min} to {average_mode_max} board sizes.')
      print('Please wait...')
      
      for i in range(average_mode_min, average_mode_max + 1):
        average_mode_turns.append(game(i, True, True, is_poisoned))
        os.system('cls') # Power hungry
        print(f'Completed {i} from {average_mode_max}.')

      print(f'Average Mode Turns: {round(sum(average_mode_turns)/len(average_mode_turns), 2)}')
    else:
      game(n, sim, False)

if __name__ == '__main__':
    main()