class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list) # userId: [timestamp, tweetId]
        self.followMap = defaultdict(set) # userId: [set of users following]
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        # Define all eligible users to include in feed
        following = self.followMap[userId]
        following.add(userId)

        # Get the most recent tweet from each user
        recentTweets = [] # heap
        
        for user in following:
            userTweets = self.tweetMap[user]
            if len(userTweets) > 0: # skip if the user never tweeted
                index = len(userTweets) - 1
                recentTweetTime = userTweets[index][0]
                recentTweetId = userTweets[index][1]
                heapq.heappush(recentTweets, [recentTweetTime, recentTweetId, user, index])
        
        while len(feed) < 10 and recentTweets:
            [time, tweetId, user, index] = heapq.heappop(recentTweets)
            
            # add tweet to feed
            feed.append(tweetId)

            # replace with next tweet from user
            if index > 0: # got all tweets from user
                userTweets = self.tweetMap[user]
                index -=1
                recentTweetTime = userTweets[index][0]
                recentTweetId = userTweets[index][1]
                heapq.heappush(recentTweets, [recentTweetTime, recentTweetId, user, index])
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
