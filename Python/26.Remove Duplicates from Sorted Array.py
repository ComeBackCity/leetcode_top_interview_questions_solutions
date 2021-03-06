# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    # Time complexity = O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tracking = nums[0]
        index = 1
        for i in nums:
            if i > tracking:
                nums[index] = i
                tracking = i
                index += 1

        return index


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([]))
