#!/usr/bin/env python3
"""
Sopantyadvayamantyam (Ultimate and penultimate)
Approximate sin(x) for small x using Vedic truncated series.
Formula: sin(x) ≈ x - x^3/6 + x^5/120
"""
import math

def sin_approx(x: float) -> float:
    return x - (x**3)/6 + (x**5)/120

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        x = float(sys.argv[1])
        print(f"sin({x}) ≈ {sin_approx(x)} (true: {math.sin(x)})")
    else:
        print("Demo: sin(0.5) ≈", sin_approx(0.5), "(true: math.sin(0.5))")
