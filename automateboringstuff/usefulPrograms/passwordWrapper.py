"""An example of functools, using wrappers and decorators"""
# Program wrapps password function based on access_level so its secured.

import functools

user = {'username': 'jose', 'access_level': 'user'}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                print("Sorry no permission")
        return secure_func
    return decorator



@make_secure('admin')
def get_admin_password():
    return 'admin: 1234'

@make_secure('user')
def get_dashboard_password():
    return 'user: user_password'

print(get_admin_password())
print(get_dashboard_password())