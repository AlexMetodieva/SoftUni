number = float(input())
inputme = input()
output = input()

if inputme == "m" and output == "cm":
    number *= 100
elif inputme == "m" and output == "mm":
    number *= 1000
elif inputme == "cm" and output == "m":
    number /= 100
elif inputme == "cm" and output == "mm":
    number *= 10
elif inputme == "mm" and output == "m":
    number /= 1000
elif inputme == "mm" and output == "cm":
    number /= 10

print(f"{number:.3f}")