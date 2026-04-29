from urdhva_tiryagbhyam import urdhva_multiply
from nikhilam import nikhilam_multiply
from anurupyena import anurupyena_multiply
from yavadunam import yavadunam_square

def vedic_multiply(a: int, b: int = None) -> int:
    """
    The intelligent Vedic multiplier.
    - If a single argument is given, returns its square using Yavadunam.
    - Otherwise selects the best multiplication Sutra.
    """
    # Square mode
    if b is None:
        return yavadunam_square(a)

    if a == 0 or b == 0:
        return 0

    # Determine the natural base (power of 10) for the larger number
    max_val = max(a, b)
    base = 1
    while base < max_val:
        base *= 10

    # 1. Nikhilam: if both numbers are within 20% of the same base
    threshold = base // 5
    if abs(a - base) <= threshold and abs(b - base) <= threshold:
        return nikhilam_multiply(a, b, base)

    # 2. Anurupyena: if one number is close to half or double of a base
    #    (scaling factor of 2 or 1/2)
    half_base = base // 2
    if (abs(a - half_base) <= threshold and abs(b - base) <= threshold) or \
       (abs(b - half_base) <= threshold and abs(a - base) <= threshold):
        return anurupyena_multiply(a, b)

    # 3. Default: Urdhva Tiryagbhyam
    return urdhva_multiply(a, b)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
        result = vedic_multiply(x)
        print(f"{x}² = {result}")
    elif len(sys.argv) == 3:
        x, y = map(int, sys.argv[1:])
        result = vedic_multiply(x, y)
        print(f"{x} × {y} = {result}")
        # Determine sutra used
        max_val = max(x, y)
        base = 1
        while base < max_val:
            base *= 10
        threshold = base // 5
        half_base = base // 2
        if abs(x - base) <= threshold and abs(y - base) <= threshold:
            sutra = "Nikhilam Navatashcaramam Dashatah"
        elif (abs(x - half_base) <= threshold and abs(y - base) <= threshold) or \
             (abs(y - half_base) <= threshold and abs(x - base) <= threshold):
            sutra = "Anurupyena"
        else:
            sutra = "Urdhva Tiryagbhyam"
        print(f"Sutra applied: {sutra}")
    else:
        print("Usage: python vedic_multiply.py <num>   (square)")
        print("       python vedic_multiply.py <num1> <num2>  (multiply)")
