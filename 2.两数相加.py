#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# type 'a list = Nil | Cons  of 'a * 'a list
# class listNode:
#     def __init__(self, val=0, next=None):
#         self.val = x
#         self.next = None

# class list:
#     def __init__(self, head=None):
#         self.head = head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        out = result = ListNode(0)

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            result.next = ListNode(carry % 10)
            result = result.next
            carry //= 10

            
        return out.next

# @lc code=end

