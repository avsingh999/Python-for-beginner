import math

# 제곱근 함수
n = math.sqrt(int(input()))
print(n)

# x보다 크거나 같은 가장 작은 정수.
n = math.ceil(float(input()))
print(n)

# 절대값을 반환
n = math.fabs(int(input()))
print(n)

# x의 팩토리얼을 반환
n = math.factorial(int(input()))
print(n)

# x이하의 가장 큰 정수를 반환
n = math.floor(float(input()))
print(n)

# x를 y로 나눌 때의 나머지를 반환
x = int(input())
y = int(input()) 
n = math.fmod(x,y)
print(n)

# x의 가수와 지수를 쌍(m, e)으로 반환
m = math.exp(float(input()))
print(m)

# iterable의 정확한 부동 소수점 합값을 반환합니다
print(math.fsum(range(10)))

# x가 무한대이거나 NaN이 아닌 경우 True를 반환합니다 (숫자가 아님).
x = int(input())
print(math.isfinite(x))	

# x가 양의 무한대이거나 음의 무한대이면 True를 반환합니다
x = int(input())
print(math.isinf(x))

# x가 NaN이면 True를 반환합니다
x = int(input())
print(math.isnan(x))

# x * (2**i) 반환
x = int(input())
i = int(input())
print(math.ldexp(x, i))

# x의 분수와 정수부분을 반환
x = int(input())
print(math.modf(x))	

# 잘린 정수 값 x를 반환합니다
x = int(input())
print(math.trunc(x))

#  e**x 반환
x = int(input())
print(math.exp(x))

# e**x - 1 반환
x = int(input())
print(math.expm1(x))

# x의 로그화한 밑을 밑으로 반환합니다 (기본값은 e).
x = int(input())
base = 10
print(math.log(x, base))

# 1 + x의 자연로그를 반환합니다
x = int(input())
print(math.log1p(x))

# x의 밑이 2 인 로그 값을 반환합니다
x= int(input())
print(math.log2(x))

# x의 밑이 10 인 로그 값을 반환합니다
x =int(input())
print(math.log10(x))

# x를 거듭제곱 y로 올림
x = int(input())
y = int(input())
print(math.pow(x, y))

# x의 제곱근을 반환
x =int(input())
print(math.sqrt(x))

# x의 아크 코사인을 반환합니다
x =int(input())
print(math.acos(x))

# x의 아크 사인을 반환합니다
x = int(input())
print(math.asin(x))	

# x의 아크 탄젠트를 반환
x = float(input())
print(math.atan(x))

# x의 아크 탄젠트를 반환
x = float(input())
print(math.atan(x))

# atan (y / x)을 반환합니다
x = int(input())
y = int(input())
print(math.atan2(y, x))

# x의 코사인을 반환합니다
x = int(input())
print(math.cos(x))

# 유클리드 표준을 반환합니다. sqrt (x * x + y * y)
x = int(input())
y = int(input())
print(math.hypot(x, y))

# x의 사인을 반환합니다
x = int(input())
print(math.sin(x))

# x의 탄젠트를 반환
x = int(input())
print(math.tan(x))

# 각도 x를 라디안에서 각도로 변환합니다
x = int(input())
print(math.degrees(x))

# 각도 x를 도에서 라디안으로 변환
x = int(input())
print(math.radians(x))

# x의 역쌍곡 코사인을 구합니다
x = int(input())
print(math.acosh(x))

# x의 역쌍곡 사인을 반환합니다
x = int(input())
print(math.asinh(x))

# x의 쌍곡 코사인을 반환합니다
x = int(input())
print(math.cosh(x))

# x의 쌍곡 사인을 반환합니다
x = int(input())
print(math.sinh(x))

# x의 쌍곡 탄젠트를 반환합니다
x = int(input())
print(math.tanh(x))

# x에서 에러 함수를 반환
x = int(input())
print(math.erf(x))

# x에서 상보오차 함수를 반환합니다
x = int(input())
print(math.erfc(x))

# x에서 감마 함수를 반환합니다
x = int(input())
print(math.gamma(x))

# x에서 감마 함수의 절대 값의 자연 로그를 반환합니다
x = int(input())
print(math.lgamma(x))

# 수학 상수, 원주와 지름의 비율 (3.14159 ...)
print(math.pi)

# 수학 상수 e (2.71828 ...)
print(math.e)
