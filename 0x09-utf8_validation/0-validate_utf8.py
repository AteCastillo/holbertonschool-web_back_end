#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""



def validUTF8(data):
    '''
    return True if data is a valid UTF-8 encoding, 
    else return False
    '''
    i = 0
    ld = len(data)
    while i < ld:
            count = 0
            if data[i] & 0x80 == 0:
                i += 1
            elif data[i] & 0xc0 == 0x80 or data[i] & 0xf8 == 0xf8:
                return False
            else:
                test = 0x40
                while data[i] & test:
                    count += 1
                    test >>= 1
                i += 1
                for _ in range(count):
                    if i >= ld or data[i] & 0xc0 != 0x80:
                        return False
                    i += 1
    return True
