def summ(a: int):
    def wrapper(b: int = None):
        nonlocal a
        if b is None:
            return a
        a += b
        return wrapper

    return wrapper


print(summ(5)(2)(-2)())
