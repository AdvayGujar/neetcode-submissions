class Twitter:

    def __init__(self):
        self.tweets = deque()
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft([userId, tweetId])

        if userId not in self.followers:
            self.followers[userId] = {userId}

    def getNewsFeed(self, userId: int) -> List[int]:
        counter = 0
        result = []
        x = 0
        if userId in self.followers:
            following = self.followers[userId]
        else:
            return result

        if self.tweets:
            while counter < 10:
                if self.tweets[x][0] in following:
                    result.append(self.tweets[x][1])
                    counter += 1
                
                x += 1
                if x == len(self.tweets):
                    break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = {followerId, followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)