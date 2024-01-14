#!/usr/bin/python3
"""
    This is the lockbox module
"""


def canUnlockAll(boxes):
    """
    this method check if all box can unlock and returns
        True or False
    """
    if not boxes or not boxes[0]:
        return False  # No boxes or the first box is empty

    keys = set([0])  # Start with the keys to open the first box
    visited = set([0])  # Keep track of visited boxes

    queue = [0]  # Use a queue for BFS

    while queue:
        current_box = queue.pop()

        for key in boxes[current_box]:
            if key not in visited:
                visited.add(key)
                keys.add(key)
                queue.append(key)

    return len(visited) == len(boxes)
