#!/bin/python3

T = int(input())
s = []
for i in range(T):
    s = input()
    even = s[::2]
    odd = s[1::2]
    print(even,odd)
    