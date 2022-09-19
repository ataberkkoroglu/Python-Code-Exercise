from math import *
import math
from winreg import EnableReflectionKey
print ("""DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.

    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    asinh(x, /)
        Return the inverse hyperbolic sine of x.

    atan(x, /)
        Return the arc tangent (measured in radians) of x.

        The result is between -pi/2 and pi/2.

    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered.

    atanh(x, /)
        Return the inverse hyperbolic tangent of x.

    ceil(x, /)
        Return the ceiling of x as an Integral.

        This is the smallest integer >= x.

    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.

        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.

        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.

        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.

    cos(x, /)
        Return the cosine of x (measured in radians).

    cosh(x, /)
        Return the hyperbolic cosine of x.

    degrees(x, /)
        Convert angle x from radians to degrees.

    dist(p, q, /)
        Return the Euclidean distance between two points p and q.

        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.

        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    erf(x, /)
        Error function at x.

    erfc(x, /)
        Complementary error function at x.

    exp(x, /)
        Return e raised to the power of x.

    expm1(x, /)
        Return exp(x)-1.

        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.

    fabs(x, /)
        Return the absolute value of the float x.

    factorial(x, /)
        Find x!.

        Raise a ValueError if x is negative or non-integral.

    floor(x, /)
        Return the floor of x as an Integral.

        This is the largest integer <= x.

    fmod(x, y, /)
        Return fmod(x, y), according to platform C.

        x % y may differ.

    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).

        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.

    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.

        Assumes IEEE-754 floating point arithmetic.

    gamma(x, /)
        Gamma function at x.

    gcd(*integers)
        Greatest Common Divisor.

    hypot(...)
        hypot(*coordinates) -> value

        Multidimensional Euclidean distance from the origin to a point.

        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))

        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).

        For example, the hypotenuse of a 3/4/5 right triangle is:

            >>> hypot(3.0, 4.0)
            5.0

    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.

          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.

    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.

    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.

    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.

    isqrt(n, /)
        Return the integer part of the square root of the input.

    lcm(*integers)
        Least Common Multiple.

    ldexp(x, i, /)
        Return x * (2**i).

        This is essentially the inverse of frexp().

    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.

    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.

        If the base not specified, returns the natural logarithm (base e) of x.

    log10(x, /)
        Return the base 10 logarithm of x.

    log1p(x, /)
        Return the natural logarithm of 1+x (base e).

        The result is computed in a way which is accurate for x near zero.

    log2(x, /)
        Return the base 2 logarithm of x.

    modf(x, /)
        Return the fractional and integer parts of x.

        Both results carry the sign of x and are floats.

    nextafter(x, y, /)
        Return the next floating-point value after x towards y.

    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.

        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.

        If k is not specified or is None, then k defaults to n
        and the function returns n!.

        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.

    pow(x, y, /)
        Return x**y (x to the power of y).

    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.

        The default start value for the product is 1.

        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.

    radians(x, /)
        Convert angle x from degrees to radians.

    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.

        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.

    sin(x, /)
        Return the sine of x (measured in radians).

    sinh(x, /)
        Return the hyperbolic sine of x.

    sqrt(x, /)
        Return the square root of x.

    tan(x, /)
        Return the tangent of x (measured in radians).

    tanh(x, /)
        Return the hyperbolic tangent of x.

    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.

        Uses the __trunc__ magic method.

    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586)
""")
toplam=5
while toplam>0:
    x=float(input("Bir Sayı Giriniz= "))
    y=input("Sayı Girmeye Devam Etmek İstiyorsanız'q' İstemiyorsanız 'a'ya Basınız...")
    if y=="a":
        break
    elif y=="q":
        print("Sayı Girmeye Devam Edebilirsiniz...")
        toplam -=1
        z=float(input("İkinci Sayı Giriniz= "))
        y=input("Sayı Girmeye Devam Etmek İstiyorsanız'q' İstemiyorsanız 'a'ya Basınız...")
        if y=="a":
         break
        elif y=="q":
           print("Sayı Girmeye Devam Edebilirsiniz...")
           toplam -=1
           b=int(input(" Sayıyı Giriniz= "))
           y=input("Sayı Girmeye Devam Etmek İstiyorsanız'q' İstemiyorsanız 'a'ya Basınız...")
           if y=="a":
             break
           elif y=="q":
              print("Sayı Girmeye Devam Edebilirsiniz...")
              toplam -=1
              c=int(input(" Sayıyı Giriniz= "))
              y=input("Sayı Girmeye Devam Etmek İstiyorsanız'q' İstemiyorsanız 'a'ya Basınız...")
              if y=="a":
               break
              elif y=="q":
                print("Sayı Girmeye Devam Edebilirsiniz...")
                toplam -=1
                d=int(input(" Sayıyı Giriniz= "))
                y=input("Sayı Girmeye Devam Etmek İstiyorsanız'q' İstemiyorsanız 'a'ya Basınız...")
                break
    elif toplam==0:
        print("Artık Sayı Giremezsiniz...")
        break
    else:
        print("Yanlış Tuşa Bastınız. Lütfen Tekrar Deneyiniz...")
