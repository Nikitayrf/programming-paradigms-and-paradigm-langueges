# Python composition function
def compose(f, g):
    return lambda x: f(g(x))

# Haskell composition function
# compose f g x = f (g x)
