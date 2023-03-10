# Time Complexity
- Asymptotic Notation(점근적 표기)
### Big O notation
- 복잡도의 **점근적 상한**을 나타냄
- 단순히 "실행시간이 $n^2$에 비례"하는 알고리즘이라고 말함.

### Big Omega notation
- 복잡도의 **점근적 하한**을 나타냄
- "최소한 이만한 시간은 걸린다"

### Theta notation
- Big O notation과 Big Omega notation가 같을 때 사용
- f(n)은 n이 증가함에 따라 $n^2$과 동일한 증가율을 가진다는 의미

### 자주 사용하는 O-표기
- $O(1)$: Constant time
- $O(logn)$: Logarithmic time
- $O(n)$: Linear time
- $O(nlogn)$: Log-linear time
- $O(n^2)$: Quadratic time
- $O(n^3)$: Cubic time
- $O(2^n)$: Exponential time

# Python3 표준입출력
- 입력
  - Raw 값의 입력: `input()`
    - 받은 입력값을 문자열로 취급
  - Evaluated된 값 입력: `eval(input())`
    - 받은 입력값을 평가된 데이터형으로 취급
- 출력
  - `print()`
  - `print('text', end='')`
  - `print('%d' % number)`
- 파일의 내용을 표준 입력으로 읽어오는 방법
  - `import sys`
  - `sys.stdin = open('input.txt', 'r')`

# 비트 연산
- 비트연산자
  - `&`: AND &rarr; 특정 비트를 0으로 만들 때 쓰임
  - `|`: OR &rarr; 특정 비트를 1로 만들 때 쓰임
  - `^`: XOR &rarr; 비교(같으면 0, 다르면 1), 특정 비트 반전
  - `~`: NOT
  - `<<`: L shift
  - `>>`: R shift

```python
a = 10
b = '0b1010'
print(f'{a:08b}')   # 10진수를 2진수로 8자리 표기
print(bin(a))       # 10진수를 2진수로 표기
print(int(b, 2))    # 2진수를 10진수로 표기
# 00001010
# 0b1010
# 10
```

## Enidanness(엔디안)
- 컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법을 의미하며 HW아키텍처마다 다름
1. Big-endian: 보통 큰 단위가 앞에 나옴. ex) 네트워크
2. Little-endian: 작은 단위가 앞에 나옴. ex) 대다수의 데스크탑 컴퓨터

# 진수
- MSB(Most Significant Bit): 최상위 비트
- LSB(Least Significant Bit): 최하위 비트
- 음의 정수 표현 방법
  - 1's complement: 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환
    - 6: `1000110`: 부호와 절대값
    - 6: `1111001`: 1의 보수 표현 &rarr; `-0`이 생기는 문제 발생
  - 2's complement: 1's complement + 1(최하위 비트)
    - 6: `1111010`

# 실수
- 실수를 표현하기 위해 부동 소수점(floating-point) 표기법 사용
- 소수점의 위치를 고정시켜 표현하는 방식: 왼쪽의 가장 유효한 숫자 다음으로 소수점의 위치를 고정시킨 후, 밑수의 지수승으로 표현
- 실수를 저장하기 위한 형식
  - 단정도 실수(32비트)
  - 배정도 실수(64비트)