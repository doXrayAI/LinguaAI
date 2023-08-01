from functools import reduce

def make_bot_pipeline(bot_function_list):
    return reduce(lambda f, g: lambda x: g(f(x)), bot_function_list)

