def digit_sum(n: int) -> int:
    return 0 if n == 0 else n % 9

def verify_cube_root(n: int, root: int) -> bool:
    """Check if n is the cube of root using digit sums."""
    return digit_sum(n) == (digit_sum(root) ** 3) % 9
