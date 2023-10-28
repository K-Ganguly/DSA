# LeetCode Link: https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store key-value pairs along with timestamps.
        self.time_map_obj = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map_obj.get(key):
            # If the key exists in the dictionary:
            # Append the new value and timestamp to the existing list of values.
            self.time_map_obj[key].append((value, timestamp))
        else:
            # If the key does not exist in the dictionary:
            # Create a new list with the current value and timestamp and store it under the key.
            self.time_map_obj[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        vals = self.time_map_obj.get(key)
        if not vals:
            # If the key does not exist in the dictionary, return an empty string.
            return ""
        result = ""
        low = 0
        high = len(vals) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if vals[mid][1] <= timestamp:
                # Binary search is used to find the value with the closest timestamp
                # that is less than or equal to the requested timestamp.
                result = vals[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return result
