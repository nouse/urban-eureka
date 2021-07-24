import numpy as np
import numpy.linalg as lin


def fib(n: int) -> int:
    a = np.array([1, 1, 1, 0], dtype=np.int64)
    a = a.reshape(2, 2)
    return lin.matrix_power(a, n - 1)[0, 0]
