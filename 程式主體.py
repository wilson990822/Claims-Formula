from decimal import Decimal, ROUND_HALF_UP
import re
print("How are you today?" )
type = input("請輸入保單類型:")
Premium = int(input("請輸入保費:"))
lyear = list(map(int, input("請輸入年期:").split()))
Sum_insured = Decimal(input("請輸入保額:"))
Increase_factor = Decimal(input("請輸入增額係數:"))
prior_year = int(input("請輸入前一年末保價:"))
current_year = int(input("請輸入當年度保價:"))
day = int(input("請輸入自周期日至事故日之天數:"))
def first_count(a, b, c):
    t = Decimal(a*1.03*min(b)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    return Decimal(t*c).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
def second_count(a, b, c, d):
    k = Decimal(a+(b-a)*(c/365)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
    return Decimal(k*d*1).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
def IWJ(Premium, lyear, Sum_insured, Increase_factor, prior_year, current_year, day):
    A = first_count(Premium, lyear, Sum_insured)
    B = first_count(Premium, lyear, Increase_factor)
    C = second_count(prior_year, current_year, day, Sum_insured)
    D = second_count(prior_year, current_year, day, Increase_factor)
    return max(A, C)+max(B, D)
match type:
    case "IWJ":
        print(IWJ(Premium, lyear, Sum_insured, Increase_factor, prior_year, current_year, day))