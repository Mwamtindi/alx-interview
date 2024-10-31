#!/usr/bin/python3
"""
Module that contains a function to validate UTF-8 encoding.
"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        byte = byte & 0xFF
        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                num_bytes = 3
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
