import numpy as np
from scipy.interpolate import BSpline


def generate_bsplines(time, k):
    """
    Generate a set of B-splines with knots c and degree k evaluated at t.
    """
    B = []
    dt = time[1] - time[0]
    knots = np.concatenate([np.flip([time[0] - (i + 1) * dt for i in range(k)]), time,
                            [time[-1] + (i + 1) * dt for i in range(k + 2)]])
    for i in range(len(knots) - 2 * k):
        b = BSpline.basis_element(knots[i:(i + k + 2)], False)
        val = b(time)
        B.append(val)

    B = np.nan_to_num(np.vstack(B))  # already adds up to 1

    return B
