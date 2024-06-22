import tkinter as tk
from tkinter import ttk

conversion_rates = {
    "USD": {"EUR": 0.91, "GBP": 0.76, "INR": 82.47},
    "EUR": {"USD": 1.10, "GBP": 0.83, "INR": 90.87},
    "GBP": {"USD": 1.31, "EUR": 1.20, "INR": 109.67},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0091}
}

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.geometry("400x300")

        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        #Inputs
        ttk.Label(self, text="From Currency:").grid(column=0, row=0, padx=10, pady=10, sticky='W')
        self.from_currency = ttk.Combobox(self, textvariable=self.from_currency_var)
        self.from_currency['values'] = list(conversion_rates.keys())
        self.from_currency.grid(column=1, row=0, padx=10, pady=10, sticky='E')

        ttk.Label(self, text="To Currency:").grid(column=0, row=1, padx=10, pady=10, sticky='W')
        self.to_currency = ttk.Combobox(self, textvariable=self.to_currency_var)
        self.to_currency['values'] = list(conversion_rates.keys())
        self.to_currency.grid(column=1, row=1, padx=10, pady=10, sticky='E')

        ttk.Label(self, text="Amount:").grid(column=0, row=2, padx=10, pady=10, sticky='W')
        self.amount_entry = ttk.Entry(self, textvariable=self.amount_var)
        self.amount_entry.grid(column=1, row=2, padx=10, pady=10, sticky='E')

        # Convert Button
        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        # Result
        result_frame = ttk.Frame(self, borderwidth=2, relief="groove", padding="10", style="ResultFrame.TFrame")
        result_frame.grid(column=0, row=4, columnspan=2, padx=10, pady=10, sticky='EW')

        # Result Label
        self.result_label = ttk.Label(result_frame, textvariable=self.result_var, font=("Helvetica", 14, "bold"),
                                      foreground="white", background="#007ACC")
        self.result_label.pack(expand=True)

        # Configure styles
        style = ttk.Style()
        style.configure("ResultFrame.TFrame", background="#007ACC")

    def convert_currency(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_var.get())

        if from_currency and to_currency and amount:
            if from_currency == to_currency:
                converted_amount = amount
            else:
                converted_amount = amount * conversion_rates[from_currency][to_currency]

            self.result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            self.result_var.set("Invalid input. Please enter valid data.")


if __name__ == "__main__":
    app = CurrencyConverter()
    app.mainloop()
