""" Practice assessment from hired.com for programming skills. """


def solution(arr):
    """ The solution. """
    if len(arr) == 0:
        return ""
    left_sum = right_sum = 0
    arr = [i if i != -1 else 0 for i in arr]
    del arr[0]
    jump = 1
    while len(arr) > 0:
        left_sum += sum(arr[0:jump])
        right_sum += sum(arr[jump:jump+jump])
        del arr[0:jump+jump]
        jump *= 2
    if left_sum > right_sum:
        return "Left"
    if right_sum > left_sum:
        return "Right"
    if left_sum == right_sum:
        return ""


assert solution([]) == ""
assert solution([1, 2, 3]) == "Right"
assert solution([1, 4, 100, 5]) == "Right"
assert solution([1, 10, 5, 1, 0, 6]) == ""
assert solution([3, 6, 2, 9, -1, 10]) == "Left"
