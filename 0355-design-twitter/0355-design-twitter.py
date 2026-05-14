class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)        
        self.followers = defaultdict(set)        
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        users = self.followers[userId].copy()
        users.add(userId)

        for user in users:
            if self.tweets[user]:
                last_index = len(self.tweets[user]) - 1
                tweet_time, tweet_id = self.tweets[user][last_index]

                heapq.heappush(minHeap, (tweet_time, tweet_id, user, last_index))

        while minHeap and len(res) < 10:
            tweet_time, tweet_id, author, index = heapq.heappop(minHeap)
            res.append(tweet_id)

            if index > 0:
                next_index = index - 1
                next_time, next_tweet = self.tweets[author][next_index]
                heapq.heappush(minHeap, (next_time, next_tweet, author, next_index)) 
        
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)