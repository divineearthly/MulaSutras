#!/usr/bin/env python3
"""
Vedic Processor: Intelligent dispatcher for all 19 Sutras.
Supports: mul, div, square, sqrt, mul9, verify, predict, compress,
          solve2, solve_lin, quadratic, derivative, factor, solve3, proportion
"""

from vilokanam_cube import vilokanam_cuberoot
from sesanyankena import remainder_by_10_power
from sopantyadvayamantyam import sin_approx
from digit_sum_verify_division import verify_division
from purana_cubic import purana_cubic
from ekadhikena_series import sum_of_naturals, sum_of_squares, sum_of_cubes
from recurring_fraction import recurring_to_fraction
from murti_gunaka import murti_multiply
from antyayor import antyayor_multiply
from vyasti_samasti import triangle_area
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
from purana import purana_solve
from chalana import chalana_derivative
from adyamadya import factorise_quadratic
from lopana import lopana_solve
from gunaka import proportion_solve

def vedic_multiply(a, b):
    """Intelligent multiplier dispatching among Urdhva, Nikhilam, Anurupyena, Ekanyunena."""
    if a == 0 or b == 0:
        return 0
    max_val = max(a, b)
    base = 1
    while base < max_val:
        base *= 10
    threshold = base // 5
    if abs(a - base) <= threshold and abs(b - base) <= threshold:
        return nikhilam_multiply(a, b, base)
    half_base = base // 2
    if (abs(a - half_base) <= threshold and abs(b - base) <= threshold) or \
       (abs(b - half_base) <= threshold and abs(a - base) <= threshold):
        return anurupyena_multiply(a, b)
    str_b = str(b)
    if str_b == '9' * len(str_b):
        return multiply_by_9s(a, len(str_b))
    str_a = str(a)
    if str_a == '9' * len(str_a):
        return multiply_by_9s(b, len(str_a))
    return urdhva_multiply(a, b)

def vedic_process(operation, *args):
    """Dispatch to the correct Vedic Sutra based on operation string."""
    if operation == "mul":
        return vedic_multiply(args[0], args[1])
    elif operation == "div":
        a, b = args[0], args[1]
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
    elif operation == "cuberoot":
        return vilokanam_cuberoot(args[0])
    elif operation == "last_n":
        return remainder_by_10_power(args[0], args[1])
    elif operation == "sin":
        return sin_approx(args[0])
    elif operation == "verify_div":
        return verify_division(args[0], args[1], args[2], args[3])
    elif operation == "cubic":
        return purana_cubic(args[0], args[1])
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
    elif operation == "quadratic":
        return purana_solve(args[0], args[1], args[2])
    elif operation == "derivative":
        return chalana_derivative(list(args))
    elif operation == "factor":
        return factorise_quadratic(args[0], args[1])
    elif operation == "solve3":
        eq1 = tuple(args[0:4])
        eq2 = tuple(args[4:8])
        eq3 = tuple(args[8:12])
        return lopana_solve(eq1, eq2, eq3)
    elif operation == "proportion":
        return proportion_solve(*args)
    elif operation == "sum_n":
        return sum_of_naturals(args[0])
    elif operation == "sum_sq":
        return sum_of_squares(args[0])
    elif operation == "sum_cu":
        return sum_of_cubes(args[0])
    elif operation == "recur_frac":
        return recurring_to_fraction(args[0], args[1])
    elif operation == "murti":
        return murti_multiply(args[0], args[1])
    elif operation == "antyayor":
        return antyayor_multiply(args[0], args[1])
    elif operation == "tri_area":
        return triangle_area(args[0], args[1], args[2])
    else:
        raise ValueError(f"Unknown operation: {operation}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Vedic Processor – Available operations:")
        print("  mul a b, div a b, square a, sqrt a, mul9 a nines")
        print("  verify a b prod, predict seed n, compress text")
        print("  solve2 sum diff, solve_lin a1 b1 c1 a2 b2 c2")
        print("  quadratic a b c, derivative c1 c2 ..., factor b c")
        print("  solve3 a1 b1 c1 d1 ... a3 b3 c3 d3, proportion a b c d (?=missing)")
        print("  sum_n n, sum_sq n, sum_cu n — sum of naturals, squares, cubes")
        print("  recur_frac i rep — recurring decimal to fraction")
        print("  murti a b, antyayor a b — special Vedic multiplications")
        print("  tri_area a b c — triangle area")
        print("  cuberoot n — cube root of perfect cube")
        print("  last_n num n — last n digits (remainder by 10^n)")
        print("  sin x — sine approximation")
        print("  verify_div div dvs q r — verify division via digit sums")
        print("  cubic a b — solve x³ + a x = b")
        print("\nDemo:")
        print("  cuberoot 405224 =", vedic_process("cuberoot", 405224))
        print("  last_n 123456 3 =", vedic_process("last_n", 123456, 3))
        print("  sin 0.5 =", vedic_process("sin", 0.5))
        print("  verify_div 12345 98 125 95 =", vedic_process("verify_div", 12345, 98, 125, 95))
        print("  cubic 6 20 =", vedic_process("cubic", 6, 20))
        print("  sum_n 5 =", vedic_process("sum_n", 5))
        print("  recur_frac 0 142857 =", vedic_process("recur_frac", 0, "142857"))
        print("  murti 43 63 =", vedic_process("murti", 43, 63))
        print("  antyayor 37 33 =", vedic_process("antyayor", 37, 33))
        print("  tri_area 3 4 5 =", vedic_process("tri_area", 3, 4, 5))
        print("  98*97 =", vedic_process("mul", 98, 97))
        print("  12345/98 =", vedic_process("div", 12345, 98))
        print("  96² =", vedic_process("square", 96))
        print("  √8281 =", vedic_process("sqrt", 8281))
        print("  23*99 =", vedic_process("mul9", 23, 2))
        print("  verify 23*45=1035:", vedic_process("verify", 23, 45, 1035))
        print("  predict from 1:", vedic_process("predict", 1, 10))
        print("  compress 'Vedic Vedic':", vedic_process("compress", "Vedic Vedic Pattern")[0])
        print("  solve2 100 20:", vedic_process("solve2", 100, 20))
        print("  solve_lin 2 3 8 5 -1 3:", vedic_process("solve_lin", 2, 3, 8, 5, -1, 3))
        print("  quadratic 1 -5 6:", vedic_process("quadratic", 1, -5, 6))
        print("  derivative 3 5 2:", vedic_process("derivative", 3, 5, 2))
        print("  factor 5 6:", vedic_process("factor", 5, 6))
        print("  solve3 1 1 1 6 2 -1 1 3 1 2 -1 2:", vedic_process("solve3", 1,1,1,6,2,-1,1,3,1,2,-1,2))
        print("  proportion 2 3 4 ?:", vedic_process("proportion", 2, 3, 4, None))
    else:
        op = sys.argv[1]
        args = []
        for x in sys.argv[2:]:
            if x == '?':
                args.append(None)
            elif x.lstrip('-').isdigit():
                args.append(int(x))
            else:
                try:
                    args.append(float(x))
                except ValueError:
                    args.append(x)
        result = vedic_process(op, *args)
        print(result)
