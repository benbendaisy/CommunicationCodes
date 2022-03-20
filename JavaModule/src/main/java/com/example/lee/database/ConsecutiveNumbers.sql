Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.


SELECT DISTINCT Num as ConsecutiveNums FROM (
    SELECT Num, @count := IF(@prevNum = Num, @count + 1, 1) AS cnt, @prevNum := Num
    FROM Logs, (SELECT @count := 0) c, (SELECT @prevNum := null) p
    ORDER BY Id asc
) n WHERE cnt > 2;

#change the way to initialize variables
SELECT DISTINCT Num as ConsecutiveNums FROM (
    SELECT Num, @count := IF(@prevNum = Num, @count + 1, 1) AS cnt, @prevNum := Num
    FROM Logs, (SELECT @count := 0, @prevNum := null) p
    ORDER BY Id asc
) n WHERE cnt > 2;