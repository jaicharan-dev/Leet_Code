class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        total_users = self.followers[userId].copy()
        total_users.add(userId)

        maxHeap = []
        for followeeId in total_users:
            if self.tweets[followeeId]:
                lastIdx = len(self.tweets[followeeId])-1
                time, tweetId = self.tweets[followeeId][lastIdx]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, lastIdx))

        res = []
        while len(res) < 10 and maxHeap:
            time, tweetId, followeeId, lastIdx = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            if lastIdx > 0:
                lastIdx -= 1
                time, tweetId = self.tweets[followeeId][lastIdx]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, lastIdx))
        
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