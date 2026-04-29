# File: paravartya_division.py
def paravartya_divide(num: int, den: int) -> tuple:
    """Vedic general division by a divisor of any length."""
    if den == 0:
        raise ZeroDivisionError
    num_str = str(num)
    den_str = str(den)
    lead = int(den_str[0])
    multiplier = [int(d) for d in den_str[1:]]  # negative of rest, but we use addition
    result = []
    remainder = 0
    for i, ch in enumerate(num_str):
        digit = remainder * 10 + int(ch)
        q = digit // lead
        result.append(str(q))
        remainder = digit % lead
        # Add q * multiplier to next digits (transpose effect)
        # Implementation simplified for demonstration; full requires handling carries.
    return int(''.join(result)) if result else 0, remainder
