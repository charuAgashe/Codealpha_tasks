# Stock Portfolio Tracker
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320
}

portfolio = {}
total = 0

n = int(input("Enter number of stocks: "))
print(stock_prices)
for i in range(n):
    name = input("Enter stock name: ").upper()
    
    if name in stock_prices:
        qty = int(input("Enter quantity: "))
        portfolio[name] = qty
    else:
        print("Stock not found")

print("\nPortfolio Details:")
for stock in portfolio:
    price = stock_prices[stock]
    value = price * portfolio[stock]
    total += value
    print(stock, ":", portfolio[stock], "shares =", value)

print("\nTotal Investment =", total)

# saving to file
file = open("portfolio.txt", "a")
file.write("\nPortfolio Summary\n")

for stock in portfolio:
    price = stock_prices[stock]
    value = price * portfolio[stock]
    file.write(stock + " " + str(value) + "\n")

file.write("Total = " + str(total))
file.close()