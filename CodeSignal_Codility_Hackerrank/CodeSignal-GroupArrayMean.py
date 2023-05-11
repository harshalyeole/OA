#Given an array of arrays task is to group these array in the ascending order of their mean value

from collections import defaultdict

def solution(a):
    hash_map = defaultdict(list)
    for i in range(len(a)):
        mean = 0
        mean = sum(a[i])/len(a[i])
        hash_map[mean].append(i)
    output = []
    for i in hash_map.values():
        output.append(i)
    return output

a = [[3,3,4,2],[4,4],[4,0,3,3],[2,3],[3,3,3]]
print(solution(a))