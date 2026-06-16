# ============================================
# TASK 2 — STOCK PORTFOLIO TRACKER
# CodeAlpha Python Programming Internship
# Author: Veenu Bhardwaj
# ============================================
 
# json = built-in Python tool to save/load data
# Like saving your portfolio to a notebook
import json
 
# os = helps us check if files exist on computer
import os
 
# datetime = gives us current date and time
from datetime import datetime
 
# ============================================
# WHAT IS THIS PROGRAM?
# A portfolio = collection of stocks you own
# This program lets you:
# 1. Add stocks you bought
# 2. See your profit or loss
# 3. Save your portfolio
# 4. View all your stocks anytime
# ============================================
 
# File where we save portfolio data
# Like a notebook on your computer
PORTFOLIO_FILE = "portfolio.json"
 
# ============================================
# STEP 1 — LOAD PORTFOLIO FROM FILE
# ============================================
def load_portfolio():
    # Check if portfolio file exists already
    if os.path.exists(PORTFOLIO_FILE):
        # Open the file and read data
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    # If no file exists, start with empty portfolio
    return {}
 
# ============================================
# STEP 2 — SAVE PORTFOLIO TO FILE
# ============================================
def save_portfolio(portfolio):
    # Save portfolio dictionary to JSON file
    # indent=4 makes it readable if you open the file
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f, indent=4)
    print("✅ Portfolio saved successfully!")
 
# ============================================
# STEP 3 — ADD A STOCK
# ============================================
def add_stock(portfolio):
    print("\n" + "="*50)
    print("         ADD NEW STOCK")
    print("="*50)
 
    # Ask for stock symbol
    # Symbol = short name of company
    # Example: APPLE, GOOGLE, TCS, RELIANCE
    symbol = input("\nEnter stock symbol (e.g. AAPL, TCS): ").upper()
    # .upper() converts to CAPITAL LETTERS
 
    # Ask for company name
    company = input("Enter company name (e.g. Apple Inc): ")
 
    # Ask how many shares bought
    # shares = number of stocks purchased
    while True:
        try:
            shares = float(input("Enter number of shares bought: "))
            if shares <= 0:
                print("⚠️  Shares must be more than 0!")
                continue
            break
        except ValueError:
            print("⚠️  Please enter a valid number!")
 
    # Ask the price at which you bought
    # buy_price = price per share when you bought it
    while True:
        try:
            buy_price = float(input("Enter buying price per share (₹ or $): "))
            if buy_price <= 0:
                print("⚠️  Price must be more than 0!")
                continue
            break
        except ValueError:
            print("⚠️  Please enter a valid number!")
 
    # Calculate total amount invested
    # Example: 10 shares × ₹500 = ₹5000 invested
    total_invested = shares * buy_price
 
    # Save this stock in our portfolio dictionary
    # dictionary = like a form with fields
    portfolio[symbol] = {
        "company": company,
        "shares": shares,
        "buy_price": buy_price,
        "total_invested": total_invested,
        "date_added": datetime.now().strftime("%d-%m-%Y %H:%M")
        # datetime.now() = current date and time
        # strftime = format it nicely
    }
 
    print(f"\n✅ {company} ({symbol}) added successfully!")
    print(f"   Shares: {shares}")
    print(f"   Buy Price: ₹{buy_price:.2f}")
    print(f"   Total Invested: ₹{total_invested:.2f}")
 
    # Save to file immediately
    save_portfolio(portfolio)
 
# ============================================
# STEP 4 — UPDATE CURRENT PRICE
# ============================================
def update_price(portfolio):
    # Since we don't have live internet API in basic version
    # We ask user to enter current market price manually
    # (In advanced version this fetches automatically)
 
    if not portfolio:
        print("\n⚠️  Portfolio is empty! Add stocks first.")
        return
 
    print("\n" + "="*50)
    print("      UPDATE CURRENT PRICES")
    print("="*50)
    print("\nYour stocks:")
 
    # Show all stocks
    for i, symbol in enumerate(portfolio, 1):
        print(f"{i}. {symbol} — {portfolio[symbol]['company']}")
 
    symbol = input("\nEnter stock symbol to update price: ").upper()
 
    if symbol not in portfolio:
        print(f"⚠️  {symbol} not found in portfolio!")
        return
 
    while True:
        try:
            current_price = float(input(f"Enter current market price of {symbol}: ₹"))
            if current_price <= 0:
                print("⚠️  Price must be more than 0!")
                continue
            break
        except ValueError:
            print("⚠️  Please enter valid number!")
 
    # Save current price to portfolio
    portfolio[symbol]["current_price"] = current_price
    portfolio[symbol]["last_updated"] = datetime.now().strftime("%d-%m-%Y %H:%M")
 
    save_portfolio(portfolio)
    print(f"✅ Price of {symbol} updated to ₹{current_price:.2f}")
 
