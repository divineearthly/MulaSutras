**Author:** Joydeep Das
**Date:** [29-Mar-2026]
**Repository:** MulaSutras on Termux

## Abstract
We implement the Vedic Mathematics sutra "Urdhva Tiryagbhyam" for arbitrary-length integer multiplication in Python. We demonstrate that the algorithm is functionally correct and analyze its execution time against Python's built-in multiplication for numbers of varying lengths. The pattern of digit operations is inherently parallel, suggesting a path toward energy-efficient hardware multipliers.

## Benchmark Results
| Digits  Vedic (s)       Built-in (s)    Ratio (Vedic/Built-in)
10      0.000138        0.000003        40.8511
50      0.002563        0.000004        723.5347
100     0.007419        0.000003        2544.2424
200     0.036418        0.000004        8741.7438
500     0.284238        0.000011        26492.5286
## Conclusion
The Vedic multiplier exhibits a predictable O(n^2) digit product count, identical to the classic algorithm, but with a unique structure that maps naturally to parallel processing units. Further implementation in hardware description languages or SIMD-optimized C is warranted.

## Keywords
Vedic Mathematics, Urdhva Tiryagbhyam, Parallel Multiplication, Ancient Algorithms
