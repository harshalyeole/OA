##Question was to rearrange an array in an optimal way such that when you add the element with a particular index(i) with the element at previous index(i-1), we end up with the most number of maximum values. Since we could not determine a way to find an algorithm for optimal sorting, we used itertools to find all the permutations possible of a given array.


import itertools

def findperm(arr):
    return list(itertools.permutations(arr)) ##returns a list of tuple with all possible permutations of a givren array

def optimalsort(arr1):
    tmp_list = findperm(arr1)
    result_list = []
    for i in tmp_list:
        arr_tmp = i
        sum_list = positiveprefix(arr_tmp)
        result = findpositve(sum_list)
        result_list.append(result)
    return max(result_list)

def positiveprefix(arr1): #for a given array we parse elements to find positive prefix
    sum_list = []
    prefixsum= 0
    for i in range(0,len(arr1)):
        if i==0:
            prefixsum = arr1[i]
        else:
            prefixsum = sum_list[i-1] + arr1[i] ##add elements for index i with elements from sum_list at prev index
        sum_list.append(prefixsum)
    return sum_list

def findpositve(arr1): #find number of positive elements
    i = 0
    for j in range(len(arr1)):
        if arr1[j]>0:
            i+=1
    return i

arr1 =[-3,0,2,1]
print(optimalsort(arr1))