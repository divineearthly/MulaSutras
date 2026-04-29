#!/usr/bin/env python3
"""
Vedic Processor: Intelligent dispatcher for all 14 Sutras.
Supports: mul, div, square, sqrt, multiply_by_9s, verify, predict, compress, solve
"""

from urdhva_tiryagbhyam import urdhva_multiply
from nikhilam import nikhilam_multiply
from anurupyena import anurupyena_multiply
from yavadunam import yavadunam_square
from nikhilam_division import nikhilam_divide
from paravartya_division import paravartya_divide
from ekanyunena import multiply_by_9s
from digit_sum_check import digit_sum, verify_multiplication
from vilokanam import vilokanam_sqrt
from ekadhikena import ekadhikena_square, ekadhikena_sequence
from shunyam import shunyam_compress
from paravartya import paravartya_solve
from sankalana import sankalana_solve

def vedic_process(operation, *args):
    """
    Dispatch to the correct Vedic Sutra based on operation string.
    Supported operations:
      mul a b       -> intelligent multiply
      div a b       -> Nikhilam or Paravartya division
      square a      -> Yavadunam square
      sqrt a        -> Vilokanam square root (perfect squares)
      mul9 a b      -> multiply a by 9, 99, 999... (b = number of 9s)
      verify a b c  -> check a*b == c via digit sums
      predict seed n-> Ekadhikena sequence prediction
      compress text -> Shunyam compression
      solve2 s d    -> Sankalana solve x+y=s, x-y=d
      solve_lin a1 b1 c1 a2 b2 c2 -> Paravartya linear solve
    """
    if operation == "mul":
        return vedic_multiply(args[0], args[1])
    elif operation == "div":
        a, b = args[0], args[1]
        # Use Nikhilam if divisor near a power of 10
        base = 10 ** len(str(b))
        if abs(base - b) <= base // 5:
            return nikhilam_divide(a, b)
        else:
            return paravartya_divide(a, b)
    elif operation == "square":
        return yavadunam_square(args[0])
    elif operation == "sqrt":
        return vilokanam_sqrt(args[0])
    elif operation == "mul9":
        return multiply_by_9s(args[0], args[1])
    elif operation == "verify":
        return verify_multiplication(args[0], args[1], args[2])
    elif operation == "predict":
        return ekadhikena_sequence(args[0], args[1])
    elif operation == "compress":
        return shunyam_compress(args[0])
    elif operation == "solve2":
        return sankalana_solve(args[0], args[1])
    elif operation == "solve_lin":
        return paravartya_solve(args[0], args[1], args[2], args[3], args[4], args[5])
    else:
        raise ValueError(f"Unknown operation: {operation}")

# Import the intelligent multiplier here to avoid circular import
def vedic_multiply(a, b):
    if a == 0 or b == 0: return 0
    max_val = max(a, b)
    base = 1
    while base < max_val: base *= 10
    threshold = base // 5
    if abs(a - base) <= threshold and abs(b - base) <= threshold:
        return nikhilam_multiply(a, b, base)
    half_base = base // 2
    if (abs(a - half_base) <= threshold and abs(b - base) <= threshold) or \
       (abs(b - half_base) <= threshold and abs(a - base) <= threshold):
        return anurupyena_multiply(a, b)
    # Check if multiplying by 9s
    str_b = str(b)
    if str_b == '9' * len(str_b):
        return multiply_by_9s(a, len(str_b))
    str_a = str(a)
    if str_a == '9' * len(str_a):
        return multiply_by_9s(b, len(str_a))
    return urdhva_multiply(a, b)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Vedic Processor - Available operations:")
        print("  mul a b, div a b, square a, sqrt a, mul9 a nines")
        print("  verify a b product, predict seed n, compress text")
        print("  solve2 sum diff, solve_lin a1 b1 c1 a2 b2 c2")
        print("\nDemo:")
        print("  98*97 =", vedic_process("mul", 98, 97))
        print("  12345/98 =", vedic_process("div", 12345, 98))
        print("  96^2 =", vedic_process("square", 96))
        print("  sqrt(8281) =", vedic_process("sqrt", 8281))
        print("  23*99 =", vedic_process("mul9", 23, 2))
        print("  verify 23*45=1035:", vedic_process("verify", 23, 45, 1035))
        print("  predict from 1 (10 steps):", vedic_process("predict", 1, 10))
        print("  compress 'Vedic Vedic Pattern':", vedic_process("compress", "Vedic Vedic Pattern")[0])
        print("  solve x+y=100, x-y=20:", vedic_process("solve2", 100, 20))
        print("  solve 2x+3y=8, 5x-y=3:", vedic_process("solve_lin", 2, 3, 8, 5, -1, 3))
    else:
        op = sys.argv[1]
        args = [int(x) if x.lstrip('-').isdigit() else x for x in sys.argv[2:]]
        result = vedic_process(op, *args)
        print(result)
