# Write an algorithm to check if a string is sorted in alphabetical order and print O if it is. If it is not in alphabetical order, then print the index of the character where it is out of alphabetical order.

# Example : “abc” returns 0
# “asd” returns 2

def funcAlphabeticOrder(inputString):
    length = len(inputString)
    for char in range(1,length):
        if inputString[char] < inputString[char-1]:
            return char
    return 0

inputString = "asd"
print(funcAlphabeticOrder(inputString))