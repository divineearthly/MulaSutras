#!/usr/bin/env python3
"""
Puranapuranabhyam for Cubics
Solve x³ + a·x = b  (depressed cubic). Returns the real root.
"""
import math

def purana_cubic(a: float, b: float) -> float:
    if a == 0:
        return b ** (1/3) if b >= 0 else -((-b) ** (1/3))
    # Vedic substitution: x = u - a/(3u)  leads to a quadratic in u³
    # u⁶ - b·u³ - (a/3)³ = 0
    a3 = a / 3.0
    discriminant = (b/2)**2 + (a3)**3
    if discriminant >= 0:
        sqrt_d = math.sqrt(discriminant)
        u_cube = b/2 + sqrt_d
        if u_cube < 0:
            u = -((-u_cube) ** (1/3))
        else:
            u = u_cube ** (1/3)
        x = u - a3 / u if u != 0 else b ** (1/3)
    else:
        # Three real roots; return the one given by trigonometric form
        r = math.sqrt(-a3**3)
        theta = math.acos(b / (2 * r)) if abs(b/(2*r)) <= 1 else 0
        x = 2 * math.sqrt(-a3) * math.cos(theta / 3)
    return x

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        a, b = map(float, sys.argv[1:])
        print(purana_cubic(a, b))
    else:
        print("Demo: x³ + 6x = 20 →", purana_cubic(6, 20))
        print("Demo: x³ + 3x = 14 →", purana_cubic(3, 14))
