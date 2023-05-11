#traverse a list from front(i) and back (j) at the same time such that i<=j to 
# find the number of pair of indices whose sum is a power of 2
##try to remove double for loop, time complexity too high > https://leetcode.com/discuss/interview-question/872882/quora-coding-challenge-number-of-pairs-whose-sum-is-a-power-of-2
import math
def solution(numbers):
    pair = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)-1,-1,-1):
            if i<=j:
                # print(f"number from i = {numbers[i]}")
                # print(f"number from j = {numbers[j]}")
                temp = numbers[i] + numbers[j]
                print(temp)
                if temp>0:
                    if math.log2(temp).is_integer():
                        print(f"adding this {temp}")
                        pair+=1
    return pair


numbers =[1,-1,2,3]
print(solution(numbers))

#probable solution with O(31*n) time complexity
# def solution(numbers):
#     count = 0
    
#     for i in range(31):
#         key = 2 ** i
        
#         my_map = {}
#         for num in numbers:
#             my_map[num] = my_map.get(num, 0) + 1
#             to_find = key - num
#             if to_find in my_map:
#                 count += 1
                

#     return count