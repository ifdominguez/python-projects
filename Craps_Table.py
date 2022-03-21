# Copyright 2022 Israel Dominguez
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ------- Craps Table Simulation -------

import random

# Create function to define craps roll
def craps_die():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die_final = die1 + die2
    return die_final


# Create Counters
win = 0
loss = 0
games_total = 0
rolls_total = 0

# Simulate single game
for trials in range(1):
    roll = craps_die()
    # Initial Roll
    if roll == 7 or roll == 11:
        win = 1
    elif roll == 2 or roll == 3 or roll == 12:
        loss = 1
    # Re-Roll if needed
    else:
        re_roll = craps_die()
        if re_roll == 7:
            loss = 1
        elif re_roll == roll:
            win = 1
        else:
            # Second Re-Roll condition
            while re_roll not in (7, roll):
                re_roll = craps_die()
            if re_roll == 7:
                loss = 1
            elif re_roll == roll:
                win = 1

# Print
print("----- Single Game Result -----")
if win == 1:
    print("The pass bet won! :)")
    win = 0
elif loss == 1:
    print("The pass bet lost. :(")
    loss = 0

# Simulate 10,000 games
iter_count = 10000

# Loop to simulate 10,000 games
for trials in range(iter_count):
    roll = craps_die()
    rolls_total = rolls_total + 1
    # Initial Roll
    if roll == 7 or roll == 11:
        win = win + 1
        games_total = games_total + 1
    elif roll == 2 or roll == 3 or roll == 12:
        loss = loss + 1
        games_total = games_total + 1
    # Re-Roll if needed
    else:
        re_roll = craps_die()
        rolls_total = rolls_total + 1
        if re_roll == 7:
            loss = loss + 1
            games_total = games_total + 1
        elif re_roll == roll:
            win = win + 1
            games_total = games_total + 1
        else:
            # Second Re-Roll condition
            while re_roll not in (7, roll):
                rolls_total = rolls_total + 1
                re_roll = craps_die()
            if re_roll == 7:
                loss = loss + 1
                games_total = games_total + 1
            elif re_roll == roll:
                win = win + 1
                games_total = games_total + 1

avg_rolls = rolls_total / games_total
win_prob = (win / games_total) * 100

# Print Answer
print("----- Simulation of 10,000 games -----")
print("The average number of dice rolls in a game of craps is {:.2f} rolls.".format(avg_rolls))
print("The estimated win probability for a game of craps is {:.2f}%.".format(win_prob))