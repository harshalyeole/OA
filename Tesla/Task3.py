from collections import deque
def solution(numbers):
    d_q = deque()
    n = str(numbers)
    for i in n:
        d_q.append(i)
    ans = ""
    while d_q:
        if len(d_q)>1:
            c = d_q.popleft()
            d = d_q.pop()
            ans+=c+d
        else:
            c = d_q.pop()
            ans+= c
    return ans


def solution80(A):
    A = str(A)
    alen = len(A)
    if alen <= 2:
        return int(A)
    return int((A[0] + A[-1] + str(solution(A[1:-1]))))
    pass

n = 123456
print(solution(n))
