"""
Stock Portfolio Tracker
-----------------------
A simple program to track stock investments using predefined prices.
"""

import csv

# Hardcoded dictionary of stock prices (symbol -> price per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400,
    "AMZN": 170,
}


def display_available_stocks():
    """Show all available stocks and their current prices."""
    print("\n" + "=" * 40)
    print("       AVAILABLE STOCKS")
    print("=" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6}  ${price:>6.2f}")
    print("=" * 40)


def get_valid_stock_name():
    """
    Ask the user for a stock symbol and validate it.
    Returns the symbol in uppercase when valid.
    """
    while True:
        stock_name = input("\nEnter stock symbol (e.g. AAPL): ").strip().upper()

        if stock_name in STOCK_PRICES:
            return stock_name

        print(f"  Error: '{stock_name}' is not a valid stock.")
        print(f"  Please choose from: {', '.join(STOCK_PRICES.keys())}")


def get_valid_quantity():
    """
    Ask the user for a quantity and validate it.
    Returns a positive whole number.
    """
    while True:
        quantity_input = input("Enter quantity (whole number): ").strip()

        # Check that the input is a positive integer
        if quantity_input.isdigit() and int(quantity_input) > 0:
            return int(quantity_input)

        print("  Error: Quantity must be a positive whole number (e.g. 1, 5, 10).")


def calculate_stock_value(stock_name, quantity):
    """
    Calculate the investment value for one stock.
    Value = price per share × quantity
    """
    price = STOCK_PRICES[stock_name]
    return price * quantity


def add_to_portfolio(portfolio, stock_name, quantity):
    """
    Add a stock purchase to the portfolio.
    If the stock already exists, the quantities are combined.
    """
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity


def ask_add_another_stock():
    """
    Ask the user if they want to add another stock.
    Returns True for yes, False for no.
    """
    while True:
        choice = input("\nAdd another stock? (yes/no): ").strip().lower()

        if choice in ("yes", "y"):
            return True
        if choice in ("no", "n"):
            return False

        print("  Error: Please enter 'yes' or 'no'.")


def display_portfolio_summary(portfolio):
    """Display a clean summary of all stocks in the portfolio."""
    print("\n" + "=" * 50)
    print("           PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("-" * 50)

    for stock_name, quantity in portfolio.items():
        price = STOCK_PRICES[stock_name]
        value = calculate_stock_value(stock_name, quantity)
        print(f"  {stock_name:<8} {quantity:>6} ${price:>9.2f} ${value:>11.2f}")

    print("=" * 50)


def calculate_total_investment(portfolio):
    """
    Calculate the total value of all stocks in the portfolio.
    Returns the total investment amount.
    """
    total = 0
    for stock_name, quantity in portfolio.items():
        total += calculate_stock_value(stock_name, quantity)
    return total


def ask_save_report():
    """
    Ask the user if they want to save the portfolio report.
    Returns True for yes, False for no.
    """
    while True:
        choice = input("\nSave portfolio report to CSV? (yes/no): ").strip().lower()

        if choice in ("yes", "y"):
            return True
        if choice in ("no", "n"):
            return False

        print("  Error: Please enter 'yes' or 'no'.")


def save_report_to_csv(portfolio, total_investment, filename="portfolio_report.csv"):
    """
    Save the portfolio summary to a CSV file.
    Includes stock name, quantity, price, value, and total investment.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["Stock", "Quantity", "Price", "Value"])

        # Write one row per stock
        for stock_name, quantity in portfolio.items():
            price = STOCK_PRICES[stock_name]
            value = calculate_stock_value(stock_name, quantity)
            writer.writerow([stock_name, quantity, price, value])

        # Write total investment at the bottom
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    print(f"\n  Report saved successfully to '{filename}'")


def main():
    """Run the stock portfolio tracker program."""
    print("\n*** Welcome to the Stock Portfolio Tracker ***")

    # Dictionary to store the user's portfolio: {stock_symbol: quantity}
    portfolio = {}

    # Step 1: Show available stocks
    display_available_stocks()

    # Step 2-6: Let the user add stocks (repeat if they want more)
    while True:
        stock_name = get_valid_stock_name()
        quantity = get_valid_quantity()
        value = calculate_stock_value(stock_name, quantity)

        add_to_portfolio(portfolio, stock_name, quantity)
        print(f"\n  Added {quantity} share(s) of {stock_name} — Value: ${value:.2f}")

        if not ask_add_another_stock():
            break

    # Step 7: Show portfolio summary
    if not portfolio:
        print("\n  No stocks were added. Goodbye!")
        return

    display_portfolio_summary(portfolio)

    # Step 8: Calculate and display total investment
    total_investment = calculate_total_investment(portfolio)
    print(f"\n  TOTAL INVESTMENT VALUE: ${total_investment:.2f}")

    # Step 9: Optionally save the report to CSV
    if ask_save_report():
        save_report_to_csv(portfolio, total_investment)

    print("\n*** Thank you for using the Stock Portfolio Tracker! ***\n")


# Run the program when this file is executed directly
if __name__ == "__main__":
    main()
