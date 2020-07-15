""" Replace all spaces with '%20' in a string."""

def urlify(s):
    return s.rstrip().replace(" ", "%20")

assert urlify("Mr John Smith     ") == "Mr%20John%20Smith"

def urlify_nohelp(s):
    """ Implement as a fixed-length list, i.e. a character array, without using rstrip() or replace(). """
    l = list(s)
    for i in range(len(l)):
        if l[i] == " ":
            for j in range(len(l)-1, i, -1):
                l[j] = l[j-2]
            l[i] = '%'
            l[i+1] = '2'
            l[i+2] = '0'
    return "".join(l)

assert urlify_nohelp("Mr John Smith    ") == "Mr%20John%20Smith"
