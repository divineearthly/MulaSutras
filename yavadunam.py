#!/usr/bin/env python3
"""
Yavadunam (As much deficiency)
Squaring and cubing of numbers near a base (power of 10).
"""
def yavadunam_square(n: int) -> int:
    """Square a number near a base (exact for numbers close to power of 10)."""
    base = 10 ** (len(str(n)) - 1)
    diff = n - base
    left = n + diff
    right = diff ** 2
    # Format right part with leading zeros matching base length
    zeros = len(str(base)) - 1
    right_str = str(right).zfill(zeros)[-zeros:]
    return int(str(left) + right_str)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
        print(f"{x}² = {yavadunam_square(x)}")
    else:
        print("Demo: 96², 1005²")
        print(yavadunam_square(96))
        print(yavadunam_square(1005))
