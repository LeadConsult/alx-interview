#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
"""

import sys

if __name__ == '__main__':

    file_size, count_code = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints the statistics: file size and counts for each status code.
        """
        print(f"The file size: {file_size}")
        for key in sorted(stats):
            value = stats[key]
            if value:
                print(f"{key}: {value}")



    try:
        for line in sys.stdin:
            count_code += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if count_code % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)
    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
