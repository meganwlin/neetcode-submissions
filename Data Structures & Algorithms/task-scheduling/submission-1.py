class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        remainingTasks = []
        taskCount = defaultdict(int)
        for task in tasks:
            taskCount[task] += 1

        for task in taskCount:
            # make this a maxheap
            heapq.heappush(remainingTasks, [-taskCount[task], task, -n - 1]) # instances of task, task id, last time task used
        
        time = 0
        # hold tasks that need more cooldown to be added back to queue
        ineligibleTasks = []

        while remainingTasks or ineligibleTasks:
            print(time)
            print(remainingTasks, ineligibleTasks)
            while len(remainingTasks) > 0:
                # find the next eligible task
                remainingTaskCount, taskName, lastTimeUsed = heapq.heappop(remainingTasks)
                if (time - lastTimeUsed) > n:
                    remainingTaskCount += 1
                    # only add back to remaining task queue if there are more of this task type
                    if remainingTaskCount < 0:
                        heapq.heappush(remainingTasks, [remainingTaskCount, taskName, time])
                    break # exit the while, and add ineligible tasks back for eligibility
                else: # needs more cooldown time, so we add to incomplete queue
                    ineligibleTasks.append([remainingTaskCount, taskName, lastTimeUsed])
            # exhausted finding an eligible task, so the CPU goes idle for one cycle 
            # or a task was found, and we need to add ineligible tasks back to queue anyways
            time += 1

            temp = []
            for task in ineligibleTasks:
                # only add back if with increment, it would be eligible next cycle
                lastTimeUsed = task[2]
                if (time - lastTimeUsed) > n:
                    heapq.heappush(remainingTasks, task)
                else:
                    temp.append(task)
            ineligibleTasks = temp
        return time
            






