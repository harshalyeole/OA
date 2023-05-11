##Given an array, find the number of subarrays of a given length that amount to a given target, the 2 numbers must be haing different indices in the subarray. ##figure out how to deal with numbers having same value but on different indices
## 'a' is the input array, 'm' is the size of the sub-arrays, 'k' is the target number
from collections import defaultdict
def solution(a,m,k):
    output = []
    for i in range(len(a)):
        sub_list = a[i:i+m]
        if len(sub_list)==m:
            output.append(sub_list)
    counter = 0
    for i in output:
        diff = 0
        # ll = enumerate(i)
        # print(i)
        # print(list(ll))
        for j in range(m):
            diff = k - i[j]
            if diff in i:
                hash_map = defaultdict(list)
                ll = enumerate(i)
                ll = list(ll)
                
                counter+=1
                break
    return counter
a = [2,4,7,5,3,5,8,5,1,7]
print(solution(a,4,10))
