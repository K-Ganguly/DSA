# LeetCode Link: https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize a low bound for the possible eating rate (minimum 1).
        low = 1
        # Initialize a high bound for the possible eating rate (maximum pile size).
        high = max(piles)

        # Perform a binary search to find the minimum eating rate.
        while low <= high:
            # Calculate the middle eating rate.
            rate_of_eating = low + (high - low) // 2
            # Initialize the variable to keep track of the total hours needed.
            num_hours = 0
            # Calculate the hours needed to eat all piles at the current rate.
            for pile in piles:
                num_hours += ceil(pile / rate_of_eating)

            # Check if the total hours exceed the available hours 'h'.
            if num_hours > h:
                # If the total hours are too many, adjust the lower bound upwards.
                low = rate_of_eating + 1
            else:
                # If the total hours are within the available time, adjust the upper bound downwards.
                high = rate_of_eating - 1

        # Return the low bound, which represents the minimum eating rate to finish within 'h' hours.
        return low