Işlem_Hakkı=10
while Işlem_Hakkı>0:
    print(" 'f', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp' ")
    a=input("Yapmak İstediginiz İşlemi Yazınız= ")
    if a=="acosh":
        math.acosh(x)
        print(x)
    elif a=="asin":
        math.asin(x)
        print(x)
    elif a=="atan":
        math.atan(x)
        print(x)
    elif a=="atan2":
        math.atan2(x,z)
        print(x)
    elif a=="acos":
        math.acos(x)
        print(x)
    elif a=="atanh":
        math.atanh(x)
        print(x)
    elif a=="ceil":
        math.ceil(x)
        print(x)
    elif a=="comb":
        math.comb(x)
        print(x)
    elif a=="copysign" :
        math.copysign(x)
        print(x)
    elif a=="cos":
        math.cos(x)
        print(x)
    elif a=="cosh":
        math.cosh(x)
        print(x)
    elif a=="degrees":
        math.degrees(x)
        print(x)
    elif a=="dist":
        math.degrees(x)
        print(x)
    elif a=="erf":
        math.erf(x)
        print(x)
    elif a=="acos":
        math.acos(x)
        print(x)
    elif a== "erfc":
        print(math.erfc(x))
        
    elif a== "exp":
        print(math.exp(x))
        
    elif a== "expm1":
        print(math.expm1(x))
        
    elif a=="fabs":
        print(math.fabs(x))
        
    elif a=="factorial":
        print(math.floor(x))
        
    elif a=="floor":
        print(math.floor(x))
    elif a=="log2":
        print(math.log2(x))
    elif a=="f":
        print("Programdan Çıkış Yapıyorsunuz...")
        break
    elif a=="fmod":
     print(math.fmod(x,z))
    elif a=="frexp":
        print(math.frexp(x))
    elif a=="fsum":
        print(math.fsum(x))
    elif a=="gamma":
        print(math.gamma(x))
    elif a== "gcd":
        x=int(x)
        print(math.gcd(x))
    elif a=="hypot":
        print(math.hypot(x))
    elif a== 'inf':
        print(math.inf(x))
    elif a== 'isclose':
        print(math.isclose(x,z))
    elif a== 'isfinite':
        print(math.isfinite(x))
    elif a== 'isinf':
        print(math.isinf(x)) 
    elif a=='isnan':
        print(math.isnan(x))
    elif a=="isqrt":
        print(math.isqrt(x))
    elif a=='lcm':
        x=int(x)
        print(math.lcm(x)) 
    elif a=='ldexp':
        z=int(z)
        print(math.ldexp(x,z))
    elif a== 'lgamma':
        print(math.lgamma(x))
    elif a== 'log':
        print(math.log(x))
    elif a== 'log10':
        print(math.log10(x))
    elif a== 'log1p':
        print(math.log1p(x)) 
    elif a=='modf':
        print(math.modf(x))
    elif a== 'nan':
        print(math.nan(x))
    elif a== 'nextafter':
        print(math.nextafter(x))
    elif a== 'perm':
        print(math.perm(x)) 
    elif a=='pi':
        print(math.pi(x))
    elif a== 'pow':
        print(math.pow(x,z))
    elif a== 'prod':
        print(math.prod(x))
    elif a== 'radians':
        print(math.radians(x))
    elif a== 'remainder':
        print(math.remainder(x,z))
    elif a== 'sin':
        print(math.sin(x))
    elif a== 'sinh':
        print(math.sinh(x))
    elif a== 'sqrt':
        print(math.sqrt(x))
    elif a== 'tan':
        print(math.tan(x))
    elif a== 'tanh':
        print(math.tanh(x))
    elif a== 'tau':
        print(math.tau(x))
    elif a== 'trunc':
        print(math.trunc(x))
    elif a== 'ulp':
        print(math.ulp(x))
    else:
        print("Yanlış Yazdınız...")

    Işlem_Hakkı -=1