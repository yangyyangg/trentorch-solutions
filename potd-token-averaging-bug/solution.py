import numpy as np


def valid_token_mean_loss(losses: np.ndarray, mask: np.ndarray) -> float:
    """
    losses: B x T array of per-token losses.
    mask: B x T array of 0/1 validity flags (same shape as losses).

    L = sum(mask * losses) / sum(mask)

    If sum(mask) == 0, return 0.0 (no division by zero).

    Return L as a float.
    """
    # TODO: sum only over valid tokens, in both numerator and denominator.
    losses = np.asarray(losses, dtype=np.float64)
    valid = np.asarray(mask) != 0
    if losses.shape != valid.shape:
        raise ValueError(f"shape mismatch: losses{losses.shape} vs mask {valid.shape}")
    count = int(np.count_nonzero(valid))
    if count == 0:
        return 0.0

    return float(losses[valid].sum() / count)
    pass
