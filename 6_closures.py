import time
# Closures are an essential feature of Python
# However, their use is often subtle
# Common applications:
# - Use in callback functions
# - Delayed evaluation
# - Decorator functions

def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print('Hello Guido')

after(3, greeting)

# But what about...

# after(3, greeting("Jeff"))

# Or how about...

# def add(x, y):
#     print(f'Adding {x} + {y} -> {x + y}')
