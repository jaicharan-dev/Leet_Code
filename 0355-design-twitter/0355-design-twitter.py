class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followers[userId]
        users.add(userId)
        max_heap = []

        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user])-1
                time, tweet = self.tweets[user][idx]
                heapq.heappush(max_heap, (time, tweet, idx, user))
        
        res = []

        while len(res) < 10 and max_heap:
            time, tweet, idx, user = heapq.heappop(max_heap)
            res.append(tweet)
            idx -= 1
            if idx >= 0:
                next_time, next_tweet = self.tweets[user][idx]
                heapq.heappush(max_heap, (next_time, next_tweet, idx, user))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:    
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)