#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Напечатать три данных действительных числа , и сначала в порядке их возрастания, затем - в порядке убывания.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)
print(c, b, a)