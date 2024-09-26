#!/usr/bin/python3

"""
Calculate the perimeter of an island in a grid
"""

def island_perimeter(grid):
    perimeter = 0  # Initialize perimeter counter

    rows = len(grid)  # Number of rows
    columns = len(grid[0])  # Number of columns

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4

                # Check the cell above (i - 1)
                if i > 0 and grid[i - 1][j] == 1:  
                    perimeter -= 1

                # Check the cell to the left (j - 1)
                if j > 0 and grid[i][j - 1] == 1:  
                    perimeter -= 1

                # Check the cell below (i + 1)
                if i < rows - 1 and grid[i + 1][j] == 1:  
                    perimeter -= 1

                # Check the cell to the right (j + 1)
                if j < columns - 1 and grid[i][j + 1] == 1:  
                    perimeter -= 1

    return perimeter