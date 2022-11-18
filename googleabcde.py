# Working Solutions
# https://www.desiqna.in/6957/google-oa-coding-questions-and-solutions-set-22-2022-usa

# We are given a string text of length N consisting of
# the letters 'a, 'b' or 'c'. We can insert any of those
# letters before or after any letter in the string
# The goal is to insert letters into text so that it will
# follow the pattern "abcabca...", i.e. it should start with
# a letter 'a, letter 'a' should be followed by 'b', letter "b'
# should be followed by 'c, and letter c' by a. The string
# may end with any of those three letters.
# What is the minimum number of letters we need to
# insert into text?
# Write a function:
# int solution(String text);
# that, given a string text of length N, returns the
# minimum number of insertions needed to
# make text follow the described pattern.
# Examples:
# 1. For text = "aabcc" we need to insert letters 'b'
# and 'c' between the pair of letters 'a', and then
# insert letters 'a' and 'b' between the two letters
# "c. This way we obtain the string "abcabcabc"
# and the function should return 4.
# 2. For text = "abcabcabca", we do not


# Python program to print the
# Minimal moves to form a string
# by appending string and adding characters

INT_MAX = 100000000

# function to return the
# minimal number of moves
def minimalSteps(s, n):
    dp = [INT_MAX for i in range(n)]

    # initialize both strings to null
    s1 = ""
    s2 = ""

    # base case
    dp[0] = 1
    s1 += s[0]

    for i in range(1, n):
        s1 += s[i]

        # check if it can be appended
        s2 = s[i + 1: i + 1 + i + 1]

        # addition of character
        # takes one step
        dp[i] = min(dp[i], dp[i - 1] + 1)

        # appending takes 1 step, and
        # we directly reach index i*2+1
        # after appending so the number
        # of steps is stord in i*2+1
        if (s1 == s2):
            dp[i * 2 + 1] = min(dp[i] + 1,
            dp[i * 2 + 1])

    return dp[n - 1]

# Driver Code
s = "abcabcabca"
n =len(s)

# function call to return
# minimal number of moves
print( minimalSteps(s, n) )