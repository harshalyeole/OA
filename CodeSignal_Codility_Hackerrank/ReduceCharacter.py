##given a string reduce it by replacing each character with the average of the characters that come before and after it. Consider all characters to be lowercase, where a = 1, b = 2...z = 26. input string "abcdefg" > turns "bcdef" after first round, continue doing this till we are only left with 1 character.
##explanatation, input string "abcdefg" gives answer "d"
##we can't take average of neighbouring characters of first and last, so we start with second character. 
##so 'b' is replaced by ('a' + 'c') //2 > (1+3)//2 = 2, so 'b' in this case is replaced by 'b'. After first iteration string becomes 'bcdef', after second iteration string becomes 'cde' and finally string is left with only 1 character which is 'd'

def reducestring(s):
    while len(s)!=1:
        t = ""
        for i in range(1,len(s)-1):
            prev = ord(s[i-1]) ##find previous value in ascii
            post = ord(s[i+1]) ##find after character value in ascii
            value= (prev + post)//2
            t+=chr(value) ##append the replacement character to an empty string
        s = t ## now s becomes the replacement string
    return s

s = 'abcdefg'
print(reducestring(s))