def solution(S):
    count = {} #dictionary for count of frequency of alphabets in the given string S

    #for every character in the string S
    for ch in S:
        if(ch in count): #if already present in dictionary
            count[ch]+=1 #increase count by 1
        else:            #if already not present in dictionary
            count[ch] = 1 #add it in dictionary

    odd = 0  #count of all alphabets occuring odd times in the string

    for alphabet in count:
        if((count[alphabet]%2)!=0): #if the frequency of the alphabet is odd
            odd+=1   #increase count of odd by 1

    #return 0 if no string is occuring odd times..
    #All occuring even times..No need to delete any character
    if(odd == 0):
        return 0 
    #else only one alphabet can occur odd times..
    #So, return odd-1.
    else:
        return odd - 1