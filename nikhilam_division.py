# File: nikhilam_division.py
def nikhilam_divide(num: int, den: int) -> tuple:
    """Divide num by den when den is near a power of 10. Returns (quotient, remainder)."""
    base = 10 ** len(str(den))
    complement = base - den
    part = str(num)
    # Split num into parts matching base length
    if len(part) <= len(str(den)):
        return num // den, num % den
    left = int(part[:-len(str(den))]) if len(part) > len(str(den)) else 0
    right = int(part[-len(str(den)):]) if part[-len(str(den)):] else 0
    # Repeatedly multiply left by complement and add to right
    while left > 0:
        right += left * complement
        left = right // base
        right = right % base
    quotient = left
    remainder = right
    return quotient, remainder

if __name__ == "__main__":
    print(nikhilam_divide(12345, 98))  # near 100
