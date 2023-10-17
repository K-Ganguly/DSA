class MinStack:
    def __init__(self):
        # Initialize the main stack to store values
        self.stack = list()
        # Initialize a variable to store the current minimum value
        self.min_value = None

    def push(self, val: int) -> None:
        # This is an initial marker for the first element.
        if not self.stack:
            self.stack.append(0)
            # Set the initial minimum as the first element.
            self.min_value = val
        else:
            # Calculate how the new value relates to the current minimum.
            diff_with_min = val - self.min_value
            # Store the difference instead of the value itself.
            self.stack.append(diff_with_min)
            # Update the minimum when the new value is smaller.
            if diff_with_min < 0:
                self.min_value = val

    def pop(self) -> None:
        # Retrieve and process the stored difference.
        diff_with_min = self.stack.pop()
        # Restore the previous minimum when necessary.
        if diff_with_min < 0:
            self.min_value -= diff_with_min

    def top(self) -> int:
        # Retrieve the stored difference at the top.
        diff_with_min = self.stack[-1]
        # Return the current minimum when applicable.
        if diff_with_min < 0:
            return self.min_value
        else:
            # Adjust and return the actual value using the stored difference.
            return self.min_value + diff_with_min

    def getMin(self) -> int:
        # Simply return the current minimum value.
        return self.min_value
