# Snowflake OA

# LeetCode: 1639. Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution:
    def numWays(self, words, target):
        m, n, k, N = len(words), len(words[0]), len(target), 10**9 + 7
        Q  = [[0] * 26 for _ in range(n)]
        dp = [[0] * k for _ in range(n)]
        sp = [[0] * k for _ in range(n)]
        for i in range(n):
            for j in range(m):
                Q[i][ord(words[j][i]) - ord("a")] += 1

        dp[0][0] = sp[0][0] = Q[0][ord(target[0]) - ord("a")]
        
        for i in range(1, n):
            for j in range(k):
                if j > 0: dp[i][j] = Q[i][ord(target[j]) - ord("a")] * sp[i-1][j-1]
                else: dp[i][j] = Q[i][ord(target[j]) - ord("a")]
                sp[i][j] = (sp[i-1][j] + dp[i][j]) % N

        return sp[-1][-1] % N