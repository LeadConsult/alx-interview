#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
"""

import sys

if __name__ == '__main__':

    file_size, count_code = 0, 0
    """Two variables are being initialized: file_size
    which will be used to store the size of the file
    being read, and count_code which will be used to
    count the number of codes encountered.
    """
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints the statistics: file size and counts for each status code.
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

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
