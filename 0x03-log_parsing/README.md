# 0x03. Log Parsing

## Project Overview

This project focuses on parsing and processing data streams in real-time using Python. The primary goal is to read from standard input (stdin), handle log data in a specific format, and compute metrics based on the input data. The project tests your understanding of Python programming concepts, including file I/O, signal handling, data processing, regular expressions, and exception handling.

## Concepts and Skills Utilized

- **File I/O in Python**: Reading from `sys.stdin` line by line.
- **Signal Handling**: Handling keyboard interruptions (CTRL + C) using signal handling in Python.
- **Data Processing**: Parsing strings to extract specific data points and aggregating data to compute summaries.
- **Regular Expressions**: Validating the format of each line using regular expressions.
- **Dictionaries in Python**: Counting occurrences of status codes and accumulating file sizes.
- **Exception Handling**: Managing exceptions during file reading and data processing.

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- Code adheres to the PEP 8 style guide (version 1.7.x).
- All files are executable and end with a new line.
- The first line of all scripts is `#!/usr/bin/python3`.

## Project Files

- **0-stats.py**: The main Python script that reads log entries from stdin, validates their format, and computes metrics.
- **0-generator.py**: A Python script that generates random log entries for testing purposes.

## How to Run

To run the log parsing script, use the following command:

```bash
./0-generator.py | ./0-stats.py

