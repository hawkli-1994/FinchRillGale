import yfinance as yf

df = yf.download('BTC-USD', start='2025-01-01', end='2025-8-18', interval='4h', proxy={'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'})
df.to_csv('./data/yahoo_btc_4h.csv')