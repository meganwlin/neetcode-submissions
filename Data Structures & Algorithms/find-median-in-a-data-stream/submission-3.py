class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]: # prevent index error, then check if it belongs in right half
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num) # maxheap for left side to access elements closest to middle first
        
        # rebalance left and right so that they are even
        while abs(len(self.left) - len(self.right)) > 1:
            # too heavy on left
            if len(self.left) > len(self.right):
                move = -heapq.heappop(self.left)
                heapq.heappush(self.right, move)
            else:
                move = heapq.heappop(self.right)
                heapq.heappush(self.left, -move)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            print(f"{self.left} and {self.right} are balanced")
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            print(f"Leftside looks like: {self.left}")
            return -self.left[0]
        else:
            print(f"Right side looks like: {self.left}")
            return self.right[0]