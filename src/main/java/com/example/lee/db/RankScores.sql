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

