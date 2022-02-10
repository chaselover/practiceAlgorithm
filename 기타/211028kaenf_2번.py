#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'validateAddresses' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY addresses as parameter.
#

def validateAddresses(addresses):
    answer = []
    for address in addresses:
        address.strip()
        if ':' not in address and address.count('.') == 3:
            if not address[0].isdigit() or not address[-1].isdigit():
                answer.append('Neither')
                continue
            arr = []
            tmp = address.split('.')
            flag = 0
            for each in tmp:
                if len(each) > 3 or int(each) < 0 or int(each) > 255:
                    flag = 1 
                    break
                if each[0] == '0' and int(each) >= 8:
                    flag = 1
                    break
            if flag:
                answer.append('Neither')
                continue
            answer.append('IPv4')
        elif '.' not in address and ':' in address:
            flag = 0
            if address[0] == ':' and address[1] != ':':
                answer.append('Neither')
                continue
            if address[-1] == ':' and address[-2] != ':':
                answer.append('Neither')
            for char in address:
                if char not in '0123456789abcdef:':
                    flag = 1
                    break
            if flag:
                answer.append('Neither')
                continue
            arr = []
            tmp = list(address.split(':'))
            for idx, each in enumerate(tmp):
                if idx > 1 and not each:
                    if not tmp[idx - 1] and idx != len(tmp) - 1:
                        flag = 1
                        break
            if flag:
                answer.append('Neither')
                continue
            for each in tmp:
                if not each:
                    flag = 1
                    break
            if not flag and len(tmp) != 8:
                answer.append('Neither')
                continue
            answer.append('IPv6')
        else:
            answer.append('Neither')
    return answer

# 000.012.234.23

if __name__ == '__main__':
    addresses_count = int(input().strip())

    addresses = []

    for _ in range(addresses_count):
        addresses_item = input()
        addresses.append(addresses_item)

    result = validateAddresses(addresses)

    print(result)