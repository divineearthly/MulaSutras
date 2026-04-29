#!/usr/bin/env python3
"""
Nikhilam Navatashcaramam Dashatah (All from 9 and the last from 10)
Multiplier for numbers near a chosen base (power of 10).
"""

def nikhilam_multiply(a: int, b: int, base: int = None) -> int:
    """
    Multiply two integers using the Nikhilam Sutra.
    If base is not given, it automatically selects the smallest power of 10 >= max(a, b).
    """
    if a == 0 or b == 0:
        return 0

    # Auto-select base if not provided
    if base is None:
        base = 1
        while base < max(a, b):
            base *= 10

    da = a - base
    db = b - base

    left = a + db
    right = da * db

    zeros = len(str(base)) - 1

    if right < 0:
        # borrow 1 from left, add base to right
        left -= 1
        right += base
        right_str = str(right).zfill(zeros)[-zeros:]
    else:
        right_str = str(right).zfill(zeros)[-zeros:]

    return int(str(left) + right_str) if left >= 0 else -1


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        b = int(sys.argv[3]) if len(sys.argv) == 4 else None
        result = nikhilam_multiply(x, y, b)
        print(f"{x} x {y} = {result} (Nikhilam, base {b if b else 'auto'})")
    else:
        print("Usage: python nikhilam.py <num1> <num2> [base]")
