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

    n_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        n_bytes -= 1

    return n_bytes == 0
