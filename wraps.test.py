from functools import wraps

def without_wraps(func):
    def __wraper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wraper

@without_wraps
def func_1():
   '''this is test!!!'''
    return "hello"

# words =without_wraps(func_1).__doc__
# print(words)

print(func_1.__doc__)
print(func_1.__name__)

def without_wraps(func):
    @wraps(func)
    def __wraper(*args, **kwargs):
        '''this is wraps!!!'''
        return func(*args, **kwargs)
    return __wraper