#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count =1
        max = 0
        if s == '':
            return 0
        elif len(s) == 1:
            return 1
        else:
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if s[j] not in s[i:j]:
                        count += 1
                    else:
                        break
                if count > max:
                    max = count
                count = 1
            return max
# @lc code=end

