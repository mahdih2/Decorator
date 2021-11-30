import src.Decorator

name = "mahdi"

@src.Decorator.my_decorator
def say(name):
    print(f"hello {name}")

say(name)