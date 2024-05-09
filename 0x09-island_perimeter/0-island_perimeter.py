#!/usr/bin/python3
"""this is the island perimeter module"""


def island_perimeter(grid):
    """Calculate the perimeter of an island."""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check the cells around the current cell
                if i == 0 or grid[i - 1][j] == 0:  # Top cell
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Bottom cell
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left cell
                    perimeter += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:  # Right cell
                    perimeter += 1
    return perimeter
