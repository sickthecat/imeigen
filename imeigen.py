#!/usr/bin/env python2
import random
import sys

def generate_imei():
    imei = [random.randint(0, 9) for _ in range(14)]
    imei_str = ''.join(map(str, imei))
    return imei_str + calculate_luhn_checksum(imei_str)

def calculate_luhn_checksum(number_str):
    sum = 0
    num_digits = len(number_str)
    oddeven = num_digits & 1

    for i in range(0, num_digits):
        digit = int(number_str[i])

        if not ((i & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum += digit

    return str((10 - (sum % 10)) % 10)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        num_imeis = int(sys.argv[1])
    else:
        num_imeis = 1

    for _ in range(num_imeis):
        print(generate_imei())
