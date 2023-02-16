def solution(N, K):
    index = 0
    while K > 0 and index < 3:
        numS = str(N)
        a = int(numS[index])
        if a == 9:
            index += 1
        else:
            res = numS[:index] + str(a+1) + numS[index+1:]
            if int(res) > N:
                N = int(res)
                K -= 1
    return N
    pass


print(solution(512, 10))
