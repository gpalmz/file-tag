from functools import reduce


def find(predicate, iterable, default=None):
    return next((e for e in iterable if predicate(e)), default)


def apply_pred(pred, iterable):
    return reduce(
        lambda acc, v: (True, v) if acc[0] and pred(acc[1], v) else (False, v),
        iterable,
        (True, next(iter(iterable)))
    )[0]
