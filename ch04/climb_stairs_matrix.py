import numpy as np
import numpy.linalg as lin


def climb_stairs(n: int) -> int:
    a = np.array([1, 1, 1, 1, 0, 0, 0, 1, 0], dtype="int64")
    a = a.reshape(3, 3)
    return lin.matrix_power(a, n)[0, 0]
