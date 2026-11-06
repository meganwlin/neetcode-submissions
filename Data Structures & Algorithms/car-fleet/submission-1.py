class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position: [2, 5, 6] location
        # speed: [1, 5, 2] miles per hour

        # sort by position
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()

        times = []
        # iterate backwards since cars cannot pass each other
        for i in range(len(position)-1, -1, -1):
            p, s = pair[i][0], pair[i][1]
            time = (target - p) / s
            
            # there is not a fleet yet
            if not times:
                times.append(time)
            # did not catch up to make a fleet, start a new fleet:
            elif times[-1] < time:
                times.append(time)
            # don't add to times if there isn't a new fleet
        return len(times)



