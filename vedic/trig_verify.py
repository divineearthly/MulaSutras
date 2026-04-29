from .transcendental import sin_approx
from .cos_approx import cos_approx

def verify_sin2_cos2(x: float, tol: float = 1e-4) -> bool:
    return abs(sin_approx(x)**2 + cos_approx(x)**2 - 1.0) < tol
