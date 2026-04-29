import time
import random
from urdhva_tiryagbhyam import urdhva_multiply

def builtin_multiply(a, b):
    return a * b

def run_test(num_digits):
    """Generate two random integers with given digit lengths and measure both methods."""
    a = random.randint(10**(num_digits-1), 10**num_digits - 1)
    b = random.randint(10**(num_digits-1), 10**num_digits - 1)
    
    # Time Vedic
    start = time.perf_counter()
    vedic_result = urdhva_multiply(a, b)
    vedic_time = time.perf_counter() - start
    
    # Time built-in
    start = time.perf_counter()
    builtin_result = builtin_multiply(a, b)
    builtin_time = time.perf_counter() - start
    
    # Verify correctness
    assert vedic_result == builtin_result, "Mismatch! Implementation error."
    
    return vedic_time, builtin_time

if __name__ == "__main__":
    print("Digits\tVedic (s)\tBuilt-in (s)\tRatio (Vedic/Built-in)")
    for digits in [10, 50, 100, 200, 500]:
        v_time, b_time = run_test(digits)
        ratio = v_time / b_time if b_time > 0 else float('inf')
        print(f"{digits}\t{v_time:.6f}\t{b_time:.6f}\t{ratio:.4f}")
