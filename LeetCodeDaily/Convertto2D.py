from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        my_map = {}

        for n in nums:
            my_map[n] = my_map.get(n, 0) + 1
        
        


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 1, 2, 3, 1]
    result = solution.findMatrix(nums)
    print(result)
