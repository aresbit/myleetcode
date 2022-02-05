#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        arr = [0] * (n + 1)

        if n < 2:
            return n
        arr[0] = 0
        arr[1] = 1
        for i  in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n]
# @lc code=end

