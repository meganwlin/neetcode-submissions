class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        minHeap = []

        # temporarily follow yourself so your tweets are included in feed
        self.followMap[userId].add(userId)

        # iterate through each user you follow
        for followeeId in self.followMap[userId]:
            # check that the user tweeted so there is no key error
            if followeeId in self.tweetMap:
                followedUsersTweets = self.tweetMap[followeeId]
                lastTweetTime, lastTweetId = followedUsersTweets[-1]
                numTweets = len(followedUsersTweets)
                heapq.heappush(minHeap, [lastTweetTime, lastTweetId, followeeId, numTweets])
        
        # build the list of last ten tweets
        while minHeap and len(feed) < 10:
            # minHeap maintains the sort based on min time
            time, tweetId, followeeId, numTweets = heapq.heappop(minHeap)
            feed.append(tweetId)

            if numTweets > 1:
                # get the followee tweet map again and use the next tweet
                numTweets -= 1
                time, tweetId = self.tweetMap[followeeId][numTweets - 1] # convert num to index
                heapq.heappush(minHeap, [time, tweetId, followeeId, numTweets])
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
