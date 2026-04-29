#!/usr/bin/env python3
"""
Puranapuranabhyam for Cubics
Solve reduced cubic: x³ + a x = b.
"""
import math

def purana_cubic(a: float, b: float) -> float:
    """Return one real root of x³ + a x = b."""
    # Vedic method: write x = u - a/(3u) and solve
    # For depressed cubic, we can use the direct formula
    # But we'll use a simpler iterative approximation for spirit
    x = b ** (1/3) if b >= 0 else -((-b)**(1/3))
    for _ in range(10):
        x = (b - x**3) / a if a != 0 else x
    return x
