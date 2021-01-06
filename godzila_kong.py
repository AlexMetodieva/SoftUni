buget = float(input())
statisti = int(input())
cena_obleklo = float(input())

sum_dekor = buget * 0.10
sum_obleklo = statisti * cena_obleklo

if statisti > 150:
    sum_obleklo -= (sum_obleklo * 0.10)
money = sum_dekor + sum_obleklo
nedostig = - (buget - money)
ostatuk = buget - money

if money > buget:
    print(f"Not enough money!\nWingard needs {nedostig:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {ostatuk:.2f} leva left.")
