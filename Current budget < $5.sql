/*
-Current Budget $5.01- $500
-Yday Margin > 15%
-Margin 2 Days Ago > 15%
-Yday GP > 95% of GP 2 Days Ago
-Yday GP > 95% of GP 3 Days Ago
*/
Expected Results
WITH
  margin1 AS (
    SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 1 DAY)
  ),
  margin2 AS (
    SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 2 DAY)
  ),
  gp1 AS (
    SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 1 DAY)
  ),
  gp2 AS (
    SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 2 DAY)
  ),
  gp3 AS (
    SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 3 DAY)
  )
SELECT t1.adset_id, t1.daily_budget, t1.status, margin2.margin
FROM AdSets t1
JOIN margin1 ON t1.adset_id = margin1.adset_id
JOIN margin2 ON t1.adset_id = margin2.adset_id
JOIN gp1 ON t1.adset_id = gp1.adset_id
JOIN gp2 ON t1.adset_id = gp2.adset_id
JOIN gp3 ON t1.adset_id = gp3.adset_id
WHERE
  (TO_DAYS(NOW()) - TO_DAYS(t1.start_time)) < 100
   AND t1.daily_budget >= 5.01
   AND margin1.margin >= 15
   AND margin2.margin > 15
   AND gp1.profit > (95/100)*gp2.profit
   AND gp1.profit > (95/100)*gp3.profit;

Get Results

WITH
	margin1 AS (
	SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 1 DAY)
	),
	margin2 AS (
	SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 2 DAY)
	),
	gross_profit1 AS (
	SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 1 DAY)
	),
    gross_profit2 AS (
	SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 2 DAY)(Missed)
	),
    gross_profit3 AS (
	SELECT * FROM v_spendreport WHERE reportDate = DATE_SUB(CURDATE(), INTERVAL 3 DAY)(Missed)
	)
SELECT t1.adset_id, t1.daily_budget, t1.status, margin2.margin(Missed)
FROM AdSets t1
	JOIN margin1 ON t1.adset_id = margin1.adset_id
	JOIN margin2 ON t1.adset_id = margin2.adset_id
	JOIN gross_profit1 ON t1.adset_id = gross_profit1.adset_id
    JOIN gross_profit2 ON t1.adset_id = gross_profit2.adset_id(Missed)
    JOIN gross_profit3 ON t1.adset_id = gross_profit3.adset_id(Missed)
WHERE
t1.daily_budget >= 5.01
AND margin1.margin >= 15
AND margin2.margin >= 15
AND gross_profit1.profit > (95/100)*gross_profit2.profit(Missed)
AND gross_profit2.profit > (95/100)*gross_profit3.profit(Missed);


step --1 

if param === "gross_profit":
    if types === "percentOfTimeFrame":
        value = (percentOfTimeFrame/100) * value
    whereList.push(this.generateWhere(s1,s2,value))
else:

