class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
            
            else:
                dp[i] += dp[i+1]
                if i + 1 < len(s) and 1 <= int(s[i] + s[i+1]) <= 26:
                    dp[i] += dp[i+2]

        return dp[0]

# Time: O(n)
# Space: O(n)
