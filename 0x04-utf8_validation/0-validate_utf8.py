#!/usr/bin/python3
"""this is utf8 validation module"""


def validUTF8(data):
    '''this method validate data for utf8'''

    def check_leading_bits(byte):
        return (byte & 0xC0) == 0x80

    # Iterate through the data
    i = 0
    while i < len(data):
        leading_bits = bin(data[i])[2:].zfill(8)[:3]

        bit_1 = checking_leading_bits(data[i + 1])
        bit_2 = checking_leading_bits(data[i + 2])
        bit_3 = checking_leading_bits(data[i + 3])

        # Check the number of bytes in the current character
        if leading_bits.startswith('0'):
            i += 1
        elif leading_bits.startswith('110'):
            if i + 1 < len(data) and bit_1:
                i += 2
            else:
                return False
        elif leading_bits.startswith('1110'):
            if i + 2 < len(data) and bit_1 and bit_2:
                i += 3
            else:
                return False
        elif leading_bits.startswith('11110'):
            if i + 3 < len(data) and bit_1 and bit_2 and bit_3:
                i += 4
            else:
                return False
        else:
            return False  # Invalid leading bits

    return True
