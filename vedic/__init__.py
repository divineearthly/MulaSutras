"""
Vedic Mathematics Library
Ancient Sutras, Modern Python.
"""
# Multiply
from .multiply import (
    urdhva_multiply,
    nikhilam_multiply,
    anurupyena_multiply,
    ekanyunena_multiply,
    murti_multiply,
    antyayor_multiply,
    vedic_multiply,
)

# Divide
from .divide import nikhilam_divide, paravartya_divide

# Square
from .square import yavadunam_square

# Square root and Cube root
from .sqrt import vilokanam_sqrt, vilokanam_cuberoot

# Series & Prediction
from .prediction import (
    ekadhikena_sequence,
    ekadhikena_square,
    sum_of_naturals,
    sum_of_squares,
    sum_of_cubes,
)

# Verification
from .verify import (
    verify_multiplication,
    verify_division,
)

# Equations
from .solve import (
    sankalana_solve,
    paravartya_solve,
    lopana_solve,
    purana_solve,
    purana_cubic,
    factorise_quadratic,
)

# Calculus
from .algebra import chalana_derivative

# Geometry
from .geometry import triangle_area

# Compression
from .compress import shunyam_compress

# Fractions
from .fraction import recurring_to_fraction

# Proportion
from .proportion import proportion_solve

# Remainder
from .transcendental import remainder_by_10_power, sin_approx

# Convenience aliases
mul = vedic_multiply
div = nikhilam_divide
square = yavadunam_square
sqrt = vilokanam_sqrt
cuberoot = vilokanam_cuberoot
predict = ekadhikena_sequence
compress = shunyam_compress
