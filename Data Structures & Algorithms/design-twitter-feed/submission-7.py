import heapq
import time
class Twitter:

    def __init__(self):
        self.time = 0
        self.user_posts = defaultdict(list)
        self.user_follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_posts[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []
        heap.extend(self.user_posts[userId])
        follow_users = self.user_follows[userId]
        for follow_user in follow_users:
            heap.extend(self.user_posts[follow_user])
        heapq.heapify(heap)
        
        while heap:
            result.append(heapq.heappop(heap)[1])
            if len(result) == 10:
                break
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
