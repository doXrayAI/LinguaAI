from functools import reduce

def make_bot_pipeline(bot_function_list):
    return reduce(lambda f, g: lambda x, y: g(*f(x, y)), bot_function_list)

