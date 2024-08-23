#!/usr/bin/python3
"""method that determines if a given data set represents a valid
UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.
    """

    n_bytes = 0

    for num in data:
        if num < 0 or num > 255:
            return False

        bin_rep = format(num, "08b")[-8:]

        if n_bytes == 0:

            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not bin_rep[0] == '1' and bin_rep[1] == '0':
                return False

        n_bytes -= 1

    return n_bytes == 0
