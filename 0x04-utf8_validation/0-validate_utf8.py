#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Validate if the given data is a valid UTF-8 encoded string.

    Args:
        data (list): A list of integers representing the bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoded string, False otherwise.
    """
    num_of_bytes = 0

    for num in data:
        if not (0 <= num <= 255):
            return False

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if num_of_bytes == 0:
            start_mask = 0b10000000
            while start_mask & int(bin_rep, 2):
                num_of_bytes += 1
                start_mask >>= 1

            if num_of_bytes == 0:
                continue

        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        num_of_bytes -= 1

    return num_of_bytes == 0
