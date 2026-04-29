# File: ekanyunena.py
def multiply_by_9s(n: int, nines: int) -> int:
    """Multiply n by 9, 99, 999, etc. using 'one less than the previous'."""
    right = int(str(10**nines - 1 - (n - 1)))  # complement
    left = n - 1
    return int(f"{left}{right}")
