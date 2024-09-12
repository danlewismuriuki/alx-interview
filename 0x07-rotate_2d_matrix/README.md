# Rotate 2D Matrix

This project contains a Python function to rotate an `n x n` 2D matrix by 90 degrees clockwise, in place.

## Table of Contents
- [Task](#task)
- [Algorithm](#algorithm)
- [Example](#example)
- [Requirements](#requirements)
- [Usage](#usage)
- [Additional Information](#additional-information)

## Task

Given an `n x n` 2D matrix, write a function that rotates the matrix 90 degrees clockwise, in place.

### Prototype
```python
def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
Algorithm
To rotate a matrix 90 degrees clockwise in place:

Transpose the matrix: Swap elements at positions (i, j) with (j, i).
Reverse each row: For every row in the transposed matrix, reverse the row to achieve the final rotated matrix.
Step-by-step Explanation
Given the matrix:

Copy code
1 2 3
4 5 6
7 8 9
Transpose the matrix:

Copy code
1 4 7
2 5 8
3 6 9
Reverse each row:

Copy code
7 4 1
8 5 2
9 6 3
This gives the matrix rotated by 90 degrees clockwise.

Example
python
Copy code
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
Expected Output
lua
Copy code
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Requirements
Allowed editors: vi, vim, emacs
Interpreter: All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.10)
All files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.8.0)
You are not allowed to import any module
All modules and functions must be documented
All your files must be executable
Usage
Clone this repository.
Navigate to the 0x07-rotate_2d_matrix directory.
Ensure the file 0-rotate_2d_matrix.py is executable.
Run the provided test file main_0.py to see the output.
bash
Copy code
chmod +x 0-rotate_2d_matrix.py
chmod +x main_0.py
./main_0.py
Additional Information
This project helps to understand matrix manipulation, in-place operations, and the importance of optimizing space complexity.
It tests your ability to work with 2D data structures in Python and improves problem-solving and algorithmic thinking skills.
css
Copy code

This `README.md` provides a clear and concise overview of the project, instructions, and 
