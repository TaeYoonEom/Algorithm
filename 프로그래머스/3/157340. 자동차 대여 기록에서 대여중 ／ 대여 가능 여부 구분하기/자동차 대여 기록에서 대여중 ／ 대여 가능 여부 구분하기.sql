SELECT CAR_ID,
       CASE 
           WHEN EXISTS (
               SELECT 1
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY B
               WHERE B.CAR_ID = A.CAR_ID
               AND B.START_DATE <= '2022-10-16'
               AND B.END_DATE >= '2022-10-16'
           )
           THEN '대여중'
           ELSE '대여 가능'
       END AS AVAILABILITY
FROM (SELECT DISTINCT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) A
ORDER BY CAR_ID DESC;