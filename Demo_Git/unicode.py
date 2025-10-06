import pandas as pd

# Initialize total sum
total_sum = 0

# List of symbols to match
symbols_to_match = ["š", "–", "•"]

# --- Process data1.csv (CP-1252) ---
df1 = pd.read_csv('data1.csv', encoding='cp1252')
total_sum += df1[df1['symbol'].isin(symbols_to_match)]['value'].sum()

# --- Process data2.csv (UTF-8) ---
df2 = pd.read_csv('data2.csv', encoding='utf-8')
total_sum += df2[df2['symbol'].isin(symbols_to_match)]['value'].sum()

# --- Process data3.txt (UTF-16, tab-separated) ---
df3 = pd.read_csv('data3.txt', encoding='utf-16', sep='\t')
total_sum += df3[df3['symbol'].isin(symbols_to_match)]['value'].sum()

print("Total sum of values for symbols š, –, •:", total_sum)