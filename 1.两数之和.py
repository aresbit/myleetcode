#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i, num in enumerate(nums): # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
        # 同时列出数据和数据下标，一般用在 for 循环当中。i和num,默认前面一个是索引，后面一个是对象里的内容
            dict[num] = i # 键值对，num是键，i是值，赋予给num键。
            
        for i, num in enumerate(nums):
            if target - num in dict and i != dict[target - num]: # 是判断键（key）在不在dict里面
                return [i, dict [target - num]]
# @lc code=end

