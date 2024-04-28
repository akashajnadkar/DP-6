'''
Time Complexity - O(n^2) for both DP and 2 pointers
Space Complexity - O(1) for 2 pointer method, O(n) for DP 

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Brute Force O(n^2)
        self.start = 0
        self.end = 0
        # for i in range(len(s)):
        #     self.checkPallindrome(s, i, i)
        #     if i < len(s)-1 and s[i+1] == s[i]:
        #         self.checkPallindrome(s, i, i+1)
                
        # print(f"{self.start} {self.end}")
        #return s[self.start:self.end+1]


        #Using DP
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(1,len(s)):
            for j in range(i , -1, -1):
                if s[i] == s[j]:
                    #if characters at i and j match then check diagonally up 
                    if i-j < 2 or dp[i-1][j+1]:
                        dp[i][j] = True
                        if i - j > self.end - self.start:
                            self.start = j
                            self.end = i
        return s[self.start:self.end+1]
        

    def checkPallindrome(self, s, left, right):
        #check pallindrome by comparing character on left pointer and right pointer
        #continue if equal break from the loop if unequal
        while left>=0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        #Bring left and right to their previous value and find total length
        #if length is greater than that between current start and end, then modify start and end
        left+=1
        right-=1
        if right - left > self.end - self.start:
            self.start = left
            self.end = right
        return

        