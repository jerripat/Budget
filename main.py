from tkinter import *
import ttkbootstrap as ttk
from logic import insertDeposit
from logic import insertCharge
from logic import getBalance

root = ttk.Window(themename="superhero")
root.title("Budget App")
root.geometry("500x500")

def updateBalanceLabel():
    lblBalance.config(text=f"Your current balance is: ${getBalance():.2f}")


def depositMoney():
    insertDeposit(deposit.get())
    deposit.delete(0, END)
    updateBalanceLabel()

def chargeMoney():
    insertCharge(charge.get(), chargeEntry.get())
    charge.delete(0, END)
    chargeEntry.delete(0, END)
    updateBalanceLabel()





lblMain = ttk.Label(
    root,
    text="Welcome to Budget App",
    font=("Arial", 20)
)
lblMain.place(x=120, y=25)

# -------------------------
# Deposit row
# -------------------------
lbldeposit = ttk.Label(
    root,
    text="Enter your deposit amount:"
)
lbldeposit.place(x=25, y=100)

deposit = ttk.Entry(root, width=15)
deposit.place(x=200, y=100)

btnDeposit = ttk.Button(
    root,
    text="Deposit",
    command=lambda: depositMoney()

)
btnDeposit.place(x=350, y=95)

# -------------------------
# Charge amount row
# -------------------------
lblCharge = ttk.Label(
    root,
    text="Enter your charge amount:"
)
lblCharge.place(x=25, y=160)

charge = ttk.Entry(root, width=15)
charge.place(x=200, y=160)

# -------------------------
# Charge description row
# -------------------------
lblDescription = ttk.Label(
    root,
    text="Enter charge description:"
)
lblDescription.place(x=25, y=220)

chargeEntry = ttk.Entry(root, width=15)
chargeEntry.place(x=200, y=220)

btnCharge = ttk.Button(
    root,
    text="Charge",
    command=lambda: chargeMoney()
)
btnCharge.place(x=350, y=215)

# -------------------------
# Balance row
# -------------------------
lblBalance = ttk.Label(
    root,
    text=f"Your current balance is: ${getBalance():.2f}"
)
lblBalance.place(x=150, y=300)

root.mainloop()
