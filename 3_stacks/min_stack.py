class MinStack:
    def __init__(self):
        self.stack = list()  # Initialize the main stack to store values
        self.min_value = (
            None  # Initialize a variable to store the current minimum value
        )

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)  # This is an initial marker for the first element.
            self.min_value = val  # Set the initial minimum as the first element.
        else:
            diff_with_min = (
                val - self.min_value
            )  # Calculate how the new value relates to the current minimum.
            self.stack.append(
                diff_with_min
            )  # Store the difference instead of the value itself.
            if diff_with_min < 0:
                self.min_value = (
                    val  # Update the minimum when the new value is smaller.
                )

    def pop(self) -> None:
        diff_with_min = self.stack.pop()  # Retrieve and process the stored difference.
        if diff_with_min < 0:
            self.min_value -= (
                diff_with_min  # Restore the previous minimum when necessary.
            )

    def top(self) -> int:
        diff_with_min = self.stack[-1]  # Retrieve the stored difference at the top.
        if diff_with_min < 0:
            return self.min_value  # Return the current minimum when applicable.
        else:
            return (
                self.min_value + diff_with_min
            )  # Adjust and return the actual value using the stored difference.

    def getMin(self) -> int:
        return self.min_value  # Simply return the current minimum value.
