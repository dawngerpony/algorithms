""" Playing with slicing of strings. """

s = "abcdefg"
s_reversed = "gfedcba"

print("len(s)", len(s))
assert len(s) == 7

print("s[0]", s[0])
assert s[0] == "a"

print("s[0:1]", s[0:1])
assert s[0:1] == "a"

print("s[0:]", s[0:])
assert s[0:] == s

print("s[0:len(s)]", s[0:len(s)])
assert s[0:len(s)] == s

print("s[0:len(s):2]", s[0:len(s):2])
assert s[0:len(s):2] == "aceg"

print("s[:]", s[:])
assert s[:] == s

print("s[::]", s[::])
assert s[::] == s

print("s[::-1]", s[::-1])
assert s[::-1] == s_reversed

print("s[-1:-len(s)-1:-1]", s[-1:-len(s)-1:-1])
assert s[-1:-len(s)-1:-1] == s_reversed

print("len(s[0:100])", len(s[0:100]))
assert len(s[0:100]) == len(s)

print(s[0:100])
assert s[0:100] == s
