#!/usr/bin/env python3
"""
Parāvartya Yojayet (Transpose and Apply)
Solves two-variable linear equations.
"""
def paravartya_solve(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ValueError("No unique solution.")
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 7:
        a1, b1, c1, a2, b2, c2 = map(float, sys.argv[1:])
        x, y = paravartya_solve(a1, b1, c1, a2, b2, c2)
        print(f"x = {x}, y = {y}")
    else:
        print("Demo: 2x + 3y = 8, 5x - y = 3")
        x, y = paravartya_solve(2, 3, 8, 5, -1, 3)
        print(f"x = {x}, y = {y}")
