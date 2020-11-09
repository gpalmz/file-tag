from functools import reduce


def p_true(_):
    return True


def p_not(p):
    return lambda v: not p(v)


def p_and(p0, p1):
    return lambda v: p0(v) and p1(v)


def p_all(preds):
    return reduce(lambda acc, p: p_and(acc, p), preds, p_true)


def p_any(preds):
    return p_not(p_all(map(p_not, preds)))
