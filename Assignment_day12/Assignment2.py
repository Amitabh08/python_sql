def supress_exception( *args, exception, result, **kwargs):
    def decorator(func):
        def inner(*fn_arg, **fn_kwarg):
            print(fn_arg,fn_kwarg)
            try:
                res = func(*fn_arg, **fn_kwarg)
                return res
            except exception:
                return result
            except Exception as ex:
                raise ex
        return inner
    return decorator



 

@supress_exception(exception = KeyError, result = False)
def authenticate(user,password):
    print(f'Authenticating {user}')
    return users[user] == password

users = {'a':123, 'b':1234}
authenticate('a',123)
authenticate('b',122)
