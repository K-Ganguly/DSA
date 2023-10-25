# LeetCode Link: https://leetcode.com/problems/car-fleet/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of cars, each represented as a tuple of their initial position and time taken to reach the target.
        cars = [(pos, (target - pos) / v) for pos, v in zip(position, speed)]

        # Sort the cars in descending order of their initial positions.
        # This allows us to process the cars from right to left, simulating their movement on the road.
        cars.sort(key=lambda car: car[0], reverse=True)

        # Initialize variables to keep track of the number of car fleets and the current maximum time taken.
        num_fleets = 0
        curr_max_time = 0

        # Iterate through the sorted list of cars.
        for curr_car_pos, curr_car_time_taken in cars:
            # If the current car takes more time to reach the target than the previous maximum time,
            # it forms a new car fleet. Update the maximum time and increment the fleet count.
            if curr_car_time_taken > curr_max_time:
                curr_max_time = curr_car_time_taken
                num_fleets += 1

        # Return the total number of car fleets.
        return num_fleets
