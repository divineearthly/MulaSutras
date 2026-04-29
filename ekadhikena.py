#!/usr/bin/env python3
"""
Ekadhikena Purvena (By one more than the previous one)
Sutra for squaring numbers ending in 5, and generating recursive sequences.
"""

def ekadhikena_square(n: int) -> int:
    """
    Square a number ending in 5 using Ekadhikena Purvena.
    Works for integers ending in 5 only.
    """
    if n % 10 != 5:
        raise ValueError("Ekadhikena square method requires a number ending in 5.")
    # Remove the last digit (5)
    previous = n // 10
    # Multiply previous by one more than previous
    left = previous * (previous + 1)
    # Append 25
    return int(str(left) + "25")


def ekadhikena_sequence(seed: int, steps: int = 10) -> list:
    """
    Generate a recursive sequence where each term is:
    a_n = a_{n-1} + (one more than the previous term's first digit)
    This demonstrates the recursive prediction principle.
    """
    seq = [seed]
    for _ in range(steps):
        prev = seq[-1]
        # Extract first digit
        first_digit = int(str(prev)[0])
        next_val = prev + (first_digit + 1)
        seq.append(next_val)
    return seq


def recurring_decimal_to_fraction(integer_part: int, recurring_digits: str) -> tuple:
    """
    Convert a recurring decimal to fraction using Ekadhikena principle.
    Example: 0.142857142857... where 142857 repeats.
    Uses the formula: (recurring part) / (10^n - 1)
    The denominator has as many 9s as the length of the recurring part.
    """
    n = len(recurring_digits)
    numerator = int(recurring_digits)
    denominator = int("9" * n)
    # Add integer part
    numerator = integer_part * denominator + numerator
    return numerator, denominator


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        mode = sys.argv[1]
        if mode == "square" and len(sys.argv) == 3:
            n = int(sys.argv[2])
            try:
                result = ekadhikena_square(n)
                print(f"{n}² = {result} (Ekadhikena Purvena)")
            except ValueError as e:
                print(f"Error: {e}")
        elif mode == "sequence" and len(sys.argv) == 3:
            seed = int(sys.argv[2])
            seq = ekadhikena_sequence(seed, 15)
            print(f"Ekadhikena sequence from {seed}: {seq}")
        elif mode == "fraction" and len(sys.argv) >= 3:
            int_part = int(sys.argv[2]) if len(sys.argv) >= 3 else 0
            recurring = sys.argv[3] if len(sys.argv) >= 4 else "142857"
            num, den = recurring_decimal_to_fraction(int_part, recurring)
            print(f"0.{recurring}{recurring}... = {num}/{den}")
        else:
            print("Usage:")
            print("  python ekadhikena.py square <number_ending_in_5>")
            print("  python ekadhikena.py sequence <seed>")
            print("  python ekadhikena.py fraction <integer_part> <recurring_digits>")
    else:
        # Demo
        print("Ekadhikena Purvena - Demo")
        print(f"25² = {ekadhikena_square(25)}")
        print(f"105² = {ekadhikena_square(105)}")
        print(f"9995² = {ekadhikena_square(9995)}")
        print(f"\nSequence from seed 1: {ekadhikena_sequence(1, 10)}")
        print(f"Sequence from seed 7: {ekadhikena_sequence(7, 10)}")
        num, den = recurring_decimal_to_fraction(0, "142857")
        print(f"\n0.142857142857... = {num}/{den}")
