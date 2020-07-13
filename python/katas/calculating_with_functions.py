def num(fn, i): return fn(i) if fn else lambda x: num


def zero(fn=None): return num(fn, 0)
def one(fn=None): return num(fn, 1)
def two(fn=None): return num(fn, 2)
def three(fn=None): return num(fn, 3)
def four(fn=None): return num(fn, 4)
def five(fn=None): return num(fn, 5)
def six(fn=None): return num(fn, 6)
def seven(fn=None): return num(fn, 7)
def eight(fn=None): return num(fn, 8)
def nine(fn=None): return num(fn, 9)
def plus(fn): return lambda x: x + fn(x)
def minus(fn): return lambda x: x - fn(x)
def times(fn): return lambda x: x * fn(x)
def divided_by(fn): return lambda x: x // fn(x)
