Island Perimeter
Project Overview
The Island Perimeter project focuses on calculating the perimeter of a single island within a 2D grid. The grid is represented by a list of lists (2D array), where 0 represents water and 1 represents land. The challenge is to compute the total perimeter of the island by iterating through the grid and analyzing the land cells and their surroundings.

Concepts Covered
2D Arrays (Matrices): Navigating through a 2D list using nested loops.
Conditional Logic: Applying conditions to determine how much each land cell contributes to the perimeter.
Counting Techniques: Determining how to account for the perimeter based on adjacent water or land cells.
Requirements
Python version: The project is interpreted/compiled using Python 3.4.3 on Ubuntu 20.04 LTS.
PEP 8: Code must adhere to PEP 8 style guidelines (version 1.7).
No external modules: You are not allowed to import any module.
Documentation: All modules and functions must be documented.
Executable files: Ensure that all your files are executable.
Problem Description
You are tasked with writing a function def island_perimeter(grid): that computes the perimeter of the island in the provided grid. The island is defined as a contiguous region of land (1s) surrounded by water (0s).

Rules:
Each cell is a square with a side length of 1.
Cells are connected horizontally and vertically (not diagonally).
The island is completely surrounded by water, and there are no lakes.
The grid will have only one island or no island.
The grid dimensions do not exceed 100x100.
Example
Consider the following grid:

css
Copy code
grid = [    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
In this case, the function island_perimeter(grid) should return 12 because the perimeter of the island is 12.

Explanation:
For each land cell (1), the function checks its neighboring cells (up, down, left, right).
If a neighboring cell is water (0), it contributes 1 unit to the perimeter.
The function sums up all these contributions to compute the total perimeter.
File Structure
0-island_perimeter.py: Contains the island_perimeter function that computes the perimeter.
0-main.py: A script for testing the island_perimeter function using a sample grid.
README.md: This documentation file.
Usage
To test the solution, you can run the 0-main.py file. Ensure that the files have the appropriate executable permissions.

bash
Copy code
$ ./0-main.py
Expected output for the sample grid:

Copy code
12
Algorithm
The algorithm for computing the perimeter works as follows:

Iterate through every cell in the grid.
For each land cell (1):
Check its four neighboring cells (up, down, left, right).
If the neighboring cell is water (0) or out of bounds, increase the perimeter count.
Return the total perimeter.
Example Execution
Sample execution of the program using the provided grid:

bash
Copy code
$ ./0-main.py
12
Further Improvements
Possible future enhancements could include optimizing the solution for larger grids or implementing additional features such as detecting multiple islands.

Author
This project is part of the ALX Interview Preparation Curriculum.

This README.md file provides an overview of the project, including the problem description, requirements, and instructions on how to run the solution. Let me know if you'd like any changes!







