# Pure function

def pow_pure(x, y):
    return x ** y


# Not a pure function

def pow_not_pure(x, y):
    print(x, y)  # побочный эффект
    return x ** y