# PynNum
A  Wordle inspired 4-digit number guessing game built with Python and Tkinter. Crack the code before you run out of tries!


A lightweight, desktop-based number guessing game built using **Python**, **Tkinter**, and **NumPy**. The game challenges players to guess a randomly generated 4-digit number within 4 attempts, using visual, color-coded feedback inspired by modern puzzle games like Wordle.

## 🚀 Features

- **Dynamic Feedback System:** Color-coded hints map out your accuracy:
  - 🟩 **Green**: Right digit, right spot.
  - 🟨 **Orange**: Right digit, wrong spot.
  - 🟥 **Red**: Digit is not in the secret number at all.
- **Robust Input Validation:** Prevents crashes by screening out non-integer inputs or guesses that aren't exactly 4 digits long.
- **Persistent Guess History:** Keeps track of previous attempts inside the GUI window to help you strategize.

## 🛠️ Requirements & Installation

Make sure you have Python installed alongside `numpy`.

1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/tkinter-number-guesser.git](https://github.com/YOUR_USERNAME/tkinter-number-guesser.git)
   cd tkinter-number-guesser
2. Install dependencies:

 pip install numpy


3.Run the application:

 python Numgame.py   
