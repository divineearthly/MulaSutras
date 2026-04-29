#!/usr/bin/env python3
"""
Urdhva Tiryagbhyam (Vertically and Crosswise) Multiplier
Pure Python implementation for arbitrary-length integers.
"""

def urdhva_multiply(a: int, b: int) -> int:
    """Multiply two non-negative integers using the Vedic Sutra."""
    if a == 0 or b == 0:
        return 0
    # Convert to strings for digit-wise access
    str_a = str(a)
    str_b = str(b)
    len_a = len(str_a)
    len_b = len(str_b)
    # Result length can be up to len_a + len_b
    result = [0] * (len_a + len_b)
    
    # Iterate over each digit pair using the crosswise pattern
    for i in range(len_a):
        for j in range(len_b):
            digit_a = int(str_a[len_a - 1 - i])  # from rightmost
            digit_b = int(str_b[len_b - 1 - j])  # from rightmost
            result[i + j] += digit_a * digit_b
            # Carry handling
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Remove leading zeros from the result list
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    # Convert back to integer
    return int(''.join(map(str, reversed(result))))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(f"{x} × {y} = {urdhva_multiply(x, y)}")
    else:
        print("Usage: python urdhva_tiryagbhyam.py <num1> <num2>")
