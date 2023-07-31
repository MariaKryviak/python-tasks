from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = 1
        while counter < len(nums):
            for index in range(len(nums)):
                if target == nums[counter] + nums[index] and counter != index:
                    return [index, counter]
            counter = counter + 1


if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 2, 3], 6))
    print(Solution().twoSum([-3, 4, 3, 90], 0))
    print(Solution().twoSum([2, 5, 5, 11], 10))
