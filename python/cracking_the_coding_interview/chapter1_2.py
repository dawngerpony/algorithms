def is_perm(s1, s2):
    # TODO error checking
    def perms(prefix, string, acc):
        if len(string) == 0:
            acc.append(prefix)
            return acc
        for i in range(len(string)):
            perms(prefix+string[i], string[0:i]+string[i+1:], acc)
        return acc
    s2_perms = perms("", s2, [])
    if s1 in s2_perms:
        return True
    return False

assert is_perm("abc", "cba") is True
assert is_perm("abc", "dba") is False


def is_perm_non_recursive(s1, s2):
    l = list(s1)
    for c in s2:
        print(l)
        for i in range(len(l)):
            if l[i] == c:
                del l[i]
                break
    print("Final l", l)
    return len(l) == 0

assert is_perm_non_recursive("abc", "cba") is True
assert is_perm_non_recursive("abc", "aba") is False
assert is_perm_non_recursive("abb", "aab") is False
