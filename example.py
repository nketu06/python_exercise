def decorator(func):
    def wrapper():
        print("first love")
        func()
        print('last love')
    return wrapper


@decorator
def printHello():
    print("hello kajal")




# decorator(printHello)()
printHello()
 