import math

#square root function
n = math.sqrt(int(input()))
print(n)

#smallest integer greater than or equal to x.
n = math.ceil(float(input()))
print(n)

#retruns absolute value
n = math.fabs(int(input()))
print(n)

#retruns factorial of x
n = math.factorial(int(input()))
print(n)

#returns the largest integer less than or equal to x
n = math.floor(float(input()))
print(n)

#returns the remainder when x is divided by y
x = int(input())
y = int(input()) 
n = math.fmod(x,y)
print(n)

#Returns the mantissa and exponent of x as the pair (m, e)
m = math.exp(float(input()))
print(m)

#Returns an accurate floating point sum of values in the iterable
print(math.fsum(range(10)))

# Returns True if x is neither an infinity nor a NaN (Not a Number)
x = int(input())
print(math.isfinite(x))	

# Returns True if x is a positive or negative infinity
x = int(input())
print(math.isinf(x))

# Returns True if x is a NaN
x = int(input())
print(math.isnan(x))

# Returns x * (2**i)
x = int(input())
i = int(input())
print(math.ldexp(x, i))

# Returns the fractional and integer parts of x
x = int(input())
print(math.modf(x))	

# Returns the truncated integer value of x
x = int(input())
print(math.trunc(x))

# Returns e**x
x = int(input())
print(math.exp(x))

# Returns e**x - 1
x = int(input())
print(math.expm1(x))

# Returns the logarithm of x to the base (defaults to e)
x = int(input())
base = 10
print(math.log(x, base))

# Returns the natural logarithm of 1+x
x = int(input())
print(math.log1p(x))

# Returns the base-2 logarithm of x
x= int(input())
print(math.log2(x))

# Returns the base-10 logarithm of x
x =int(input())
print(math.log10(x))

# Returns x raised to the power y
x = int(input())
y = int(input())
print(math.pow(x, y))

# Returns the square root of x
x =int(input())
print(math.sqrt(x))

# Returns the arc cosine of x
x =int(input())
print(math.acos(x))

# Returns the arc sine of x
x = int(input())
print(math.asin(x))	

# Returns the arc tangent of x
x = float(input())
print(math.atan(x))

# Returns the arc tangent of x
x = float(input())
print(math.atan(x))

# Returns atan(y / x)
x = int(input())
y = int(input())
print(math.atan2(y, x))

# Returns the cosine of x
x = int(input())
print(math.cos(x))

# Returns the Euclidean norm, sqrt(x*x + y*y)
x = int(input())
y = int(input())
print(math.hypot(x, y))

# Returns the sine of x
x = int(input())
print(math.sin(x))

# Returns the tangent of x
x = int(input())
print(math.tan(x))

# Converts angle x from radians to degrees
x = int(input())
print(math.degrees(x))

# Converts angle x from degrees to radians
x = int(input())
print(math.radians(x))

# Returns the inverse hyperbolic cosine of x
x = int(input())
print(math.acosh(x))

# Returns the inverse hyperbolic sine of x
x = int(input())
print(math.asinh(x))

# Returns the hyperbolic cosine of x
x = int(input())
print(math.cosh(x))

# Returns the hyperbolic cosine of x
x = int(input())
print(math.sinh(x))

# Returns the hyperbolic tangent of x
x = int(input())
print(math.tanh(x))

# Returns the error function at x
x = int(input())
print(math.erf(x))

# Returns the complementary error function at x
x = int(input())
print(math.erfc(x))

# Returns the Gamma function at x
x = int(input())
print(math.gamma(x))

# Returns the natural logarithm of the absolute value of the Gamma function at x
x = int(input())
print(math.lgamma(x))

# Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
print(math.pi)

# mathematical constant e (2.71828...)
print(math.e)
