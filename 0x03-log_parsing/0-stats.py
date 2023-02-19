#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Read stdin line by line
for line in sys.stdin:
    # Split the line into its components
    try:
        ip_address, _, _, timestamp, _, request, status_code, file_size, *_ = line.split()
    except ValueError:
        # If the line doesn't match the expected format, skip it
        continue

    # Update metrics
    status_code = int(status_code)
    if status_code in status_codes:
        status_codes[status_code] += 1
    total_size += int(file_size)
    line_count += 1

    # Print statistics every 10 lines or when interrupted
    if line_count % 10 == 0:
        print(f'Total file size: {total_size}')
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print(f'{code}: {count}')
        print()

# Print final statistics
print(f'Total file size: {total_size}')
for code, count in sorted(status_codes.items()):
    if count > 0:
        print(f'{code}: {count}')