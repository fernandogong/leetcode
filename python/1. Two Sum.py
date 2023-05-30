class Solution(object):
    def twoSum(self, nums, target):

        num_dict = {}
        output = []

        for index, number in enumerate(nums):
            result = target-number
            if result in num_dict:
                output.append(num_dict[result])
                output.append(index)
            num_dict[number] = index
        return output

nums = [2,5,7,4,11]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))
