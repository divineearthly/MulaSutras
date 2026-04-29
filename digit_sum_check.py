# File: digit_sum_check.py
def digit_sum(n: int) -> int:
    s = n % 9
    return 9 if s == 0 else s

def verify_multiplication(a, b, product):
    return digit_sum(a) * digit_sum(b) % 9 == digit_sum(product)
