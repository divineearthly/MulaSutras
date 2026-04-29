#!/usr/bin/env python3
"""
Gunita Samuccaya for Division
Verify: dividend ≡ divisor × quotient + remainder mod 9
"""
def digit_sum(n: int) -> int:
    if n == 0: return 0
    return n % 9

def verify_division(dividend, divisor, quotient, remainder):
    return digit_sum(dividend) == (digit_sum(divisor) * digit_sum(quotient) + digit_sum(remainder)) % 9
