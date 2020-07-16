numbers = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
numbers = {n: i for i, n in enumerate(numbers)}
numbers[""] = 0

tens = {"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}

formulas = {
    "-": lambda x, y: tens[x] + numbers[y],
    "hundred": lambda x, y: (parse_chunk(x, 1) * 100) + parse_chunk(y, 2),
    "thousand": lambda x, y: (parse_chunk(x, 1) * 1000) + parse_chunk(y, 1)
}
order = ["thousand", "hundred", "-"]

def parse_int(string):
    s2 = string.replace(" and", "")
    if s2 == "one million":
        return 1000000
    return parse_chunk(s2)

def parse_chunk(string, o=0):
    parts = string.strip().split(order[o])
    if len(parts) > 1:
        x, y = parts
        return formulas[order[o]](x, y if y != "" else "zero")
    x = parts[0]
    return numbers[x] if x in numbers else tens[x] if x in tens else parse_chunk(x, o+1)

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
assert parse_int("one million") == 1000000
print("Test 7 passed!")
assert parse_int("thirty") == 30
print("Test 8 passed!")
