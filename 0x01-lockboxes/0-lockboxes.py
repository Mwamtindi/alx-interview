#!/usr/bin/python3
"""Module with a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each element is a list of keys
                                contained in that box.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return True

    n = len(boxes)
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with the keys in the first box
    to_check = [0]  # Boxes to check

    while to_check:
        box_index = to_check.pop()  # Get the last box to check
        for key in boxes[box_index]:
            if key < n and not unlocked[key]:  # Check if the key is valid
                unlocked[key] = True  # Unlock the box
                to_check.append(key)

    return all(unlocked)  # Return True if all boxes are unlocked


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
