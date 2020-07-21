def rotate(c, rot):
    shift = 97 if c.islower() else 65
    return chr((ord(c) + rot - shift) % 26 + shift)

def partlen(s):
    total = len(s)
    max = 0
    msg_length, remainder = divmod(total, 4)
#     print(msg_length, remainder)
    for i in range(msg_length, 0, -1):
        parts, new_remainder = divmod(total, i)
#         print(parts, new_remainder)
        if parts == 4 and new_remainder > max:
            max = new_remainder
            msg_length = i
    return msg_length

def encode_str(strng, shift):
#     print(strng, shift)
    char1 = strng[0].lower()
    prefix = char1 + rotate(char1, shift)
    encoded = prefix + "".join([rotate(c, shift) if c.isalpha() else c for c in strng])
    part_length = partlen(encoded)
    return [encoded[i:i+part_length] for i in range(0, len(encoded), part_length)]

def decode(arr):
    shift = ord(arr[0][1]) - ord(arr[0][0])
    arr[0] = arr[0][2:] # remove prefix from encoded string before decoding
    return "".join([rotate(c, 0-shift) if c.isalpha() else c for c in "".join(arr)])

@test.describe('Tests')
def fixed_tests():
    def testing_code(strng, shift, exp):
        actual = encode_str(strng, shift)
        Test.assert_equals(actual, exp)

    def testing_decode(arr, exp):
        actual = decode(arr)
        Test.assert_equals(actual, exp)
        
    @test.it('Basic Tests testing encode')
    def tests1():
        u = "I should have known that you would have a perfect answer for me!!!"
        v = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]
        testing_code(u, 1, v)
        v = ['ikK ujqwnf jcx', 'g mpqyp vjcv a', 'qw yqwnf jcxg ', 'c rgthgev cpuy', 'gt hqt og!!!']
        testing_code(u, 28, v)
    
        u = "abcdefghjuty12"
        v = ['abbc', 'defg', 'hikv', 'uz12']
        testing_code(u, 1, v)
        v = ['aeef', 'ghij', 'klny', 'xc12']
        testing_code(u, 30, v)

    @test.it('Basic Tests testing decode')
    def tests2():
        u = "O CAPTAIN! my Captain! our fearful trip is done;"
        v = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g", "fbsgvm usj", "q jt epof;"]
        testing_decode(v, u)
        v = ['owW KIXBIQ', 'V! ug Kixb', 'iqv! wcz n', 'miznct bzq', 'x qa lwvm;']
        testing_decode(v, u)
    
        u = "Exult, O shores, and ring, O bells! But I, with mournful tread, Walk the deck my Captain lies, Fallen cold and dead. "
        v = ["efFyvmu, P tipsft, boe s", "joh, P cfmmt! Cvu J, xju", "i npvsogvm usfbe, Xbml u", "if efdl nz Dbqubjo mjft,", " Gbmmfo dpme boe efbe. "]
        testing_decode(v, u)

        

