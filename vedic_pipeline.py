#!/usr/bin/env python3
"""
Vedic Pipeline: Unifies Shunyam, Ekadhikena, and Paravartya for data processing.
Input: CSV file with numbers (one per line or comma-separated).
Output: Compressed data, next predicted value, and constraint check.
"""

import csv
import sys
from shunyam import shunyam_compress
from ekadhikena import ekadhikena_sequence
from paravartya import paravartya_solve

def process_csv(filename):
    """Read numbers from CSV, return list of floats."""
    nums = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for val in row:
                try:
                    nums.append(float(val))
                except ValueError:
                    pass
    return nums

def main():
    if len(sys.argv) < 2:
        print("Usage: python vedic_pipeline.py <data.csv>")
        # Demo mode
        print("\nDemo mode: generating sample data...")
        # Create sample data
        sample = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        print(f"Sample data: {sample}")
        # Shunyam on text representation
        text = str(sample)
        comp, d = shunyam_compress(text)
        print(f"Compressed representation: {comp[:80]}...")
        # Ekadhikena prediction from last number
        seed = int(sample[-1])
        seq = ekadhikena_sequence(seed, 3)
        predicted = seq[-1]
        print(f"Next predicted value (Ekadhikena from {seed}): {predicted}")
        # Paravartya constraint: check if predicted fits a simple linear balance
        # Suppose we want x + 2*y = predicted, and 3*x - y = last_actual
        # Solve for x,y:
        last_actual = sample[-1]
        try:
            x, y = paravartya_solve(1, 2, predicted, 3, -1, last_actual)
            print(f"Constraint solution: x={x}, y={y}")
            print(f"Check: 1*{x} + 2*{y} = {1*x+2*y} (should be {predicted})")
        except ValueError:
            print("No unique solution for constraint.")
        return

    filename = sys.argv[1]
    nums = process_csv(filename)
    print(f"Loaded {len(nums)} numbers.")
    if len(nums) < 2:
        print("Need at least 2 numbers.")
        return
    # Shunyam compression on the text representation
    text = str(nums)
    comp, d = shunyam_compress(text)
    print(f"Compressed size: {len(comp)} bytes (original: {len(text)} bytes)")
    # Ekadhikena prediction using last number as seed
    seed = int(nums[-1])
    seq = ekadhikena_sequence(seed, 3)
    predicted = seq[-1]
    print(f"Next predicted value: {predicted}")
    # Paravartya: simple linear constraint between last actual and predicted
    last_actual = nums[-1]
    # Example: x + y = predicted, 2x - y = last_actual
    try:
        x, y = paravartya_solve(1, 1, predicted, 2, -1, last_actual)
        print(f"Constraint solution: x={x}, y={y}")
    except ValueError:
        print("Constraint not uniquely solvable.")

if __name__ == "__main__":
    main()
