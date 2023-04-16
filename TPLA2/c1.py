import requests
import matplotlib.pyplot as plt

# Prompt user to enter app_id and currency codes
app_id = input("Enter your Open Exchange Rates app_id: ")
from_currency = input("Enter the 3-letter code for the base currency: ")
to_currency = input("Enter the 3-letter code for the target currency: ")
duration = input("Enter the duration (e.g. '1 year' or '6 months'): ")

# Compute start and end dates based on duration
words = duration.split()
if len(words) != 2:
    print("Invalid duration format! Please specify a number followed by a time unit (year(s), month(s), or day(s)).")
    quit()
num, unit = words[0], words[1].lower()
if not num.isdigit():
    print("Invalid duration format! Please enter a valid number.")
    quit()
num = int(num)
current_date = requests.get('https://api.exchangeratesapi.io/latest', params={'app_id': app_id}).json()['date']
end_date = current_date
if unit == "year" or unit == "years":
    start_date = f"{int(current_date[:4])-num}-{current_date[5:]}"
elif unit == "month" or unit == "months":
    end_year, end_month, _ = list(map(int, current_date.split("-")))
    start_month = end_month - num
    start_year = end_year - start_month // 12
    start_month %= 12
    start_date = f"{start_year:04}-{start_month+1:02}-01"
else:
    start_date = f"{int(current_date[:8])-num*7}T00:00:00Z"

# Retrieve historical rates from Open Exchange Rates API
url = 'https://openexchangerates.org/api/time-series.json'
parameters = {
    'app_id': app_id,
    'start': start_date,
    'end': end_date,
    'base': from_currency,
    'symbols': to_currency
}
response = requests.get(url, params=parameters)
rates = response.json()['rates']

# Plot the exchange rates using Matplotlib
plt.plot(rates.keys(), rates.values())
plt.xlabel('Date')
plt.ylabel(f'{from_currency}/{to_currency} rate')
plt.title(f'{from_currency}/{to_currency} exchange rate over the last {num} {unit}(s)')
plt.show()