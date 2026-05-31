there are two games made by me, one is a classic snake water gun game. and the other one is the perfect gusse game.

the first one:
contains a simple Snake, Water, Gun game built using Python basics of programming.The project uses random computer choices, user input handling, and conditional statements to create a fun command-line game experience. It was made as a practice project to improve understanding of Python concepts such as dictionaries, loops, and logic building.

the second one:
a simple number guessing game built using Python In this game, the computer randomly selects a number between 1 and 100, and the user keeps guessing until the correct number is found. The program provides hints after each guess and stores all guessed numbers in a text file. This project was created to practice Python concepts such as loops, conditionals, file handling, lists, and random module.

the third one is my logic roman to number:
# Roman to Integer - LeetCode #13

## Problem Description

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Given a Roman numeral, convert it to an integer.

## Solution Approach

This solution uses:

* A dictionary to map Roman numeral symbols to their integer values.
* A `while` loop to iterate through the Roman numeral string.
* Comparison of adjacent symbols to determine whether values should be added or subtracted.
* Index skipping when a pair has already been processed.

### Logic

1. Compare the current Roman numeral with the next one.
2. If the current value is smaller than the next value, subtract it from the next value and move two positions forward.
3. If the values are equal, add both values and move two positions forward.
4. If the current value is greater than the next value, add the current value and move one position forward.
5. Handle the final remaining character separately.



