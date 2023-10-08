SELECT
	MIN(average)
FROM(
	SELECT
	continent_code,
		AVG(area_in_sq_km) AS average
	FROM
		countries
	GROUP BY
		continent_code
) AS average_area;	