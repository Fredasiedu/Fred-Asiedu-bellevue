def main():
   # Define the dictionary of stocks
   stocks = {
       "AAPL": 150.25,
       "GOOGL": 2500.50,
       "MSFT": 300.75,
       "AMZN": 3500.00,
       "FB": 350.25,
       "TSLA": 650.75,
       "NFLX": 600.50,
       "NVDA": 800.00,
       "JPM": 150.75,
       "BAC": 40.25
   }

   # Ask the user for a ticker symbol
   ticker_symbol = input("Enter a ticker symbol: ")

   # Search for the ticker symbol in the dictionary
   if ticker_symbol in stocks:
       stock_price = stocks[ticker_symbol]
       print(f"The stock price for {ticker_symbol} is ${stock_price:.2f}")
   else:
       print("Ticker symbol not found.")


# Run the program
main()