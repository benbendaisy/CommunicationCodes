class Solution:
    """
    You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

    You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

    Return the maximum number of events you can attend.

    Example 1:

    Input: events = [[1,2],[2,3],[3,4]]
    Output: 3
    Explanation: You can attend all the three events.
    One way to attend them all is as shown.
    Attend the first event on day 1.
    Attend the second event on day 2.
    Attend the third event on day 3.
    Example 2:

    Input: events= [[1,2],[2,3],[3,4],[1,2]]
    Output: 4
    """
    def maxEvents1(self, events: List[List[int]]) -> int:
        events.sort()  # Sort by start day
        min_heap = []  # Min-heap for end days
        day = 0
        event_index = 0
        total_events = len(events)
        attended = 0

        while event_index < total_events or min_heap:
            if not min_heap:
                # Jump to the next available event's start day
                day = events[event_index][0]

            # Add all events starting on or before the current day
            while event_index < total_events and events[event_index][0] <= day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1

            # Remove expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
                day += 1

        return attended
    
    def maxEvents2(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        
        events.sort()
        min_heap, day, event_idx, total_events, attended = [], 0, 0, len(events), 0
        while event_idx < total_events or min_heap:
            if not min_heap:
                day = events[event_idx][0]
            
            while event_idx < total_events and events[event_idx][0] <= day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
                day += 1
        return attended