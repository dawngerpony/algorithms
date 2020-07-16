numbers = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
numbers = {n: i for i, n in enumerate(numbers)}

tens = {"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}

# multipliers = {
#     "thousand": 1000,
#     "hundred": 100,
#     "-": 1
# }

def parse_int(string):
    s2 = string.replace(" and", "")
    total = 0
    if s2 == "one million":
        return 1000000
    parts = s2.split("thousand")
    if len(parts) > 1:
        total += parse_chunk(parts[0], "hundred") * 1000
        total += parse_chunk(parts[1], "hundred")
    else:
        total += parse_chunk(parts[0], "hundred")
    return total

def parse_chunk(string, sep="-"):
    parts = string.strip().split(sep)
    if len(parts) > 1:
        if parts[1] == "":
            parts[1] = "zero"
        if sep == "-":
            return tens[parts[0]] + numbers[parts[1]]
        if sep == "hundred":
            return (parse_chunk(parts[0]) * 100) + parse_chunk(parts[1])
    if parts[0] == "":
        return 0
    if parts[0] in numbers:
        return numbers[parts[0]]
    return parse_chunk(parts[0])

assert parse_int('one') == 1
print("Test 1 passed!")
assert parse_int('twenty') == 20
print("Test 2 passed!")
assert parse_int('two hundred forty-six') == 246
print("Test 3 passed!")
assert parse_int("seven hundred eighty-three thousand nine hundred and nineteen") == 783919
print("Test 4 passed!")
assert parse_int("twenty-one") == 21
print("Test 5 passed!")
assert parse_int("one hundred") == 100
print("Test 6 passed!")
