# File: vilokanam.py
def vilokanam_sqrt(n: int) -> int:
    """Return integer square root by observation (works for perfect squares)."""
    last_digit = n % 10
    # Mapping of last digit to possible root endings
    end_map = {0:0,1:1,4:2,9:3,6:4,5:5,6:6,9:7,4:8,1:9}
    possible = [x for x in range(10) if (x*x)%10 == last_digit]
    # Narrow using rough estimate
    est = int(n**0.5)
    for i in range(est-5, est+6):
        if i*i == n:
            return i
    return est
