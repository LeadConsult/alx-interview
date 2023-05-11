import sys

def main():
    # Initialize variables
    file_size = 0
    status_code_counts = {}

    # Read lines from stdin
    for line in sys.stdin:
        # Split the line into words
        words = line.split()

        # Get the status code and file size
        status_code = words[-2]
        file_size += int(words[-1])

        # Increment the count for the status code
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        # Print the status code counts every 10 lines
        if len(status_code_counts) == 10:
            print("File size: {}".format(file_size))
            for status_code, count in status_code_counts.items():
                print("{}: {}".format(status_code, count))
            status_code_counts = {}

    # Print the final status code counts
    if len(status_code_counts) > 0:
        print("File size: {}".format(file_size))
        for status_code, count in status_code_counts.items():
            print("{}: {}".format(status_code, count))

if __name__ == "__main__":
    main()
