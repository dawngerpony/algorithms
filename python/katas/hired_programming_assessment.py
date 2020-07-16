# def solution(n):
#     if n == 0 or n == 1 or n == 2:
#         return n
#     if n == 3:
#         return 4
#     return solution(max(n-3,0)) + solution(max(n-2,0)) + solution(max(n-1,0))


def solution(n):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 0
    for i in range(n+1):
        cache[i] += sum(cache[i - x] for x in [1, 2, 3] if i - x > 0)
        cache[i] += 1 if i in [1, 2, 3] else 0
    return cache[i]


assert solution(4) == 7
assert solution(5) == 13
assert solution(3) == 4
assert solution(34) == 615693474
assert solution(32) == 181997601
assert solution(44) == 272809183135
