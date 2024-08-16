#!/usr/bin/env python3
"""
Write a script that reads stdin line by line and computes metrics:
"""
import sys
import signal

# Initialize global variables for tracking metrics
total_file_size = 0
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_count = 0


def print_stats():
    """
    Print the accumulated metrics.

    Outputs the total file size and the count of each status code
        that has appeared
    in the processed log lines. Only status codes with counts greater
        than zero are printed.
    The status codes are printed in ascending order.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def process_line(line):
    """
    Process a single line of input and update metrics.

    Args:
        line (str): A line from the input stream that represents a log entry.

    The line is expected to have a specific format. This function
        extracts the status
    code and file size from the line, updates the count for the status code and
    accumulates the total file size. It also prints statistics every 10 lines.
    """
    global total_file_size, status_code_count, line_count

    # Split the line into parts and validate the length
    parts = line.split()
    if len(parts) < 7:
        return  # Skip lines that don't match the expected format

    # Extract the status code and file size from the line
    status_code = parts[-2]
    file_size = parts[-1]

    # Update metrics if the status code is valid
    if status_code in status_code_count:
        try:
            file_size = int(file_size)
            status_code_count[status_code] += 1
            total_file_size += file_size
        except ValueError:
            pass  # Ignore lines with invalid file size format

    line_count += 1
    if line_count % 10 == 0:
        print_stats()


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C).

    Args:
        sig (int): The signal number.
        frame (frame object): The current stack frame.

    Prints the accumulated statistics and exits the program gracefully when
    a keyboard interruption is detected.
    """
    print_stats()
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    process_line(line)

# Print final statistics if the input ends normally
print_stats()
