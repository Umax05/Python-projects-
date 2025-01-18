import yfinance as yf
import pandas as pd

def get_stock_price(ticker_symbols):
    stock_data = []
    for symbol in ticker_symbols:
        try:
            stock = yf.Ticker(symbol)
            data = stock.info
            current_price = data.get('currentPrice', 'N/A')
            previous_close = data.get('previousClose', 'N/A')
            day_high = data.get('dayHigh', 'N/A')
            day_low = data.get('dayLow', 'N/A')
            volume = data.get('volume', 'N/A')
            
            if previous_close != 'N/A' and current_price != 'N/A':
                percent_change = ((current_price - previous_close) / previous_close) * 100
                percent_change = round(percent_change, 2)
            else:
                percent_change = 'N/A'
            
            stock_info = {
                'Ticker': symbol.upper(),
                'Current Price': current_price,
                'Previous Close': previous_close,
                'Day High': day_high,
                'Day Low': day_low,
                'Volume': volume,
                'Percentage Change (%)': percent_change
            }
            stock_data.append(stock_info)
            
        except Exception as e:
            print(f"Error fetching data for {symbol.upper()}: {e}")
    
    if stock_data:
        df = pd.DataFrame(stock_data)
        print(df.to_string(index=False))
    else:
        print("No valid stock data to display.")

def main():
    print("=== Enhanced Stock Price Checker ===")
    while True:
        tickers = input("Enter stock ticker symbol(s) separated by commas (or type 'exit' to quit): ").strip()
        if tickers.lower() == 'exit':
            print("Exiting Stock Price Checker. Goodbye!")
            break
        elif tickers == '':
            print("Please enter at least one ticker symbol.")
            continue
        else:
            ticker_list = [ticker.strip().upper() for ticker in tickers.split(',') if ticker.strip() != '']
            if not ticker_list:
                print("No valid ticker symbols entered.")
                continue
            get_stock_price(ticker_list)

if __name__ == "__main__":
    main()
