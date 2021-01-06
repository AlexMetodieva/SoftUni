excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum_puzzles = puzzles * 2.6
sum_dolls = dolls * 3
sum_bears = bears * 4.1
sum_minions = minions * 8.2
sum_trucks = trucks * 2
total_sum = sum_puzzles + sum_dolls + sum_bears + sum_minions + sum_trucks
num = puzzles + dolls + bears + minions + trucks
if num >= 50:
    total_sum = total_sum -(total_sum*0.25)
rent = total_sum * 0.10
total_sum -= rent
yes = total_sum - excursion
no = excursion - total_sum
if excursion <= total_sum:
    print(f"Yes! {yes:.2f} lv left.")
else:
    print(f"Not enough money! {no:.2f} lv needed.")