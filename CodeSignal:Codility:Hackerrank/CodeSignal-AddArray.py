##question is when given an array, return an array of same length where output[i] = input[i-1] + input[i] + input[i+1]
def solution(a):
    b = [0]*len(a)
    for i in range(len(a)):
        if i+1>=len(a) or i-1<0:
            if i+1>=len(a) and i-1<0:
                b[i] = a[i]
            elif i+1>=len(a):
                b[i] = a[i-1] + a[i]
            elif i-1<0:
                b[i] = a[i] + a[i+1]
        else:
            b[i] = a[i-1] + a[i] + a[i+1]
    return b

a = [4,0,1,-2,3]
print(solution(a))