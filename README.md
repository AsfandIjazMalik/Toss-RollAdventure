# Toss-RollAdventure
Python Programming 

# Rolling Dice Game 🎲
A fun and interactive Python-based game where players compete against a computer to roll dice, accumulate scores, and win by reaching the target score first. The game includes dynamic rules, real-time decision-making, and a toss to decide the turn order. <br>
## Features
- **Toss to Decide Turn Order**: A virtual coin toss (Head/Tail) determines who rolls first. <br>
- **Interactive Gameplay**: Players roll dice and earn or lose points based on their results. <br>
- **Dynamic Scoring Rules**:<br>
  - Roll a `1`: Subtract 2 points from the score. <br>
  - Roll a `6`: Add 6 points plus 2 bonus points (total of 8). <br>
  - Roll `2, 3, 4, or 5`: Add the rolled number to the score. <br>
- **Score Tracking**: Displays both the current and historical scores for the player and computer. <br>
- **Winning Condition**: The first to reach the target score of 20 wins. <br>

## Concepts Used<br>
This project demonstrates various Python programming concepts, including: <br>
1. **Functions**:<br>
   - Modular code with functions for game rules and gameplay logic. <br>
2. **Conditionals**:<br>
   - Decision-making with `if-elif-else` for scoring and gameplay rules. <br>
3. **Loops**:<br>
   - `while` loops for continuous gameplay until a winning condition is met. <br>
4. **Random Module**:<br>
   - Generating random dice rolls and coin toss outcomes. <br>
5. **Lists**:<br>
   - Recording score histories for both the player and the computer. <br>
6. **Input Handling**:<br>
   - Interactive prompts to engage the user. <br>
7. **String Formatting**:<br>
   - Professional, user-friendly messages with `f-strings`.<br>
## How to Play<br>
1. Run the script using Python. <br>
2. Choose from the menu: <br>
   - Press `P` to play the game. <br>
   - Press `R` to read the game rules. <br>
   - Press `E` to exit the game. <br>
3. During gameplay: <br>
   - Toss a coin to determine the turn order. <br>
   - Roll the dice on your turn and accumulate points based on the dice result. <br>
   - Compete to be the first to reach a score of 20. <br>

## Prerequisites
- Python 3.x installed on your system. <br>
- Basic understanding of running Python scripts. <br>

## Example Output
********************************************<br>
       WELCOME TO THE ROLLING DICE GAME<br>
********************************************<br>

1. Press P to Play Game (or press 1) <br>
2. Press R to Read Game Rules (or press 2) <br>
3. Press E to Exit the Game (or press 3) <br>

Enter your choice (P/R/E or 1/2/3): P<br>

*************    TOSS    *************<br>
Who gets the first turn to roll the dice? <br>
Choose Head or Tail: Head<br>

You chose Head, and it is Head. <br>
You will roll the dice first. <br>

Press R to roll the dice: R<br>
You rolled a 6. <br>
Your current score: 8<br>
...
