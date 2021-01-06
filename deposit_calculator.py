deposit_sum = float(input())
duration_deposit_month = int(input())
yearly_percentage = float(input())
interest = deposit_sum * (yearly_percentage/100)
interest_per_moth = interest/12

result_sum = deposit_sum + duration_deposit_month * interest_per_moth
print(result_sum)