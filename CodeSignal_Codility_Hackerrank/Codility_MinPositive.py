##return smallest positive integer greater than 0 that is not in passed list

def solution(n):
    A = set(n)
    ans = 1
    while ans in A:
       ans += 1
    return ans

n = [1,3,4,5,1,0]
print(solution(n))