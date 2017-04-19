'''
Purpose : find all the substring of the text into a list
Algorithm : KMP algorithm
Example : findAllSubstring("hello and hello and hi there", "hello") -> [0, 10]
'''

def findAllSubstring(text,pattern):
    ans = []
    dp = [0]*len(pattern)
    for i in xrange(1,len(pattern)):
        dp[i] = dp[i-1]
        while dp[i] > 0 and pattern[dp[i]] != pattern[i]:
            dp[i] = dp[dp[i]-1]
        if pattern[dp[i]] == pattern[i]:
            dp[i] += 1
    match = 0
    for i in xrange(len(text)):
        while match > 0 and pattern[match] != text[i]:
            match = dp[match-1]
        if pattern[match] == text[i]:
            match += 1
        if match == len(pattern):
            match = dp[match-1]
            ans.append(i-len(pattern)+1)
    return ans
