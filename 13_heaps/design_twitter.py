# LeetCode Link: https://leetcode.com/problems/design-twitter/
from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        # Initialize the Twitter object with a global timestamp, user tweets, and user followings
        self.time = 0
        self.tweets = defaultdict(list)  # Dictionary to store user tweets
        self.users = defaultdict(set)  # Dictionary to store user followings

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Post a tweet by appending it to the user's tweet list along with the timestamp
        self.tweets[userId].append((self.time, tweetId))
        # Decrement the global timestamp to maintain chronological order
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Initialize a heap to store tweets and a set to track users being followed
        heap = list()
        following = self.users[userId]
        following.add(
            userId
        )  # Include the user in the list of following to see their own tweets
        tweets_list = list()

        # Iterate through each user the current user is following
        for user in following:
            # Iterate through each tweet of the user and add it to the heap
            for tweet in self.tweets[user]:
                heap.append(tweet)

        # Convert the list of tweets into a min-heap based on timestamps
        heapq.heapify(heap)

        # Retrieve up to 10 tweets from the heap or until the heap is empty
        i = 0
        while heap and i < 10:
            i += 1
            # Pop the tweet from the heap and append its tweetId to the result list
            tweet_id = heapq.heappop(heap)[1]
            tweets_list.append(tweet_id)

        return tweets_list

    def follow(self, followerId: int, followeeId: int) -> None:
        # Allow a user to follow another user by adding the followeeId to the follower's set of followings
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Unfollow a user by removing the followeeId from the follower's set of followings
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
