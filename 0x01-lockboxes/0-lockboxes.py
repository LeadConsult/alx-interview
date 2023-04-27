#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def can_unlock_all(boxes):
    """
    This function determines if all the boxes can be opened.

    Args:
        boxes: A list of lists, where each inner list represents the 
        keys to unlock the corresponding box.

    Returns:
        True if all the boxes can be opened, False otherwise.
    """

    # Check if the input is valid.
    if not boxes or not isinstance(boxes, list):
        return False

    # Initialize a set to store the unlocked boxes.
    unlocked = set()

    # Iterate over the boxes.
    for box in boxes:
        # Check if the box is already unlocked.
        if box in unlocked:
            continue

        # Iterate over the keys in the box.
        for key in box:
            # Check if the key is already unlocked.
            if key in unlocked:
                continue

            # Unlock the box.
            unlocked.add(key)

    # Check if all the boxes are unlocked.
    return len(unlocked) == len(boxes)
