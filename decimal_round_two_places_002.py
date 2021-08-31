import decimal
from decimal import Decimal

float_for = format(2.005500123, ".3f")
print(float_for)
print(type(float_for))

dec001 = Decimal(float_for)

ctx = decimal.getcontext()
ctx.rounding = decimal.ROUND_HALF_UP

limit_dec001 = round(dec001, 2)
print(limit_dec001)

my_float002 = 2.675
limit_float002 = round(my_float002, 2)
print(limit_float002)

# import decimal
# from decimal import Decimal
#
#
# ctx = decimal.getcontext()
# ctx.rounding = decimal.ROUND_HALF_UP
#
# x = Decimal('2.25')
# y = Decimal('3.35')
#
# print(round(x, 1))
# print(round(y, 1))
