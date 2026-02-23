# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start:.4f}s")
#         return result
#     return wrapper

# @timer
# def slow_function(sleep_time):
#     time.sleep(sleep_time)
#     return "understood"

# print(slow_function(2))

# def require_login(func):
#     def wrapper(user, *args, **kwargs):
#         if not user.get("logged_in"):
#             print("Access denied")
#             return
#         return func(user, *args, **kwargs)
#     return wrapper

# @require_login
# def view_dashboard(user):
#     print("Welcome to dashboard")

# view_dashboard({"logged_in":True})

# Task 1
from functools import wraps
def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("Function started")
            try:
                for _ in range(n):
                    r=func(*args,**kwargs)
            except Exception as e:
                raise ValueError(e)
            print("Function end")
            return r
        return wrapper
    return decorator

@retry(3)
def test(a=4,b=5,c=0):
    """
    Docstring for test
    
    :param a: Description
    :param b: Description
    """
    print("hello world")
    return a+b+c

print(test(a=5,b=6))
print(test.__name__)
print(test.__doc__) 

