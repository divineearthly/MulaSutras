#!/usr/bin/env python3
"""
Vedic Pipeline: Unifies all Sutras for data processing.
Input: CSV file with numbers.
Output: Compressed data, prediction, and constraint solving.
"""

import csv, sys
from shunyam import shunyam_compress
from ekadhikena import ekadhikena_sequence
from paravartya import paravartya_solve
from sankalana import sankalana_solve
from vedic_multiply import vedic_multiply

def process_csv(filename):
    nums = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for val in row:
                try: nums.append(float(val))
                except ValueError: pass
    return nums

def main():
    if len(sys.argv) < 2:
        print("Usage: python vedic_pipeline.py <data.csv>")
        # Demo mode
        sample = [10, 20, 30, 40, 50]
        print(f"Sample data: {sample}")
        text = str(sample)
        comp, d = shunyam_compress(text)
        print(f"Compressed: {comp[:80]}...")
        seed = int(sample[-1])
        predicted = ekadhikena_sequence(seed, 3)[-1]
        print(f"Ekadhikena prediction from {seed}: {predicted}")
        # Use sunkalan for sum/diff if only two values
        if len(sample) >= 2:
            s = sample[-2] + sample[-1]
            d = sample[-1] - sample[-2]
            x, y = sankalana_solve(s, d)
            print(f"Sankalana: x+y={s}, x-y={d} → x={x}, y={y}")
        return

    filename = sys.argv[1]
    nums = process_csv(filename)
    print(f"Loaded {len(nums)} numbers.")
    if len(nums) < 2:
        return
    text = str(nums)
    comp, d = shunyam_compress(text)
    print(f"Compressed: {len(comp)} bytes (was {len(text)})")
    seed = int(nums[-1])
    predicted = ekadhikena_sequence(seed, 3)[-1]
    print(f"Predicted next: {predicted}")
    # Example constraint solving
    last = nums[-1]
    # If only two numbers, use Sankalana
    if len(nums) == 2:
        x, y = sankalana_solve(nums[0]+nums[1], nums[1]-nums[0])
        print(f"Sankalana solution: x={x}, y={y}")
    else:
        # Use Paravartya as before
        try:
            x, y = paravartya_solve(1, 1, predicted, 2, -1, last)
            print(f"Paravartya solution: x={x}, y={y}")
        except ValueError:
            print("No unique Paravartya solution.")

if __name__ == "__main__":
    main()
