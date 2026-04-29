#!/usr/bin/env python3
"""
C Benchmark: Urdhva Tiryagbhyam (C implementation) vs Python Built-in *
"""

import time
import random
import ctypes

# Load the shared library
urdhva_lib = ctypes.CDLL('./urdhva.so')

# Define function signatures
urdhva_lib.urdhva_multiply_c.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
urdhva_lib.urdhva_multiply_c.restype = ctypes.c_void_p

urdhva_lib.free_urdhva_string.argtypes = [ctypes.c_void_p]
urdhva_lib.free_urdhva_string.restype = None

def c_urdhva_multiply(a: int, b: int) -> int:
    """Multiply two non-negative integers using the C Urdhva Tiryagbhyam."""
    a_str = str(a).encode('utf-8')
    b_str = str(b).encode('utf-8')
    ptr = urdhva_lib.urdhva_multiply_c(a_str, b_str)
    if not ptr:
        raise MemoryError("C function returned NULL")
    result_str = ctypes.c_char_p(ptr).value.decode('utf-8')
    urdhva_lib.free_urdhva_string(ptr)  # free C memory
    return int(result_str)

def builtin_multiply(a, b):
    return a * b

def run_test(num_digits):
    a = random.randint(10**(num_digits-1), 10**num_digits - 1)
    b = random.randint(10**(num_digits-1), 10**num_digits - 1)
    
    # Time C Urdhva
    start = time.perf_counter()
    c_result = c_urdhva_multiply(a, b)
    c_time = time.perf_counter() - start
    
    # Time built-in
    start = time.perf_counter()
    py_result = builtin_multiply(a, b)
    py_time = time.perf_counter() - start
    
    assert c_result == py_result, f"Mismatch: {c_result} vs {py_result}"
    return c_time, py_time

if __name__ == "__main__":
    print("Digits\tC Urdhva (s)\tPython Built-in (s)\tSpeedup (x)")
    for digits in [10, 50, 100, 200, 500, 1000]:
        c_t, py_t = run_test(digits)
        speedup = py_t / c_t if c_t > 0 else float('inf')
        print(f"{digits}\t{c_t:.6f}\t\t{py_t:.6f}\t\t{speedup:.2f}")
