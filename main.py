# Module for randomly generating numbers
import random

# Greeting message
print('********************************************\n'
      '\tWELCOME TO THE ROLLING DICE GAME\n'
      '********************************************\n')

# Function to display game rules
def display_game_rules():
    """
    This function prints the rules of the Rolling Dice Game.
    """
    print("\nGAME RULES:\n"
          "1. A toss (head or tail) decides who plays first. The winner of the toss always gets the first turn.\n"
          "2. Each player rolls the dice on their turn.\n"
          "3. Rolling a '1': Subtract 2 points from the player's score.\n"
          "4. Rolling a '6': Add 6 points for the roll + 2 bonus points (total: 8 points).\n"
          "5. Rolling '2, 3, 4, or 5': Add the rolled number to the player's score.\n"
          "6. The first player to reach the target score (e.g., 20) wins the game!\n")

# Function to play the game
def play_game():
    """
    This function contains the main logic for the Rolling Dice Game.
    """
    # Initialize scores and score histories
    computer_total_score = 0
    player_total_score = 0
    computer_score_history = []
    player_score_history = []

    # Toss logic
    coin_sides = ['Head', 'Tail']
    user_toss_choice = input('\n*************\tTOSS\t*************\n'
                             'Who gets the first turn to roll the dice?\nChoose Head or Tail: ').lower()
    toss_result = random.choice(coin_sides).lower()
    if user_toss_choice == toss_result:
        print(f'\nYou chose {user_toss_choice}, and it is {toss_result}.\nYou will roll the dice first.\n')
        turn = 'player'
    else:
        print(f'\nYou chose {user_toss_choice}, and it is {toss_result}.\nThe computer will roll the dice first.\n')
        turn = 'computer'

    # Main game loop
    while computer_total_score < 20 and player_total_score < 20:
        if turn == 'player':
            input('\nPress R to roll the dice: ').lower()
            player_roll = random.randint(1, 6)

            # Player score logic
            if player_roll == 1:
                player_total_score -= 2
            elif player_roll == 6:
                player_total_score += 8
            else:
                player_total_score += player_roll

            # Record player score after the roll
            player_score_history.append(player_total_score)
            print(f'You rolled a {player_roll}.\nYour current score: {player_total_score}\n')
            turn = 'computer'

        elif turn == 'computer':
            computer_roll = random.randint(1, 6)

            # Computer score logic
            if computer_roll == 1:
                computer_total_score -= 2
            elif computer_roll == 6:
                computer_total_score += 8
            else:
                computer_total_score += computer_roll

            # Record computer score after the roll
            computer_score_history.append(computer_total_score)
            print(f'The computer rolled a {computer_roll}.\nIts current score: {computer_total_score}\n')
            turn = 'player'

        # Score comparison
        print(f'Your score: {player_total_score} | Computer score: {computer_total_score}\n')

    # Game result
    print(f'\nYour score history: {player_score_history}')
    print(f'Computer score history: {computer_score_history}')

    if player_total_score >= 20:
        print(f'\nCongratulations! You win with a score of {player_total_score}.\n')
    else:
        print(f'\nBetter luck next time! The computer wins with a score of {computer_total_score}.\n')

# Main menu
while True:
    choice = input('1. Press P to Play Game (or press 1)\n'
                   '2. Press R to Read Game Rules (or press 2)\n'
                   '3. Press E to Exit the Game (or press 3)\n\n'
                   'Enter your choice (P/R/E or 1/2/3): ').lower()
    if choice in ['r', '2']:
        display_game_rules()
    elif choice in ['p', '1']:
        play_game()
    elif choice in ['e', '3']:
        print('You have exited the game. See you next time!\nTHANK YOU :)')
        break
    else:
        print('Invalid input. Please enter a valid option.\n')