class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a stack to store indices of temperatures.
        stack = []
        # Initialize a result list with zeros.
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # For each temperature in the list:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If the stack is not empty and the current temperature is greater than the temperature
                # at the index at the top of the stack, it means we've found a warmer day.
                j = stack.pop()  # Pop the index from the stack.
                result[j] = (
                    i - j
                )  # Calculate the number of days to wait and update the result.

            # Push the current index onto the stack to check for it in future iterations.
            stack.append(i)

        # Return the list with the number of days to wait for warmer temperatures.
        return result
