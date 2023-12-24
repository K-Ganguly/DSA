# LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize an array to store the product of all elements except the current one.
        product_array = [1] * len(nums)

        # Calculate the product of all elements to the left of each element.
        left_product = 1
        for i, num in enumerate(nums):
            product_array[i] = left_product
            left_product *= nums[i]  # Update the product for the next element.

        # Calculate the product of all elements to the right of each element and combine it with the left product.
        right_product = 1
        right_index = len(nums) - 1
        while right_index > -1:
            product_array[
                right_index
            ] *= right_product  # Combine the left and right products.
            right_product *= nums[
                right_index
            ]  # Update the product for the next element to the right.
            right_index -= 1

        return product_array  # Return the array containing the product of all elements except the current one.
