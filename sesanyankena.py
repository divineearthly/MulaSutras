#!/usr/bin/env python3
"""
Sesanyankena Caramena (By the last digit)
Find remainder of division by 10^n without performing division.
Simply return the last n digits.
"""
def remainder_by_10_power(num: int, n: int) -> int:
    return num % (10 ** n)
