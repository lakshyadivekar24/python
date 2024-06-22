import tkinter as tk
from tkinter import messagebox


class ATMSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ATM Simulator")
        self.geometry("400x300")

        self.balance = 1000  # Initial balance

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self, text="ATM Simulator", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        # Display Balance Button
        self.balance_button = tk.Button(self, text="Check Balance", command=self.check_balance)
        self.balance_button.pack(pady=5)

        # Deposit Frame
        self.deposit_frame = tk.Frame(self)
        self.deposit_frame.pack(pady=5)

        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount:")
        self.deposit_label.pack(side=tk.LEFT)

        self.deposit_entry = tk.Entry(self.deposit_frame)
        self.deposit_entry.pack(side=tk.LEFT)

        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side=tk.LEFT)

        # Withdraw Frame
        self.withdraw_frame = tk.Frame(self)
        self.withdraw_frame.pack(pady=5)

        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount:")
        self.withdraw_label.pack(side=tk.LEFT)

        self.withdraw_entry = tk.Entry(self.withdraw_frame)
        self.withdraw_entry.pack(side=tk.LEFT)

        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(side=tk.LEFT)

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit)
        self.exit_button.pack(pady=20)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount <= 0:
                raise ValueError("Invalid amount")
            self.balance += amount
            self.deposit_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"${amount} deposited successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount <= 0:
                raise ValueError("Invalid amount")
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance.")
            else:
                self.balance -= amount
                self.withdraw_entry.delete(0, tk.END)
                messagebox.showinfo("Success", f"${amount} withdrawn successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    app = ATMSimulator()
    app.mainloop()
