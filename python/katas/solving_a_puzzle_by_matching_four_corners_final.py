def puzzle_solver(pieces, width, height):
    l_dict = {}
    t_dict = {}
    q = [ [None for i in range(width)] for j in range(height) ]
    for p in pieces:
        p = Piece(p)
        # top left corner
        if p.tl is None and p.tr is None and p.bl is None:
            q[0][0] = p
            continue
        lkey = (p.tl, p.bl)
        if lkey not in l_dict: l_dict[lkey] = []
        l_dict[lkey].append(p)
        tkey = (p.tl, p.tr)
        if tkey not in t_dict: t_dict[tkey] = []
        t_dict[tkey].append(p)
    # top row, working from left to right
    for x in range(1, width):
        q[0][x] = l_dict[(q[0][x-1].tr, q[0][x-1].br)].pop()
    # the rest of the rows, looking at the piece above
    for y in range(1, height):
        for x in range(0, width):
            q[y][x] = t_dict[(q[y-1][x].bl, q[y-1][x].br)].pop()

    # pull out the IDs and create the required list/tuple structure
    return [tuple([w.id for w in q[h]]) for h in range(height)]

class Piece:
    def __init__(self, data):
        up, down, self.id = data
        self.tl, self.tr = up
        self.bl, self.br = down


puzzle = [((None, 5), (None, None), 3), ((17, None), (None, None), 9), ((None, 4), (None, 5), 8)    ,
        ((4, 11), (5, 17), 5),        ((11, None), (17, None), 2),   ((None, None), (None, 4), 7) ,
        ((5, 17), (None, None), 1), ((None, None), (11, None), 4), ((None, None), (4, 11), 6)     ]
assert puzzle_solver(puzzle, 3, 3) == [(7, 6, 4), (8, 5, 2), (3, 1, 9)]
print("Test 1 passed!")

puzzle = [((None, None), (None, 8), 2), ((None, 8), (None, 21), 3), ((8, None), (21, None), 1), ((21, None), (None, None), 6), ((None, 21), (None, None), 5), ((None, None), (8, None), 4)]
assert puzzle_solver(puzzle, 2, 3) == [(2, 4), (3, 1), (5, 6)]
print("Test 2 passed!")

puzzle = [((1684, 7221), (None, None), 212), ((13126, 13764), (None, None), 5972), ((13154, 16351), (None, None), 17615), ((11849, 12474), (14042, 4363), 8794), ((154, 12636), (7134, 12145), 4137), ((19177, 2468), (10607, 2384), 4828), ((None, 16516), (None, 13126), 9808), ((None, None), (None, 6969), 9362), ((None, None), (6899, 11317), 7211), ((13764, 7134), (None, None), 876), ((16351, 2371), (None, None), 7445), ((12987, 1440), (13154, 16351), 9719), ((14888, 13955), (154, 12636), 386), ((None, None), (14734, 19794), 130), ((2384, 11849), (9531, 14042), 12989), ((10984, 848), (7221, 14431), 18605), ((4363, 1684), (None, None), 2345), ((1440, 16661), (16351, 2371), 17420), ((14431, 13154), (None, None), 11620), ((None, None), (6969, 7640), 12657), ((19794, 6899), (848, 12987), 4710), ((11317, 608), (1440, 16661), 4498), ((6637, 9531), (None, None), 1732), ((None, None), (19177, 2468), 18908), ((16661, None), (2371, None), 11506), ((14734, 19794), (10984, 848), 13399), ((None, None), (6189, 11132), 12159), ((16516, 12203), (13126, 13764), 1453), ((6189, 11132), (11849, 12474), 5936), ((12636, 10607), (12145, 6637), 8877), ((10607, 2384), (6637, 9531), 12185), ((None, None), (11132, 6873), 11807), ((14042, 4363), (None, None), 6693), ((7221, 14431), (None, None), 18288), ((None, None), (2468, 6189), 2423), ((None, None), (7640, 14888), 16357), ((848, 12987), (14431, 13154), 4635), ((608, None), (16661, None), 12571), ((None, None), (608, None), 51), ((12145, 6637), (None, None), 17390), ((12203, 154), (13764, 7134), 7920), ((None, None), (6873, 14734), 11854), ((13955, 19177), (12636, 10607), 12116), ((6899, 11317), (12987, 1440), 12530), ((None, 13126), (None, None), 12965), ((None, None), (19794, 6899), 7296), ((7134, 12145), (None, None), 4602), ((None, None), (14888, 13955), 13659), ((None, None), (13955, 19177), 3499), ((12474, 9108), (4363, 1684), 17167), ((None, None), (11317, 608), 9880), ((9108, 10984), (1684, 7221), 2890), ((2468, 6189), (2384, 11849), 4457), ((9531, 14042), (None, None), 18992), ((6969, 7640), (16516, 12203), 4296), ((11132, 6873), (12474, 9108), 13195), ((7640, 14888), (12203, 154), 12272), ((None, 6969), (None, 16516), 5546), ((2371, None), (None, None), 11955), ((6873, 14734), (9108, 10984), 15250)]
assert puzzle_solver(puzzle, 15, 4) == [(9362, 12657, 16357, 13659, 3499, 18908, 2423, 12159, 11807, 11854, 130, 7296, 7211, 9880, 51), (5546, 4296, 12272, 386, 12116, 4828, 4457, 5936, 13195, 15250, 13399, 4710, 12530, 4498, 12571), (9808, 1453, 7920, 4137, 8877, 12185, 12989, 8794, 17167, 2890, 18605, 4635, 9719, 17420, 11506), (12965, 5972, 876, 4602, 17390, 1732, 18992, 6693, 2345, 212, 18288, 11620, 17615, 7445, 11955)]
print("Test 3 passed!")
