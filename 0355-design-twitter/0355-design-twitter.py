class Twitter:

    def __init__(self):

        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        max_heap = []

        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user])-1
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(max_heap, (time, tweetId, idx, user))
        
        feed_count = 0
        res = []

        while feed_count < 10 and max_heap:
            time, tweet, idx, user = heapq.heappop(max_heap)
            res.append(tweet)
            feed_count += 1
            idx -= 1
            if idx >= 0:
                next_time, next_tweet = self.tweets[user][idx]
                heapq.heappush(max_heap, (next_time, next_tweet, idx, user))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)