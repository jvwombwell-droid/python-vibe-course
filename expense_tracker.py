"""Track multiple expenses and show a summary when done."""

expenses = []

print("Add expenses (amount + description). Type 'done' when finished.\n")

while True:
    user_input = input("Enter amount and description (or 'done'): ").strip()

    if user_input.lower() == "done":
        break

    # Split on the first space: amount, then the rest is the description
    parts = user_input.split(maxsplit=1)

    if len(parts) != 2:
        print("Please enter an amount and description, e.g. 12.50 Coffee")
        continue

    amount_text, description = parts

    try:
        amount = float(amount_text)
    except ValueError:
        print("Invalid amount. Use a number like 12.50")
        continue

    expenses.append({"amount": amount, "description": description})
    print(f"Added: ${amount:.2f} - {description}")

# Show summary
print("\n--- Expense Summary ---")

if not expenses:
    print("No expenses recorded.")
else:
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total: ${total:.2f}\n")
    print("All expenses:")
    for expense in expenses:
        print(f"  ${expense['amount']:.2f} - {expense['description']}")
