def kalana_factor(a: float, b: float, c: float) -> tuple:
    """Factor ax² + bx + c by using derivative relationships.
    Returns (root1, root2) or None."""
    if a == 0:
        return None
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return None
    import math
    sqrt_d = math.sqrt(discriminant)
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    return (x1, x2)
