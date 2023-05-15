#!/usr/bin/python3

"""
UTF-8 Validation

This function validates whether the given data is a valid UTF-8 encoding.

A valid UTF-8 encoding consists of a sequence of bytes, each of which
represents a single Unicode code point. The first byte of each sequence
must have the high-order two bits set to 10, and the remaining bytes must
have the high-order bit set to 1. The number of bytes in a sequence
determines the value of the represented code point.

The function returns True if the given data is a valid UTF-8 encoding,
and False otherwise.
"""


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False

    :param data: The data to be validated.
    :return: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    number_of_bytes_in_UTF_8 = 0

    # Iterate over the bytes in the data.
    for byte in data:

        # Get the mask for the high-order bit.
        mask = 1 << 7

        # If this is the first byte in the sequence, then check
        # that the high-order two bits are set to 10.
        if not number_of_bytes_in_UTF_8:

            # While the high-order bit of the byte is set, increment
            # the number of bytes in the sequence.
            while byte & mask:
                number_of_bytes_in_UTF_8 += 1
                mask >>= 1

            # If the number of bytes in the sequence is 0 or greater
            # than 4, then the encoding is invalid.
            if not number_of_bytes_in_UTF_8 or number_of_bytes_in_UTF_8 > 4:
                return False

        # Otherwise, check that the high-order bit of the byte is set to 1.
        else:

            # If the high-order bit of the byte is not set to 1, then
            # the encoding is invalid.
            if byte >> 6 != 0b10:
                return False

        # Decrement the number of bytes in the sequence.
        number_of_bytes_in_UTF_8 -= 1

    # If the number of bytes in the sequence is 0, then the encoding is valid.
    return number_of_bytes_in_UTF_8 == 0
