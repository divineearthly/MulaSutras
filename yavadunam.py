#!/usr/bin/env python3
"""
Yavadunam (As much deficiency)
Square numbers near the NEAREST power of 10.
"""
def yavadunam_square(n: int) -> int:
    if n == 0:
        return 0
    # Find nearest base (power of 10)
    import math
    power = round(math.log10(abs(n)))
    base = 10 ** power
    # If number is closer to the next power, use that
    if abs(n - base) > abs(n - base * 10):
        base *= 10
    diff = n - base
    left = n + diff
    right = diff * diff
    zeros = len(str(base)) - 1
    right_str = str(right).zfill(zeros)[-zeros:]
    return int(str(left) + right_str)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
        print(f"{x}² = {yavadunam_square(x)}")
    else:
        print("Demo: 96² =", yavadunam_square(96))
        print("Demo: 1005² =", yavadunam_square(1005))
