class Solution:
    """
    You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

    ​Return the minimum number of intervals required to complete all tasks.

    Example 1:

    Input: tasks = ["A","A","A","B","B","B"], n = 2

    Output: 8

    Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

    After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

    Example 2:

    Input: tasks = ["A","C","A","B","D","B"], n = 1

    Output: 6

    Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

    With a cooling interval of 1, you can repeat a task after just one other task.

    Example 3:

    Input: tasks = ["A","A","A", "B","B","B"], n = 3

    Output: 10

    Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

    There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build frequency map
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)
        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            task_cnt = 0
            # Execute tasks in each cycle
            while cycle > 0 and pq:
                cur_freq = -heapq.heappop(pq)
                if cur_freq > 1:
                    store.append(-(cur_freq - 1))
                task_cnt += 1
                cycle -= 1
            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            # Add time for the completed cycle
            time += task_cnt if not pq else n + 1
        return time
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a frequency array to keep track of the count of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        # Sort the frequency array in non-decreasing order
        freq.sort()
        # Calculate the maximum frequency of any task
        max_freq = freq[25] - 1
        # Calculate the number of idle slots that will be required
        idle_slots = max_freq * n
        # Iterate over the frequency array from the second highest frequency to the lowest frequency
        for i in range(24, -1, -1):
            # Subtract the minimum of the maximum frequency and the current frequency from the idle slots
            idle_slots -= min(max_freq, freq[i])
        # If there are any idle slots left, add them to the total number of tasks
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)