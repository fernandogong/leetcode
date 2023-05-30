# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = l1[::-1]
        l2 = l2[::-1]

        sum1 = int(''.join(map(str, l1)))
        sum2 = int(''.join(map(str, l2)))
        sum = sum1+sum2

        sum_list = [int(number) for number in str(sum)]

        return sum_list

l1 = [2,4,3]
l2 = [5,6,4]

solution = Solution()
print(solution.addTwoNumbers(l1, l2))