#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = set(status_codes.keys())
line_count = 0


def print_stats():
    """
    Function to print statistics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Split the line by spaces to extract fields
            parts = line.split()
            # Validate the expected format
            if len(parts) < 7:
                continue
            ip = parts[0]
            date = parts[3] + " " + parts[4]
            method = parts[5][1:]
            path = parts[6]
            http_version = parts[7][:-1]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code count if it's a valid code
            if status_code in valid_codes:
                status_codes[status_code] += 1

        except Exception:
            # If any error occurs, skip this line
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # On keyboard interrupt, print final stats
    print_stats()
    raise

# Print final stats after the loop ends
print_stats()
