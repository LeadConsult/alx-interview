#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""

def canUnlockAll(boxes):
    # Create variables for the current position and unlocked boxes
    position = 0
    unlocked = {}

    # Loop through each box in the list of boxes
    for box in boxes:
        # If the box is empty or the position is 0, mark it as always unlocked
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        
        # Loop through each key in the box
        for key in box:
            # If the key is valid and not the current position, mark it as unlocked
            if key < len(boxes) and key != position:
                unlocked[key] = key
        
        # If all boxes are unlocked, return True
        if len(unlocked) == len(boxes):
            return True
        
        # Move to the next box
        position += 1
    
    # If not all boxes are unlocked, return False
    return False
