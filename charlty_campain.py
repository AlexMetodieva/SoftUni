
count_days = int(input())
count_cooks = int(input())
count_cake = int(input())
count_waffles = int(input())
count_pancakes = int(input())

price_cake = 45
price_waffles = 5.8
price_pancakes = 3.20

daily_wage = (count_cake * price_cake + count_waffles * price_waffles + count_pancakes * price_pancakes) *count_cooks
total_sum = daily_wage * count_days
charlty_money = total_sum - 1/8 * total_sum
print(charlty_money)