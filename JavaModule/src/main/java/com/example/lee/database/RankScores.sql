Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

SELECT Score, (SELECT COUNT(DISTINCT(Score))+1 FROM Scores s2 WHERE s2.Score > s1.Score) As Rank
FROM Scores s1
ORDER BY Score DESC;

SELECT Score, Rank FROM(
  SELECT    Score,
            @curRank := @curRank + IF(@prevScore = Score, 0, 1) AS Rank,
            @prevScore := Score
  FROM      Scores, (SELECT @curRank := 0) r, (SELECT @prevScore := NULL) p
  ORDER BY  Score DESC
) t;

SELECT Scores.Score, count(scoring.Score) as Rank FROM Scores,
(SELECT DISTINCT Score from Scores) scoring
WHERE Scores.Score <= scoring.Score
GROUP BY Scores.Id, Scores.Score order by Score desc;

SELECT e.Score, t.Rank FROM Scores e
INNER JOIN (
	SELECT @rank := @rank + 1 AS Rank, Score
	FROM (
	    /*SELECT distinct Score FROM (select @rank := 0) r, Scores ORDER BY Score DESC*/
		SELECT Score FROM (select @rank := 0) r, Scores GROUP BY Score ORDER BY Score DESC
	) t
) t
ON e.Score = t.Score
ORDER BY e.Score DESC;

