import math

'''
Total digits = (int)(math.log10(n)+1)
First digit = (int)(n / pow(10, digits))
last digit = (n % 10)
'''


def evenlyDivides(self, N):  # gfg
    # 12 -> 2
    # 22074 -> 2 (0 is a digit may raise ZerodivisionError)
    count = 0
    real = N
    while N:
        last = N % 10
        if last != 0 and real % last == 0:  # zeroDivisionError handled
            count += 1
        N = N//10
    return count


def reverse_digit(self, n):  # gfg
    # array,string -> use Two pointer
    digit = 0
    while n:
        last = n % 10
        digit = (10*digit)+last
        n = n//10
    return digit



