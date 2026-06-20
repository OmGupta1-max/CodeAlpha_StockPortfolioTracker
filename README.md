# Stock Portfolio Tracker

A beginner-friendly Python console application that helps you track stock investments using predefined prices. Build a portfolio, view a summary, calculate your total investment value, and optionally export a report to CSV.

---

## Project Overview

The **Stock Portfolio Tracker** is a command-line program designed for learners who want to practice core Python concepts in a practical context. Users select stocks from a predefined list, enter purchase quantities, and the program calculates the value of each holding and the overall portfolio.

The project emphasizes clean structure through functions, input validation, formatted console output, and file handling — all using only Python's built-in modules.

---

## Features

- **Predefined stock prices** — Uses a hardcoded dictionary of popular stocks (AAPL, TSLA, GOOG, MSFT, AMZN)
- **Multiple stock purchases** — Add as many stocks as you like in a single session
- **Input validation** — Rejects invalid stock symbols and non-positive quantities
- **Portfolio summary** — Displays a formatted table with stock, quantity, price, and value
- **Total investment calculation** — Automatically sums the value of all holdings
- **CSV export** — Optionally save the portfolio report to `portfolio_report.csv`
- **Modular design** — Logic is organized into small, reusable functions with comments

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core programming language |
| **csv** (built-in) | Writing portfolio reports to CSV files |
| **input() / print()** | User interaction via the console |
| **Dictionaries** | Storing stock prices and portfolio holdings |

> No external libraries are required. Only Python's standard library is used.

---

## Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── stock_tracker.py      # Main application (run this file)
├── requirements.txt      # Project goals and feature specifications
├── flow.txt              # Program flow diagram
├── README.md             # Project documentation (this file)
└── portfolio_report.csv  # Generated after saving a report (optional)
```

---

## How to Run

### Prerequisites

- Python 3.6 or higher installed on your system

### Steps

1. **Clone or download** this project to your local machine.

2. **Open a terminal** and navigate to the project folder:

   ```bash
   cd CodeAlpha_StockPortfolioTracker
   ```

3. **Run the program**:

   ```bash
   python stock_tracker.py
   ```

4. **Follow the on-screen prompts** to add stocks, view your summary, and save your report.

---

## Sample Workflow

```
START
  │
  ▼
Display Available Stocks
  │
  ▼
User Enters Stock Name ──► Invalid? ──► Show Error & Retry
  │                              │
  ▼                              ▼
Enter Quantity ──────────► Invalid? ──► Show Error & Retry
  │
  ▼
Calculate Value & Add to Portfolio
  │
  ▼
Add Another Stock? ── Yes ──► Loop back to stock entry
  │
  No
  ▼
Display Portfolio Summary
  │
  ▼
Calculate Total Investment
  │
  ▼
Save to CSV? ── Yes ──► Save portfolio_report.csv
  │
  No
  ▼
END
```

### Step-by-step example

1. The program displays available stocks and their prices.
2. Enter a stock symbol, e.g. `AAPL`.
3. Enter a quantity, e.g. `10`.
4. The program confirms the purchase and its value.
5. Choose `yes` to add another stock, or `no` to finish.
6. Review the portfolio summary and total investment value.
7. Choose `yes` to save the report to CSV, or `no` to exit.

---

## Example Output

### Available stocks

```
========================================
       AVAILABLE STOCKS
========================================
  AAPL    $180.00
  TSLA    $250.00
  GOOG    $150.00
  MSFT    $400.00
  AMZN    $170.00
========================================
```

### Adding stocks

```
Enter stock symbol (e.g. AAPL): AAPL
Enter quantity (whole number): 10

  Added 10 share(s) of AAPL — Value: $1800.00

Add another stock? (yes/no): yes

Enter stock symbol (e.g. AAPL): TSLA
Enter quantity (whole number): 5

  Added 5 share(s) of TSLA — Value: $1250.00

Add another stock? (yes/no): no
```

### Portfolio summary

```
==================================================
           PORTFOLIO SUMMARY
==================================================
  Stock       Qty      Price        Value
--------------------------------------------------
  AAPL         10 $   180.00 $    1800.00
  TSLA          5 $   250.00 $    1250.00
==================================================

  TOTAL INVESTMENT VALUE: $3050.00

Save portfolio report to CSV? (yes/no): yes

  Report saved successfully to 'portfolio_report.csv'

*** Thank you for using the Stock Portfolio Tracker! ***
```

### CSV report (`portfolio_report.csv`)

```csv
Stock,Quantity,Price,Value
AAPL,10,180,1800
TSLA,5,250,1250

Total Investment,,,3050
```

---

## Learning Outcomes

By building and running this project, you will practice:

- **Variables and data types** — Integers, strings, and dictionaries
- **Functions** — Breaking a program into small, focused, reusable pieces
- **Control flow** — `while` loops, `if/else` conditions, and user input handling
- **Input validation** — Checking user input before processing it
- **String formatting** — Creating clean, aligned console output with f-strings
- **File I/O** — Reading and writing data to a CSV file using the `csv` module
- **Program structure** — Using `main()` and `if __name__ == "__main__"` as entry points

---


## Author

Om Gupta

Created as part of the CodeAlpha Python Programming Internship.
