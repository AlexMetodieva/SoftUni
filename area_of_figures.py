from math import pi
figure = input()

if figure == "square":
    a = float(input())
    S = (a*a)
    print(f"{S:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    S = (a*b)
    print(f"{S:.3f}")
elif figure == "circle":
    r = float(input())
    S = (pi * (r*r))
    print(f"{S:.2f}")
elif figure == "triangle":
    a = float(input())
    h = float(input())
    S = ((a/2) * h)
    print(f"{S:.3f}")



