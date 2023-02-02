# 레스토랑의 종업원이라고 가정하자. 손님이 스테이크를 주문하였을 때, 메뉴 가격 외에 VAT가 반영되었음을 설명해야 한다. 
# 단, 이때 string interpolation과 서식명세를 사용하라.
# 스테이크의 가격은 50,000원/ VAT는 15%이다.
# 원래의 스테이크 가격과 VAT, VAT가 포함된 실제 결제 금액을 계산하여, 아래와 같이 출력하라.

# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500


steak = 50000
VAT = int(steak * 0.15)
price = steak + VAT

print(
'스테이크   ' + f'{steak:,}\n' + 
'+ VAT     ' + f'{VAT:,}\n' 
+ '총계 ₩    ' + f'{price:,}'
)
