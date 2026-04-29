import math

def log_approx(x: float, terms: int = 5) -> float:
    """Approximate ln(1+x) using the Vedic series: x - x²/2 + x³/3 - ..."""
    result = 0
    for n in range(1, terms + 1):
        term = (x ** n) / n
        if n % 2 == 0:
            result -= term
        else:
            result += term
    return result

if __name__ == "__main__":
    for x in [0.5, 1.0, 2.0]:
        print(f"ln(1+{x}) ≈ {log_approx(x):.6f} (true: {math.log(1+x):.6f})")
