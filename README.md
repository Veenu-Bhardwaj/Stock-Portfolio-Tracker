📈 Stock Portfolio Tracker — Python Project
A Python application to track your stock portfolio with automatic profit/loss calculation and permanent data saving.

✨ Features
➕ Add multiple stocks with company name, shares and buy price
💹 Update current market prices anytime
📊 Automatic Profit and Loss calculation per stock
📈 Shows percentage change for each stock
💰 Overall portfolio summary with total invested and current value
💾 Saves all data permanently to JSON file — data stays even after closing
🗑️ Remove stocks from portfolio with confirmation
📋 Clean menu-driven interface

🛠️ Tech Stack
Language: Python 3.x
Libraries used: json, os, datetime (all built-in — no installation needed)

⚙️ How to Run
Step 1 — Make sure Python is installed
Open Command Prompt or Terminal and type:
python --version
You should see: Python 3.x.x
If not installed, download from: https://python.org/downloads

Step 2 — Download the code
Click the green Code button → Download ZIP → Extract
OR with Git:
git clone https://github.com/Veenu-Bhardwaj/Stock-Portfolio-Tracker.git

Step 3 — Navigate to the folder
cd Stock-Portfolio-Tracker

Step 4 — Run the program
python stock_portfolio.py
On some Windows systems:
py stock_portfolio.py

Step 5 — Use the menu
Choose options 1 to 6 from the menu

Note: portfolio.json is created automatically when you add your first stock. This file saves all your data permanently.

🔧 Customization
Change the currency symbol by finding this in the code:

pythonf"₹{buy_price:<9.2f}"
Replace ₹ with $ for USD or any other currency symbol.

🚀 Future Improvements
 Connect to live stock API (Yahoo Finance or Alpha Vantage)
 Add price history graph using Matplotlib
 Add buy/sell transaction history
 Export portfolio report to PDF or Excel
 Add stop-loss alerts
 Build web interface using Flask

👩‍💻 About the Developer
Veenu Bhardwaj
🎓 BTech CSE (AI & Data Science) — GITM Gurugram
🏆 3x University Topper (Semester 1, 2, 3)
💼 Open to internships and opportunities
🔗 LinkedIn: linkedin.com/in/veenu-bhardwaj-96952434b
🐙 GitHub: github.com/Veenu-Bhardwaj

⭐ If you found this useful, please star the repository!
