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

    def count_leading_ones(first_byte):
        """ Count the number of leading 1s in the first byte """
        if first_byte & 0b10000000 == 0:
            return 1
        num_leading_ones = 0
        mask = 0b10000000
        while mask & first_byte:
            num_leading_ones += 1
            mask >>= 1
        if num_leading_ones == 1 or num_leading_ones > 4:
            return -1
        return num_leading_ones

    current_index = 0
    while current_index < len(data):
        first_byte = data[current_index]
        num_bytes_needed = count_leading_ones(first_byte)

        if num_bytes_needed == -1:
            return False
        if num_bytes_needed == 1:
            current_index += 1
            continue

        if current_index + num_bytes_needed > len(data):
            return False

        for j in range(1, num_bytes_needed):
            if not (data[current_index + j] & 0b11000000 == 0b10000000):
                return False

        current_index += num_bytes_needed

    return True
