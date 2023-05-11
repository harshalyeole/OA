##Question was to find the number of cyclic pairs in an array. Example of cyclic pair for number 13 would be [13,31]. Cyclic pair for number 546, would be [546,465,654], if the number of digits match, 5604 is a cyclic pair of 4560 but not of 456.

def cyclicshift(num):
    shift_list = []
    num = list(str(num))
    val = ""
    for i in range(len(num)):
        num.append(num.pop(0))
        val = ''.join(num)
        shift_list.append(int(val))
    return shift_list


def solution(arr1):
    cyclic = 0
    for i in range(len(arr1)):
        shift_list = cyclicshift(arr1[i])
        for j in range(i+1,len(arr1)) :
            if arr1[j] in shift_list and checkLen(arr1[i],arr1[j]):
                cyclic+=1
    return cyclic

def checkLen(num1,num2):
    if len(str(num1)) == len(str(num2)):
        return True
    return False

arr1 =[13,5604,31,2,13,4560,546,654,456]
print(solution(arr1))