# LeetCode Link: https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if the total gas is less than the total cost, indicating no possible circuit
        if sum(gas) < sum(cost):
            return -1

        # Initialize the start index and a variable to track the total gas available
        start_index = 0
        total = 0

        # Iterate through the gas and cost arrays
        for i in range(len(gas)):
            # Update the total gas available at the current station
            total += gas[i] - cost[i]

            # If the total becomes negative, reset it to 0 and update the start index
            if total < 0:
                total = 0
                start_index = i + 1

        # Return the start index where a circuit can be completed
        return start_index
