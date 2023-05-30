class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum1, sum2 = 0, 0

        for digit in l1:
            sum1 = sum1 * 10 + digit
        for digit in l2:
            sum2 = sum2 * 10 + digit

        sum = sum1+sum2

        sum_list = [int(number) for number in str(sum)]
        reverted_list = []
        for i in range(len(sum_list) -1, -1, -1):
            reverted_list.append(sum_list[i])
        return reverted_list

l1 = [2,4,3]
l2 = [5,6,4]

solution = Solution()
print(solution.addTwoNumbers(l1, l2))