from tkinter import *
import ttkbootstrap as ttk

from logic import insertDeposit
from logic import insertCharge
from logic import getBalance


root = ttk.Window(themename="superhero")
root.title("Budget App")
root.geometry("500x700")


def updateBalanceLabel():
    lblBalance.config(text=f"Your current balance is: ${getBalance():.2f}")


def depositMoney():
    amount = deposit.get()

    insertDeposit(amount)

    # Add deposit to the treeview
    tree.insert("", END, values=(amount, "Deposit"))

    deposit.delete(0, END)
    updateBalanceLabel()


def chargeMoney():
    amount = charge.get()
    description = chargeEntry.get()

    insertCharge(amount, description)

    tree.insert("", END, values=(amount, description))

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
lblDeposit = ttk.Label(
    root,
    text="Enter your deposit amount:"
)
lblDeposit.place(x=25, y=100)

deposit = ttk.Entry(root, width=15)
deposit.place(x=200, y=100)

btnDeposit = ttk.Button(
    root,
    text="Deposit",
    command=depositMoney
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
    command=chargeMoney
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


# -------------------------
# Treeview frame
# -------------------------
treeFrame = ttk.Frame(
    root,
    width=400,
    height=200,
    relief=RIDGE
)
treeFrame.place(x=50, y=350)

# Keeps the frame size from shrinking
treeFrame.pack_propagate(False)


# -------------------------
# Treeview widget
# -------------------------
tree = ttk.Treeview(
    treeFrame,
    columns=("Amount", "Description"),
    show="headings",
    height=8
)

tree.heading("Amount", text="Amount")
tree.heading("Description", text="Description")

tree.column("Amount", width=120, anchor=CENTER)
tree.column("Description", width=260, anchor=W)

tree.pack(fill=BOTH, expand=True)


root.mainloop()