from inspect import getmembers
import math


def eval_math_fn(function, name_dict):
    math_name_dict = dict(getmembers(math))
    
    # Uncomment to use custom function
    # x = name_dict['x']
    # return (x ** 2) - x
    
    return eval(function, {**name_dict, **math_name_dict})
