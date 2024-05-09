#!/usr/bin/python3
""" valide_utf8 """


def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        num_bytes = 1
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        # Check if the number of bytes is within the valid range
        if num_bytes < 1 or num_bytes > 4:
            return False

        # Check if there are enough bytes left in the data
        if i + num_bytes > len(data):
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            if not is_continuation(data[i + j]):
                return False

        i += num_bytes

    return True

# Example usage
data_set = [197, 130, 1]  # Represents the UTF-8 encoding for "Ç"
print(validUTF8(data_set))  # Output: True

invalid_data_set = [197, 130, 200]  # Invalid UTF-8 encoding
print(validUTF8(invalid_data_set))  # Output: False
