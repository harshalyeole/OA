import math


def solution(arr):
    # idea is that you can keep shift value from right to left, but not left to right,
    # this means you should minimize your left most node, s.t. the maximum of the array is minimized
    # a.k.a your left most node should always be the maximum

    available_sink = 0
    current_max = arr[0]
    for i in range(1, len(arr)):
        a = arr[i]
        if a < current_max:
            available_sink += current_max - a
        else:
            diff = a - current_max
            if diff <= available_sink:
                available_sink -= diff
            else:
                # we yield, we need to distributed the remain across all members
                remain = diff - available_sink
                count = i+1
                current_max += math.ceil(remain / count)
                available_sink = 0 if remain % count == 0 else count - remain % count
    return current_max


print(solution([10, 3, 5, 7]))