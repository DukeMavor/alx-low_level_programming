#!/usr/bin/python3
"""
This module defines a function that computes the perimeter of an island
in a rectangular grid.
"""

def island_perimeter(grid):
    """
    Computes the perimeter of the island described in `grid`.

    Args:
        grid (list of list of int): A rectangular grid of 0s and 1s, where
            0 represents water and 1 represents land.

    Returns:
        The perimeter of the island, or 0 if the grid is empty or has no land.

    Example:
        >>> grid = [
        ...     [0, 0, 0, 0, 0, 0],
        ...     [0, 1, 0, 0, 0, 0],
        ...     [0, 1, 0, 0, 0, 0],
        ...     [0, 1, 1, 1, 0, 0],
        ...     [0, 0, 0, 0, 0, 0]
        ... ]
        >>> island_perimeter(grid)
        12
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
