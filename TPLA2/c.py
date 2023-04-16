import tkinter as tk
from tkinter import ttk
import requests



def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    return rates

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    exchange_rate = exchange_rates[from_currency] / exchange_rates[to_currency]
    converted_amount = amount / exchange_rate
    result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

exchange_rates = get_exchange_rates()

root = tk.Tk()
root.title("Currency Converter")

mainframe = ttk.Frame(root, padding="30 15")
mainframe.grid()

from_currency_var = tk.StringVar()
from_currency_var.set("USD")
to_currency_var = tk.StringVar()
to_currency_var.set("EUR")

amount_entry = ttk.Entry(mainframe, width=10)
amount_entry.grid(column=1, row=1)

from_currency_dropdown = ttk.Combobox(mainframe, textvariable=from_currency_var, state="readonly", values=list(exchange_rates.keys()))
from_currency_dropdown.grid(column=2, row=1)

to_currency_dropdown = ttk.Combobox(mainframe, textvariable=to_currency_var, state="readonly", values=list(exchange_rates.keys()))
to_currency_dropdown.grid(column=3, row=1)

result_var = tk.StringVar()
result_label = ttk.Label(mainframe, textvariable=result_var)
result_label.grid(column=1, row=2, columnspan=3)

convert_button = ttk.Button(mainframe, text="Convert", command=convert_currency)
convert_button.grid(column=2, row=3)

root.mainloop()

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    return rates

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    exchange_rate = exchange_rates[from_currency] / exchange_rates[to_currency]
    converted_amount = amount / exchange_rate
    result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

exchange_rates = get_exchange_rates()

root = tk.Tk()
root.title("Currency Converter")

mainframe = ttk.Frame(root, padding="30 15")
mainframe.grid()

from_currency_var = tk.StringVar()
from_currency_var.set("USD")
to_currency_var = tk.StringVar()
to_currency_var.set("EUR")

amount_entry = ttk.Entry(mainframe, width=10)
amount_entry.grid(column=1, row=1)

from_currency_dropdown = ttk.Combobox(mainframe, textvariable=from_currency_var, state="readonly", values=list(exchange_rates.keys()))
from_currency_dropdown.grid(column=2, row=1)

to_currency_dropdown = ttk.Combobox(mainframe, textvariable=to_currency_var, state="readonly", values=list(exchange_rates.keys()))
to_currency_dropdown.grid(column=3, row=1)

result_var = tk.StringVar()
result_label = ttk.Label(mainframe, textvariable=result_var)
result_label.grid(column=1, row=2, columnspan=3)

convert_button = ttk.Button(mainframe, text="Convert", command=convert_currency)
convert_button.grid(column=2, row=3)


root.mainloop()



   