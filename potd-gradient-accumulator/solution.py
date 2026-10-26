from fractions import Fraction
def gradient_accumulator(
    theta: float, eta: float, microbatches: list[tuple[int, float]]
) -> tuple[float, float]:
    """
    microbatches: list of (n_j, g_j) pairs, n_j examples with mean
    gradient g_j.

    g = sum(n_j * g_j) / sum(n_j)   (example-weighted mean, NOT the mean
    of the microbatch means).
    theta' = theta - eta * g.

    Return (g, theta_prime).
    """
    # TODO: weight by example count, divide exactly once.
    if not microbatches:
        return ValueError("need at least one microbatch")
    ratios = []
    max_e = 0
    total_n = 0
    for n, g_j in microbatches:
        if n <= 0:
            raise ValueError("microbatch must be positive")
        p, q = float(g_j).as_integer_ratio()
        e = q.bit_length()-1
        ratios.append((n, p, e))
        max_e = max(max_e, e)
        total_n += n

    num = 0
    for n, p, e in ratios:
        num += n*p << (max_e - e)

    g = Fraction(num, total_n << max_e)
    theta_prime = Fraction(theta) - Fraction(eta)*g
    return float(g), float(theta_prime)
    pass
