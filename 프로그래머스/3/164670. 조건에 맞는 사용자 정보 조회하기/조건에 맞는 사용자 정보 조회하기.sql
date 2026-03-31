SELECT b.USER_ID, b.NICKNAME, CONCAT(b.CITY, ' ',b.STREET_ADDRESS1, ' ',b.STREET_ADDRESS2) AS '전체주소', 
CONCAT(
    SUBSTR(TLNO, 1, 3), '-',
    SUBSTR(TLNO, 4, 4), '-',
    SUBSTR(TLNO, 8, 4)
) AS '전화번호'
FROM USED_GOODS_USER b
WHERE b.USER_ID IN (SELECT WRITER_ID 
                     FROM USED_GOODS_BOARD
                     GROUP BY WRITER_ID
                     HAVING COUNT(*) >=3
                   )
ORDER BY b.USER_ID DESC;