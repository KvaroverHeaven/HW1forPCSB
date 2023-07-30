# Arup Guha
# 10/1/2018
# Program that does some test statistics using a list.

import math
from typing import List

# This is how you create a list in Python.
scores: List[float] = []

# Prompt the user to enter the scores.
print("Please enter your test scores, ending the list with a -1.")
try:
    curscore: float = float(input(""))
except ValueError:
    print("That's not a score!")


# Read in the scores.
while curscore != -1:

    # Adds a value to the end of a list.
    if (0 <= curscore <= 100):
        scores.append(curscore)
    else:
        print("That's not a valid score.")

    # Get next score.
    try:
        curscore: float = float(input(""))
    except ValueError:
        print("That's not a score!")

# Set up my accumuators.
total = 0
minimum = scores[0]
maximum = scores[0]

# Go through each score.
for i in range(len(scores)):

    # Add into our total.
    total = total + scores[i]

    # Update the minimum if necessary.
    if scores[i] < minimum:
        minimum = scores[i]

    # Do the same for the maximum.
    if scores[i] > maximum:
        maximum = scores[i]

# Store average.
avg = total/len(scores)

# Use Python's Prewritten functions.
print(f"Min is {min(scores)} Max is {max(scores)} Sum is {sum(scores)}")

# Print out our stats so far.
print(f"Min = {minimum} Max = {maximum} Avg = {total/len(scores):.2f}")

# Add up the sum of terms for the variance.
varsum = 0
for x in scores:
    varsum = varsum + ((x-avg)**2)

# Print out the standard deviation.
print(f"The standard deviation is {math.sqrt(varsum/len(scores)):.3f}")
