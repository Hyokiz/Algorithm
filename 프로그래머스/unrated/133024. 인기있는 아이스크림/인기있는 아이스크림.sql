-- 코드를 입력하세요
# 총 주문량 기준 내림차순
# 같다면 출하 번호 기준 오름차순
SELECT FLAVOR 
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID
