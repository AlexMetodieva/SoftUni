strawberries_price = float(input())
bananas_weigh = float(input())
oranges_weigh = float(input())
raspberries_weigh = float(input())
strawberries_weigh = float(input())

raspberries_price = 1/2 * strawberries_price
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price
total_price = (strawberries_price * strawberries_weigh + oranges_price * oranges_weigh\
              + bananas_price * bananas_weigh + raspberries_price * raspberries_weigh)
print(total_price)
