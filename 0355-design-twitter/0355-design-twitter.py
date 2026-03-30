class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        total_users = self.followMap[userId]
        total_users.add(userId)

        for user in total_users:
            if user in self.tweetMap and self.tweetMap[user]:
                last_index = len(self.tweetMap[user]) - 1
                time_stamp, tweet_id = self.tweetMap[user][last_index]

                heapq.heappush(maxHeap, (time_stamp, tweet_id, user, last_index))

        while maxHeap and len(res) < 10:
            time_stamp, tweet_id, user, last_index = heapq.heappop(maxHeap)   
            res.append(tweet_id)

            if last_index > 0:
                next_index = last_index - 1
                next_time_stamp, next_tweet_id = self.tweetMap[user][next_index]
                heapq.heappush(maxHeap, (next_time_stamp, next_tweet_id, user, next_index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) 
    

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)