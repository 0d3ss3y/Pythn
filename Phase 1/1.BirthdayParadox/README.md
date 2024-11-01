# Birthday Paradox Simulator

**Birthday Paradox Simulator** is a probability-based program that explores the surprising likelihood of two people in a group sharing the same birthday. Even in relatively small groups, the probability of shared birthdays is higher than one might intuitively expect. This program uses Monte Carlo simulations to determine the likelihood of shared birthdays across different group sizes.

## How It Works

The objective of the Birthday Paradox Simulator is to estimate the probability of shared birthdays in groups of various sizes. The program performs multiple trials to simulate random birthdays and calculates the probability of at least two people sharing a birthday for each group size.

### Steps

1. Specify the group size (e.g., 23 people).
2. Set the number of trials (e.g., 1000).
3. For each trial, the program:
   - Randomly assigns birthdays to each individual in the group.
   - Checks if at least two people in the group have the same birthday.
   - Records the occurrence of shared birthdays.
4. After running the trials, the program calculates the percentage of trials where a shared birthday was found, providing an estimated probability.

Using this simulation approach, the program calculates probabilities for various group sizes, demonstrating how likely it is for people in a group to share a birthday.

## Example Results

In a group of:
- **23 people**, there is approximately a **50%** chance of a shared birthday.
- **70 people**, there is a **99.9%** chance of a shared birthday.

These results showcase the probability of shared birthdays as the group size increases.

## Requirements

- Python 3.x (if implementing in Python)
- No additional dependencies

## Installation

1. Clone or download the project files.
2. Run `birthday.py` to start the simulation.