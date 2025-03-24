class Solution:
    """
    You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

    Return the count of days when the employee is available for work but no meetings are scheduled.

    Note: The meetings may overlap.

    Example 1:

    Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

    Output: 2

    Explanation:

    There is no meeting scheduled on the 4th and 8th days.

    Example 2:

    Input: days = 5, meetings = [[2,4],[1,3]]

    Output: 1

    Explanation:

    There is no meeting scheduled on the 5th day.

    Example 3:

    Input: days = 6, meetings = [[1,6]]

    Output: 0

    Explanation:

    Meetings are scheduled for all working days.
    """
    def countDays1(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        # Sort meetings by start time
        meetings.sort()
        
        # Merge overlapping meetings
        merged = []
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        # Count free days
        free_days = 0
        
        # Days before the first meeting
        if merged[0][0] > 1:
            free_days += merged[0][0] - 1

        # Days between merged meetings
        for i in range(1, len(merged)):
            free_days += merged[i][0] - merged[i - 1][1] - 1

        # Days after the last meeting
        if merged[-1][1] < days:
            free_days += days - merged[-1][1]

        return free_days
    
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        meetings.sort()
        merged = []
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        n = len(merged)
        free_days = 0
        if merged[0][0] > 1:
            free_days += merged[0][0] - 1
        for i in range(1, n):
            free_days += merged[i][0] - merged[i - 1][1] - 1
        
        if merged[-1][1] < days:
            free_days += days - merged[-1][1]

        return free_days