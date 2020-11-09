import operator

from sexpdata import loads, Symbol

from util import find, apply_pred
from predicate import p_not as create_not, p_all as create_and, p_any as create_or

KEY_NOT_FOUND = object()


def create_atom(val):
    return lambda tags: val


def create_key(key_val):
    def eval_key(tags):
        tag = find(lambda tag: tag.key == key_val(tags), tags)
        return KEY_NOT_FOUND if tag is None else tag.value

    return eval_key


def create_has(keys):
    return lambda tags: all(key(tags) is not KEY_NOT_FOUND for key in keys)


def create_eq(args):
    return lambda tags: apply_pred(operator.eq, (arg(tags) for arg in args))


def create_lt(args):
    return lambda tags: apply_pred(operator.lt, (arg(tags) for arg in args))


def create_gt(args):
    return lambda tags: apply_pred(operator.gt, (arg(tags) for arg in args))


def is_sexpr_func(sexpr, name):
    return sexpr[0] == Symbol(name)


def parse_sexpr_func_args(sexpr):
    return tuple(parse_sexpr(p) for p in sexpr[1:])


def parse_sexpr(sexpr):
    if isinstance(sexpr, int) or isinstance(sexpr, str):
        return create_atom(sexpr)
    elif isinstance(sexpr, Symbol):
        return create_key(parse_sexpr(sexpr._val))
    elif is_sexpr_func(sexpr, 'and'):
        return create_and(parse_sexpr_func_args(sexpr))
    elif is_sexpr_func(sexpr, 'or'):
        return create_or(parse_sexpr_func_args(sexpr))
    elif is_sexpr_func(sexpr, 'not'):
        return create_not(parse_sexpr_func_args(sexpr)[0])
    elif is_sexpr_func(sexpr, 'has'):
        return create_has(parse_sexpr_func_args(sexpr))
    elif is_sexpr_func(sexpr, '='):
        return create_eq(parse_sexpr_func_args(sexpr))
    elif is_sexpr_func(sexpr, '<'):
        return create_lt(parse_sexpr_func_args(sexpr))
    elif is_sexpr_func(sexpr, '>'):
        return create_gt(parse_sexpr_func_args(sexpr))


def str_to_sexpr(s):
    return loads(s)


def parse_str(s):
    return parse_sexpr(str_to_sexpr(s))


def eval_str(s, tags):
    return parse_str(s)(tags)
