
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python that practices string manipulation, loops, and handling user input. Students will implement game flow, track guesses, and display clear win/lose outcomes.

## 📝 Tasks

### 🛠️	Implement the Hangman Game

#### Description
Create a playable Hangman program that selects a secret word, displays masked progress, accepts single-letter guesses from the player, updates the display after each guess, and ends the game when the player guesses the word or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the secret word as masked characters (e.g., _ _ _ _ ) and reveal letters as they are guessed.
- Accept single-letter guesses and ignore or warn on repeated guesses.
- Track and display letters already guessed.
- Limit the number of incorrect attempts (suggestion: 6) and show remaining attempts.
- End the game with a clear win or lose message and reveal the secret word on loss.

Optional enhancements (not required):

- Add difficulty levels with longer/shorter words.
- Load words from `data.csv` or a separate words file.
- Provide a simple ASCII-art hangman that updates with incorrect guesses.

