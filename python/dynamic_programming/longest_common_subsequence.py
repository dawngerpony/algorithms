""" https://www.techiedelight.com/longest-common-subsequence/
"""

CALLS = 0

def lcs_recursive(s1, s2):
    global CALLS
    CALLS += 1
    # print((s1, s2))
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1[-1] == s2[-1]:
        # print("same")
        return lcs_recursive(s1[0:len(s1)-1], s2[0:len(s2)-1]) + 1
    else:
        # print("different")
        return max(lcs_recursive(s1[0:len(s1)], s2[0:len(s2)-1]), lcs_recursive(s1[0:len(s1)-1], s2[0:len(s2)]))


def lcs_dynamic(s1, s2, cache):
    global CALLS
    CALLS += 1
    # print((s1, s2))
    key = (s1, s2)
    if len(s1) == 0 or len(s2) == 0:
        # print("zero")
        return 0
    if key not in cache:
        if s1[-1] == s2[-1]:
            # print("same")
            result = lcs_dynamic(s1[0:len(s1)-1], s2[0:len(s2)-1], cache)
            # print("result", result)
            cache[key] = result + 1
        else:
            # print("different")
            cache[key] = max(lcs_dynamic(s1[0:len(s1)], s2[0:len(s2)-1], cache), lcs_dynamic(s1[0:len(s1)-1], s2[0:len(s2)], cache))
    return cache[key]


# assert lcs("ABCD", "BCD") == 3
CALLS = 0
lcslen = lcs_recursive("ABCBDAB", "BDCABA")
print(lcslen, CALLS)
assert lcslen == 4

CALLS = 0
cache = {}
lcslen = lcs_dynamic("ABCBDAB", "BDCABA", cache)
print(lcslen, CALLS)
assert lcslen == 4
