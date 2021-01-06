num = int(input())
bonus = 0

if num <= 100:
    bonus = 5
elif 101 <= num <= 999:
    bonus = num * 0.20
elif num > 1000:
    bonus = num * 0.10
if num % 2 == 0:
    bonus = 1 + bonus
elif num % 5 == 0:
    bonus = 2 + bonus

print(bonus)
print(bonus + num)
