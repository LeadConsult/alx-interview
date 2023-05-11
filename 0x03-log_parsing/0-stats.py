import sys

# store the count of all status codes in a dictionary
status_codes_dict = {}

# store the total size of all files in a variable
total_size = 0

# keep count of the number lines counted
count = 0

try:
    for line in sys.stdin:
        # split the line into a list of words
        words = line.split()

        # if the line is not empty and the first word is "FILE", then process the line
        if words and words[0] == "FILE":
            # get the status code from the second word
            status_code = words[1]

            # get the file size from the third word
            file_size = int(words[2])

            # if the status code is not in the dictionary, then add it with a count of 1
            if status_code not in status_codes_dict:
                status_codes_dict[status_code] = 1

            # if the status code is in the dictionary, then increment its count
            else:
                status_codes_dict[status_code] += 1

            # update the total size
            total_size += file_size

            # update the count of lines
            count += 1

        # if the count of lines is equal to 10, then print the status code counts and reset the count
        if count == 10:
            print('File size: {}'.format(total_size))

            # print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

            count = 0

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
