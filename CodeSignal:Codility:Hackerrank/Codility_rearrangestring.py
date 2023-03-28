##Question was to re-arrange a given number such that 123456 > 162534 ,  130 > 103
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
            ans+=c + d
        else:
            c = d_q.pop()
            ans+=c
    return ans

n = 17
print(solution(n))
