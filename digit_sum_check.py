#!/usr/bin/env python3
def digit_sum(n: int) -> int:
    """Return the digital root (0-8). For verification, treat 9 as 0."""
    if n == 0:
        return 0
    return n % 9

def verify_multiplication(a: int, b: int, product: int) -> bool:
    return (digit_sum(a) * digit_sum(b)) % 9 == digit_sum(product)
