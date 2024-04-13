from datetime import datetime

class Solution:
    """
    Write a program to count the number of days between two dates.

    The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

    Example 1:

    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1
    Example 2:

    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15
    """
    def daysBetweenDates1(self, date1: str, date2: str) -> int:
        time1 = [int(num) for num in date1.split("-")]
        time2 = [int(num) for num in date2.split("-")]
        t1 = datetime(*time1).timestamp()
        t2 = datetime(*time2).timestamp()
        return int(abs(t1 - t2) / 86400)
    
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        t1 = datetime.strptime(date1, "%Y-%m-%d").date()
        t2 = datetime.strptime(date2, "%Y-%m-%d").date()
        return abs((t2 - t1).days)