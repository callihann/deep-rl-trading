from tradingSimulator import TradingSimulator

full_stock_list = [
    "Apple Inc",
    "Abbvie Inc",
    "Abbott Laboratories",
    "Accenture Plc",
    "Adobe Systems Inc",
    "American International Group",
    "Adv Micro Devices",
    "Amgen Inc",
    "American Tower Corp",
    "Amazon.com Inc",
    "Broadcom Ltd",
    "American Express Company",
    "Boeing Company",
    "Bank of America Corp",
    "Bank of New York Mellon Corp",
    "Booking Holdings Inc",
    "Blackrock Inc",
    "Bristol-Myers Squibb Company",
    "Berkshire Hathaway Cl B", # broken stopping point
    "Citigroup Inc",
    "Costco Wholesale",
    "Emerson Electric Company",
    "Johnson & Johnson",
    "Coca-Cola Company",
    "Mastercard Inc",
    "Nike Inc",
    "Oracle Corp",
    "Philip Morris International Inc",
    "Rtx Corp",
    "Starbucks Corp",
    "Simon Property Group",
    "Wells Fargo & Company",
]

partial_stock_list = [
    "Citigroup Inc",
    "Costco Wholesale",
    "Emerson Electric Company",
    "Johnson & Johnson",
    "Coca-Cola Company",
    "Mastercard Inc",
    "Nike Inc",
    "Oracle Corp",
    "Philip Morris International Inc",
    "Rtx Corp",
    "Starbucks Corp",
    "Simon Property Group",
    "Wells Fargo & Company",
]

if __name__ == '__main__':
    for i in full_stock_list:
        simulator = TradingSimulator()
        strategy = 'TDQN'
        stock = i
        try:
            simulator.simulateNewStrategy(strategy, stock, saveStrategy=False)
        except Exception as e:
            print(e)
            print("Error with stock: " + stock)
            pass

