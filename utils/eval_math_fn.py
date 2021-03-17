from inspect import getmembers
import math


def eval_math_fn(function, name_dict):
    math_name_dict = dict(getmembers(math))
    return eval(function, {**name_dict, **math_name_dict})
