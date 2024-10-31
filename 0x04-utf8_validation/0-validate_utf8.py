#!/usr/bin/python3
"""This module contains a function to validate UTF-8 encoding."""


def validUTF8(data):
    """Determine if a given data set reps valid UTF-8 encoding."""
    num_byte_s = 0

    for num in data:

        if num_byte_s > 0:
            if (num >> 6) != 0b10:
                return False
            num_byte_s -= 1
        else:

            if (num >> 7) == 0b0:
                num_byte_s = 0
            elif (num >> 5) == 0b110:
                num_byte_s = 1
            elif (num >> 4) == 0b1110:
                num_byte_s = 2
            elif (num >> 3) == 0b11110:
                num_byte_s = 3
            else:
                return False

    return num_byte_s == 0
