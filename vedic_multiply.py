from anurupyena import anurupyena_multiply
from yavadunam import yavadunam_square
from urdhva_tiryagbhyam import urdhva_multiply
from nikhilam import nikhilam_multiply

def vedic_multiply(a: int, b: int) -> int:
    """
    Automatically select the most efficient Vedic multiplication method.
    Uses Nikhilam if both numbers are within 20% of a power of 10 (base),
    otherwise uses Urdhva Tiryagbhyam.
    """
    if a == 0 or b == 0:
        return 0
    # Try to find a suitable base for Nikhilam
    max_val = max(a, b)
    base = 1
    while base < max_val:
        base *= 10
    # Check if both numbers are within 20% of base
    threshold = base // 5  # 20% tolerance
    if abs(a - base) <= threshold and abs(b - base) <= threshold:
        return nikhilam_multiply(a, b, base)
    else:
        return urdhva_multiply(a, b)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        result = vedic_multiply(x, y)
        # Determine which sutra was used
        max_val = max(x, y)
        base = 1
        while base < max_val:
            base *= 10
        threshold = base // 5
        if abs(x - base) <= threshold and abs(y - base) <= threshold:
            sutra = "Nikhilam Navatashcaramam Dashatah"
        else:
            sutra = "Urdhva Tiryagbhyam"
        print(f"{x} × {y} = {result}")
        print(f"Sutra applied: {sutra}")
    else:
        print("Usage: python vedic_multiply.py <num1> <num2>")
