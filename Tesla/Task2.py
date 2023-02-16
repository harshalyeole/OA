def solution(S):
    acounts = S.count('A')
    bcounts = S.count('B')
    ncounts = S.count('N')

    aMove = acounts // 3
    bMove = bcounts // 1
    nMove = ncounts // 2

    print("aMove,bMove,nMove", aMove,bMove,nMove)
    return min(aMove,bMove,nMove)
    pass

print(solution('NAABXXAN'))