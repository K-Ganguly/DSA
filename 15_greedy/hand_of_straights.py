# LeetCode Link: https://leetcode.com/problems/hand-of-straights/
import heapq
from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible evenly by the group size
        if len(hand) % groupSize != 0:
            return False

        # Use a defaultdict to store the frequency of each card
        num_freq = defaultdict(int)

        # Count the frequency of each card in the hand
        for num in hand:
            num_freq[num] += 1

        # Initialize a min heap with the unique cards in the hand
        min_heap = list(num_freq.keys())
        heapq.heapify(min_heap)

        # Process each group of cards
        while min_heap:
            # Get the minimum card in the current group
            min_of_group = min_heap[0]

            # Iterate through the cards in the current group
            for num in range(min_of_group, min_of_group + groupSize):
                # Check if the current card is present in the frequency dictionary
                if num_freq[num] == 0:
                    return False

                # Decrease the frequency of the current card
                num_freq[num] -= 1

                # If the frequency becomes zero, remove the card from the min heap
                if num_freq[num] == 0:
                    # Ensure the removed card is the expected minimum of the group
                    if num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        # If all groups are processed without issues, the hand is valid
        return True
