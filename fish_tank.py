length = int(input())
width = int(input())
heigth = int(input())

volum = float(input())
total_vol = length*width*heigth
liter = total_vol*0.001
persent = volum/100
total_water = liter-persent*liter
print(total_water)
