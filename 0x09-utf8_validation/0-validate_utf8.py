#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""



def validUTF8(data):
    '''
    return True if data is a valid UTF-8 encoding, 
    else return False
    '''
    bytes = 0
    for number in data:
        binary_result = format(number, '#010b')[-8:]

        if bytes == 0:
            for bit in binary_result:
                if bit == '0':
                    break
                bytes += 1

            if bytes == 0:
                continue

            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (binary_result[0] == '1' and binary_result[1] == '0'):
                return False

        bytes -= 1

    return bytes == 0