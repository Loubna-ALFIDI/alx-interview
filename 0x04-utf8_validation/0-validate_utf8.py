#!/usr/bin/python3
"""this script defines the function validUTF8"""


def validUTF8(data):
    """this function checks if data is utf-8 valid"""
    is_valid = True
    for c in data:
        try:
            b = c.to_bytes(8, byteorder='little')
            b.decode('utf-8')
            continue
        except UnicodeDecodeError:
            is_valid = False
            break
    return is_valid
