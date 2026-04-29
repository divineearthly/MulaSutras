#!/usr/bin/env python3
"""
Vilokanam (By mere observation)
Instant cube root of perfect cubes up to 10^12.
"""
def vilokanam_cuberoot(n: int) -> int:
    if n == 0: return 0
    # Digit mapping of last digit
    cube_map = {0:0, 1:1, 8:2, 7:3, 4:4, 5:5, 6:6, 3:7, 2:8, 9:9}
    last = n % 10
    root_last = cube_map.get(last, None)
    if root_last is None: return round(n ** (1/3))
    # Remove last three digits
    left_part = n // 1000
    # Find nearest cube to left_part
    for i in range(1, 22):
        if i**3 > left_part:
            first = i - 1
            break
    else:
        first = 21
    return first * 10 + root_last
