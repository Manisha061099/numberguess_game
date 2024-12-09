# numberguess_game
Welcome to the Number Guessing Game! This is a simple Python game where the computer randomly selects a number between 1 and 100, and the player has to guess it. The game provides feedback on whether the guess is too high or too low, and it continues until the player guesses the correct number.

Table of Contents
How to Play
How to Run
Features
Extensions
License
How to Play
The computer randomly selects a number between 1 and 100.
You will be prompted to enter your guess.
After each guess, the game will tell you whether your guess is:
Too low
Too high
Correct
The game continues until you guess the correct number.
You will receive feedback on how many attempts it took to guess the correct number.
How to Run
To play the Number Guessing Game on your local machine, follow these steps:

1. Clone or Download the Repository
If you want to download or clone the project:

bash
Copy code
git clone https://github.com/yourusername/number-guessing-game.git
Alternatively, you can simply download the Python file.

2. Install Python
Ensure that Python 3.x is installed on your machine. You can check if Python is installed by running the following command:

bash
Copy code
python --version
If Python is not installed, you can download and install it from the official website: https://www.python.org/downloads/

3. Run the Game
Once you've downloaded or cloned the repository, navigate to the project folder and run the game:

bash
Copy code
python number_guessing_game.py
4. Follow the Prompts
The game will prompt you to guess a number. Type your guess and press Enter. The game will provide feedback until you guess the correct number.

Features
Random number generation: The computer randomly selects a number between 1 and 100.
Feedback on guesses: After each guess, the game will tell you if the guess is too low or too high.
Unlimited attempts: Keep guessing until you find the correct number.
Attempts count: The game will tell you how many attempts it took to guess the correct number.
Extensions
Here are some possible extensions you can add to the game:

Difficulty levels: Implement different difficulty levels (e.g., easy, medium, hard) where the number range changes based on difficulty.
Maximum attempts: Add a limit to the number of attempts, and end the game if the player exceeds the maximum number of guesses.
Score tracking: Track how many attempts it takes to guess the number and save the best scores.
GUI interface: Use a Python library like Tkinter to create a graphical user interface (GUI) for the game.
License
This project is licensed under the MIT License - see the LICENSE file for details.
