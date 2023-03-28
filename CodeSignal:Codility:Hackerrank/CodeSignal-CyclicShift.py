##Question was given 2 arrays of same length, arr1 goes cyclic shift till it comes back to its original form. With each cyclic shift, find the absolute difference between elements of arr1 and arr2 for index i [i will start from 0 till len of array]and the total sum of all these difference. In the end we had to return the minimum value out of all these total sums
def solutions(arr1,arr2):
    shifted_arr = []
    n = len(arr1)
    i = 0
    while i<n:
        temp_diff = 0
        final_val = 0
        last_elemt = arr1[n-1]
        arr1.pop()
        arr1.insert(0,last_elemt)
        for j in range(len(arr1)):
            temp_diff = abs(arr1[j] - arr2[j])
            final_val+=temp_diff
        shifted_arr.append(final_val)
        i+=1
    return min(shifted_arr)
arr1 = [1,4,2,11]
arr2 = [10,1,8,4]
print(solutions(arr1,arr2))
