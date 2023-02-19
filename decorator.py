# Decorator pattern

# def advise(func):
#
#     def wrapper(*args, **kwargs):
#         print("Advertisement")
#
#         return func(*args, **kwargs)
#
#     return wrapper
#
# def test(val1, val2):
#     result = val1 / val2
#
#     return result


# Syntactic sugar with parameters

def advertisement(*param, **kwparam):
    def advise(func):

        def wrapper(*args, **kwargs):
            print(*param, **kwparam)

            return func(*args, **kwargs)

        return wrapper
    return advise

@advertisement("Push Notification")
def test(val1, val2):
    result = val1 / val2

    return result

# Decorator with repeats

# def decorator_func(attempt=0, *param, **kwparam): # decorator params
#     def decorated_func(func): # decorated function
#
#         def wrapper(*args, **kwargs): # params of decorated function
#             attempts = attempt #kwparam["attempt"]
#
#             while attempts != 0:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as error:
#                     print(f"Error: {error}, attempts left {attempts}")
#                     attempts -= 1
#
#         return wrapper
#     return decorated_func
#
# @decorator_func(attempt=10)
# def test(val1, val2):
#     result = val1 / val2
#
#     return result

# Decoration of classes

# def decorator(password):
#     def decorated_obj(my_class):
#
#         def wrapp(*args, **kwargs):
#             if password != "russiaisterroriststate":
#                 raise ValueError("Denied!")
#             return my_class(*args, **kwargs)
#
#         return wrapp
#     return decorated_obj

# @decorator(password="russiaisterroriststate")
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def test(self):
#         print(self.a, self.b)

if __name__ == "__main__":
    # Decorator pattern
    # var = advise(test)
    # print(type(var))
    # print(var(1, 2))

    # Syntactic sugar with parameters
    print(test(1, 2))

    # Decorator with attempts
    # print(test(1, 0))

    # Decoration of classes
    # obj = MyClass(1, 2)
    # print(obj.test())
