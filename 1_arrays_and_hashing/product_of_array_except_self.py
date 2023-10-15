# Leetcode Link: https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1] * len(nums)

        left_product = 1
        for i, num in enumerate(nums):
            product_array[i] = left_product
            left_product *= nums[i]

        right_product = 1
        right_index = len(nums) - 1
        while right_index > -1:
            product_array[right_index] *= right_product
            right_product *= nums[right_index]
            right_index -= 1

        return product_array
