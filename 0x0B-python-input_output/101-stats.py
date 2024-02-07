#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""


#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Prints the metrics computed since the beginning.

    Parameters:
    - total_size: The total file size.
    - status_codes: A dictionary containing the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            data = line.split()
            if len(data) > 2:
                total_size += int(data[-1])
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1

            count += 1
            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
