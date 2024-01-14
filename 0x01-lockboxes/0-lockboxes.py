#!/usr/bin/python3
"""
    This is the lockbox module
"""


def canUnlockAll(boxes):
    """
    this method check if all box can unlock and returns
        True or False
    """
    keys = {0}  # Start with the keys to open the first box
    visited = set()

    while keys:
        current_key = keys.pop()
        visited.add(current_key)

        for new_key in boxes[current_key]:
            if new_key not in visited:
                keys.add(new_key)

    return len(visited) == len(boxes)
