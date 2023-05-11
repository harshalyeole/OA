# There is a set of N jars containing chocolates. Some of them may be empty. Determine the maximum number of chocolates Andrew can pick from the jars given that he cannot pick from jars next to each other.
# Write an algorithm to find the maximum number of chocolates that can be picked from the jars in such a way that the chocolates are not picked from jars next to each other.

# Input
# The first line of input consists of an integer- num/ars, representing the number of jars (N).
# The next line consists of N space-separated integers representing the number of chocolates in each jar.

# Output
# Print the maximum number of chocolates that can be picked from the jars in such a way that the chocolates are not picked from jars next to each other.

#Example
# Input:
# 6
# 5 30 99 60 5 10

# Output : 114

# Explanation:
# Andrew picks from the 1st (5), 3rd
# (99) and 6th (10) jars.
# So, the output is 114.

def maxSum(inputArr):
    if not inputArr:
        return 0
    maxChocolatepicked = [None for _ in range(len(inputArr)+1)]
    N = len(inputArr)
    maxChocolatepicked[N],maxChocolatepicked[N-1] = 0, inputArr[N-1]
    for i in range(N-2,-1,-1):
        maxChocolatepicked[i] = max(maxChocolatepicked[i+1], maxChocolatepicked[i+2] + inputArr[i])
    return maxChocolatepicked[0]

def main():
    inputArr = []
    #input array size is not required that's why we are omitting it
    inputArr = list(map(int, input("Put the array values accordingly seperated by a spaceabar-->  ").split()))

    result = maxSum(inputArr)
    print(result)

if __name__ == "__main__":
    main()