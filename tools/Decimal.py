# use Fraction from fractions first

from decimal import Decimal, ROUND_DOWN

a, b = input().split()
c = Decimal(a) * Decimal(b)

print(Decimal(c).quantize(1, rounding=ROUND_DOWN))

