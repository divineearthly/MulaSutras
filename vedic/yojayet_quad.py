def solve_simultaneous_quadratics(a1, b1, c1, d1, a2, b2, c2, d2):
    """
    Solve:
      a1*x² + b1*y² + c1*x + d1*y = 0
      a2*x² + b2*y² + c2*x + d2*y = 0
    (Returns one real solution pair if simple; placeholder for now)
    """
    # For demo, assume both are simple with no squared terms (degenerate to linear)
    if a1 == 0 and b1 == 0 and a2 == 0 and b2 == 0:
        # linear in x,y
        det = c1*d2 - c2*d1
        if det == 0:
            return None
        x = (0*b2 - 0*d2) / det  # not correct general, but placeholder
        y = (c1*0 - c2*0) / det
        return (x, y)
    return None
