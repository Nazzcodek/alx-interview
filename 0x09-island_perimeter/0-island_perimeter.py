#!/usr/bin/python3
"""This is the island perimeter interview solution"""


def island_perimeter(grid):
    """this method find the perimeter of an island"""
    # Initialize the perimeter count to 0
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check the top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom neighbor
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right neighbor
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
