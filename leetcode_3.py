class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        curlen = 0
        window = []
        for i in range(0,len(s)):
            if s[i] not in window:
                window.append(s[i])
                curlen+=1
            else:
                if(curlen>maxlen):
                    maxlen = curlen
                while window[0]!=s[i]:
                    wpop = window.pop(0)
                    print("popped element: ", wpop)
                window.pop(0)
                window.append(s[i])
                curlen = len(window)
        if(len(window)>maxlen):
                    maxlen = len(window)
        return maxlen
        
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/