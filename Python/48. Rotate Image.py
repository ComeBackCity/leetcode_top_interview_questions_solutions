# Problem Link: https://leetcode.com/problems/rotate-image/
from typing import List


class Solution:
    # time = O(n^2) memory = O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t, b = l, r
                tl = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = tl

            l += 1
            r -= 1