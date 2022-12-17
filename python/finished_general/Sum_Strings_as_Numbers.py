'''
Given the string representations of two integers, return the string representation of the 
sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int 
will not work.
'''

from time import perf_counter
from itertools import zip_longest as zipL

def sum_strings(x, y):
    result = ""
    carry = 0
    for a, b in zipL(x[::-1],y[::-1], fillvalue='0'):
        temp = int(a)+int(b)+carry
        result += str(temp%10)
        carry = 1 if temp > 9 else 0
    result += str(carry)
    result = result[::-1].lstrip("0")
    return result if result else "0"


def assert_equals(a, b):
    try:
        assert a == b
        print(f"success! {a} == {b}")
    except:
        print(f"failed {a} not equal to {b}")

assert_equals(sum_strings("1", "1"), "2")
assert_equals(sum_strings("50","50"),"100")
assert_equals(sum_strings("75","25"),"100")
assert_equals(sum_strings("100","0"),"100")

start_f = perf_counter()
# sum_strings("1"*10**6, "1"*10**6)
end_f = perf_counter()
print(f"time for fast function was {end_f-start_f}")