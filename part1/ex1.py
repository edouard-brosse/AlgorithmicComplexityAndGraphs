from typing import List
import numpy as np


def parcours(lst: List[float]) -> List[float]:  # O(n*log(n))
    left_houses = sorted([pos for pos in lst if pos < 0],
                         reverse=True)  # O(n*log(n))
    right_houses = sorted([pos for pos in lst if pos >= 0])  # O(n*log(n))
    if (len(left_houses) == 0):
        return right_houses
    if (len(right_houses) == 0):
        return left_houses
    max_abs_left = abs(max(left_houses))  # O(n)
    max_abs_right = abs(min(right_houses))  # O(n)

    if max_abs_left < max_abs_right:
        schedule = left_houses + right_houses
    else:
        schedule = right_houses + left_houses

    return schedule


def test(n: int):
    lst: List[float] = np.random.normal(0, n, n).tolist()
    # print(lst)
    print(parcours(lst))
