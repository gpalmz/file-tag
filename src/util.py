from functools import reduce
from itertools import product


def apply_pred(pred, iterable):
    iterable = iter(iterable)
    return reduce(
        lambda acc, v: (True, v) if acc[0] and pred(acc[1], v) else (False, v),
        iterable,
        (True, next(iterable, None))
    )[0]


def have_matching_combination(pred, iterables):
    return any(map(lambda iterable: apply_pred(pred, iterable), product(*iterables)))
