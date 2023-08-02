from functools import reduce

def make_bot_pipeline(bot_function_list):
    '''Turns the list of bot functions taking 2 positional arguments 
    and returning 2 arguments into a pipeline'''
    return reduce(lambda f, g: lambda x, y: g(*f(x, y)), bot_function_list)

