#!/usr/bin/env python3
"""
Sankalana-Vyavakalanabhyam (By Addition and Subtraction)
Solves: x + y = S, x - y = D  (or any linear combination with pattern)
"""
def sankalana_solve(sum_val, diff_val):
    """Return (x, y) from x+y = sum, x-y = diff."""
    x = (sum_val + diff_val) / 2
    y = (sum_val - diff_val) / 2
    return x, y

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        s, d = map(float, sys.argv[1:])
        x, y = sankalana_solve(s, d)
        print(f"x + y = {s}, x - y = {d} → x = {x}, y = {y}")
    else:
        print("Demo: sum=100, diff=20")
        x, y = sankalana_solve(100, 20)
        print(f"x = {x}, y = {y}")
