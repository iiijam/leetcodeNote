'''
旋转数组
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
'''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) <= k:
            nums.reverse()
        else:
        #reverse the list and then reverse the first k elements and then reverse the rest
            nums.reverse()
            nums[:k] = nums[:k][::-1]
            nums[k:] = nums[k:][::-1]

print(Solution().rotate([1,2,3,4,5,6,7], 3))