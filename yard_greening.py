square_meters = float(input())

price = square_meters * 7.61
discount = price * 0.18
price = price - discount

print("The final price is: " + str(price) + " lv.")
print("The discount is: " + str(discount) + " lv.")