# ============================================
# STEP 5 — VIEW PORTFOLIO (MAIN FEATURE!)
# ============================================
def view_portfolio(portfolio):
    if not portfolio:
        print("\n⚠️  Portfolio is empty! Add stocks first.")
        return
 
    print("\n" + "="*70)
    print("                    YOUR STOCK PORTFOLIO")
    print("             By Veenu Bhardwaj — CodeAlpha Intern")
    print("="*70)
    print(f"{'SYMBOL':<10} {'COMPANY':<20} {'SHARES':<8} {'BUY':<10} {'CURRENT':<10} {'P&L':<12} {'STATUS'}")
    print("-"*70)
 
    # Variables to track totals
    total_invested = 0
    total_current = 0
    total_profit_loss = 0
 
    for symbol, data in portfolio.items():
        shares = data["shares"]
        buy_price = data["buy_price"]
        invested = data["total_invested"]
 
        # Check if current price is available
        if "current_price" in data:
            current_price = data["current_price"]
            current_value = shares * current_price
 
            # Profit/Loss calculation
            # profit_loss = current value - amount invested
            profit_loss = current_value - invested
 
            # Percentage change
            # How much % did price change
            pct_change = ((current_price - buy_price) / buy_price) * 100
 
            # Status emoji
            if profit_loss > 0:
                status = "📈 PROFIT"
            elif profit_loss < 0:
                status = "📉 LOSS"
            else:
                status = "➡️  SAME"
 
            # Add to totals
            total_invested += invested
            total_current += current_value
            total_profit_loss += profit_loss
 
            # Print this stock row
            print(f"{symbol:<10} {data['company'][:18]:<20} {shares:<8.1f} "
                  f"₹{buy_price:<9.2f} ₹{current_price:<9.2f} "
                  f"₹{profit_loss:<11.2f} {status} ({pct_change:+.1f}%)")
        else:
            # No current price yet
            total_invested += invested
            print(f"{symbol:<10} {data['company'][:18]:<20} {shares:<8.1f} "
                  f"₹{buy_price:<9.2f} {'N/A':<10} {'N/A':<12} ⏳ Update price")
 
    # Show summary at bottom
    print("="*70)
    print(f"\n💰 PORTFOLIO SUMMARY:")
    print(f"   Total Invested:     ₹{total_invested:,.2f}")
 
    if total_current > 0:
        print(f"   Current Value:      ₹{total_current:,.2f}")
        overall_pl = total_current - total_invested
        overall_pct = ((total_current - total_invested) / total_invested) * 100
 
        if overall_pl > 0:
            print(f"   Overall Profit:     ₹{overall_pl:,.2f} 📈 (+{overall_pct:.1f}%)")
        else:
            print(f"   Overall Loss:       ₹{abs(overall_pl):,.2f} 📉 ({overall_pct:.1f}%)")
 
    print(f"\n   Total Stocks in Portfolio: {len(portfolio)}")
    print(f"   Report Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}")
    print("="*70)
 
# ============================================
# STEP 6 — REMOVE A STOCK
# ============================================
def remove_stock(portfolio):
    if not portfolio:
        print("\n⚠️  Portfolio is empty!")
        return
 
    print("\n" + "="*50)
    print("         REMOVE STOCK")
    print("="*50)
 
    # Show all stocks first
    for symbol, data in portfolio.items():
        print(f"  {symbol} — {data['company']}")
 
    symbol = input("\nEnter stock symbol to remove: ").upper()
 
    if symbol not in portfolio:
        print(f"⚠️  {symbol} not found!")
        return
 
    # Confirm before deleting
    confirm = input(f"Are you sure you want to remove {symbol}? (yes/no): ").lower()
    if confirm == "yes" or confirm == "y":
        del portfolio[symbol]
        # del = delete from dictionary
        save_portfolio(portfolio)
        print(f"✅ {symbol} removed from portfolio!")
    else:
        print("❌ Removal cancelled.")
 
# ============================================
# STEP 7 — SHOW SUMMARY ONLY
# ============================================
def show_summary(portfolio):
    if not portfolio:
        print("\n⚠️  Portfolio is empty!")
        return
 
    total_invested = sum(data["total_invested"] for data in portfolio.values())
    # sum() adds all values together
    # portfolio.values() = all stock data
 
    print("\n" + "="*50)
    print("         PORTFOLIO SUMMARY")
    print("="*50)
    print(f"  Total Stocks: {len(portfolio)}")
    print(f"  Total Invested: ₹{total_invested:,.2f}")
    print(f"  Stocks: {', '.join(portfolio.keys())}")
    # .keys() = all stock symbols
    # ', '.join() = combines them with comma
    print("="*50)
 
# ============================================
# STEP 8 — MAIN MENU
# ============================================
def main():
    # Load existing portfolio when program starts
    portfolio = load_portfolio()
 
    print("\n" + "="*50)
    print("      STOCK PORTFOLIO TRACKER")
    print("   By Veenu Bhardwaj — CodeAlpha Intern")
    print("="*50)
 
    # Main loop — keeps running until user exits
    while True:
        print("\n📊 MAIN MENU:")
        print("  1. Add New Stock")
        print("  2. View Full Portfolio")
        print("  3. Update Stock Price")
        print("  4. Remove Stock")
        print("  5. Portfolio Summary")
        print("  6. Exit")
        print("-"*30)
 
        choice = input("Enter your choice (1-6): ")
 
        # Match choice to function
        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            view_portfolio(portfolio)
        elif choice == "3":
            update_price(portfolio)
        elif choice == "4":
            remove_stock(portfolio)
        elif choice == "5":
            show_summary(portfolio)
        elif choice == "6":
            print("\n👋 Thank you for using Stock Portfolio Tracker!")
            print("   — Veenu Bhardwaj, CodeAlpha Intern\n")
            break
            # break = exit the while loop
        else:
            print("⚠️  Invalid choice! Please enter 1-6.")
 
# Start the program
if __name__ == "__main__":
    main()
 