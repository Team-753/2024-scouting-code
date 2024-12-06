Select RANK() OVER (ORDER BY ScenarioScore DESC) AS Rank, drv2.* FROM (
SELECT TeamID, (drv.A1*S.A1 + drv.A2*S.A2 + drv.A3*S.A3 + drv.A4*S.A4) / Matches as ScenarioScore FROM Scenarios AS S CROSS JOIN (
SELECT       TeamID, SUM(cast(A.A1 as int)) as A1, SUM(A.A2) as A2, SUM(A.A3) as A3, SUM(A.A4) as A4, count(*) as Matches
FROM            AttributeScore as A GROUP BY TeamID) drv
WHERE        (S.ID = 5)) drv2
ORDER BY ScenarioScore DESC
