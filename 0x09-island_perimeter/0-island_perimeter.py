#!/usr/bin/python3

"""
This module def a func to calc perimeter of an island described in a grid.
The grid is represented as a 2D list where:
- 0 represents water
- 1 represents land

Functions:
    island_perimeter(grid): Calculates perimeter of island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.

    Args:
        grid : A 2D grid where 0 reps water and 1 reps land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
