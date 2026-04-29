#!/usr/bin/env python3
"""
Anurupyena (Proportionately)
Scale one number to a convenient base, multiply, then descale.
Useful when both numbers are near different powers of 10.
"""
def anurupyena_multiply(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    # Choose a base and scaling factors
    # Scale big number down to base range
    import math
    m = max(a, b)
    base = 10 ** (len(str(m)) - 1)
    # Find scaling factors
    fa = a / base
    fb = b / base
    # Multiply scaled numbers and scale back
    return round((fa * fb) * (base * base))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        x, y = map(int, sys.argv[1:])
        print(f"{x} × {y} = {anurupyena_multiply(x, y)}")
    else:
        print("Demo: 1234 × 1005")
        print(anurupyena_multiply(1234, 1005))
