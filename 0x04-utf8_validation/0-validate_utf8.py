#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Validate if the given data is a valid UTF-8 encoded string.

    Args:
        data (list): A list of integers representing the bytes.

    Returns:
        bool: True if the data is a valid UTF-8 encoded string, False otherwise.
    """
    num_of_bytes = 0

    # Iterate over each integer in the data array
    for num in data:
        # Get the binary representation. We only need the least significant 8 bits
        # for any given number, so we discard the rest.
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we are to start to count a new UTF-8 character.
        if num_of_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            start_mask = 0b10000000
            while start_mask & int(bin_rep, 2):
                num_of_bytes += 1
                start_mask >>= 1

            # 1 byte characters
            if num_of_bytes == 0:
                continue

        # Else, we are to account for the incoming bytes
        # which represents the Unicode character.
        else:
            # Else, only the 2 most significant bits should be 10.
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # We reduce the number of bytes to fill.
        num_of_bytes -= 1

    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return num_of_bytes == 0
