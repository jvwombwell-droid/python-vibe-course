"""Track multiple expenses and show a summary when done."""


def main() -> None:
    # Each expense is stored as a dictionary with amount and description
    expenses = []

    print("Personal Expense Tracker")
    print("Add expenses one at a time. Type 'done' when finished.\n")

    while True:
        user_input = input("Enter amount and description (or 'done'): ").strip()

        # Stop adding expenses when the user types "done"
        if user_input.lower() == "done":
            break

        # Split on the first space: amount, then the rest is the description
        parts = user_input.split(maxsplit=1)

        if len(parts) != 2:
            print("Please enter an amount and description, e.g. 12.50 Coffee")
            continue

        amount_text, description = parts

        # Make sure the amount is a valid number
        try:
            amount = float(amount_text)
        except ValueError:
            print("Invalid amount. Use a number like 12.50")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        # Add this expense to the list
        expenses.append({"amount": amount, "description": description})
        print(f"Added: ${amount:.2f} - {description}")

    # Show summary after the user finishes
    print("\n--- Expense Summary ---")

    if not expenses:
        print("No expenses recorded.")
        return

    # Calculate total spent and average expense
    total_spent = sum(expense["amount"] for expense in expenses)
    average_expense = total_spent / len(expenses)

    print(f"Total spent:     ${total_spent:.2f}")
    print(f"Average expense: ${average_expense:.2f}")
    print(f"Number of expenses: {len(expenses)}\n")

    print("Full list of expenses:")
    for index, expense in enumerate(expenses, start=1):
        amount = expense["amount"]
        description = expense["description"]
        print(f"  {index}. ${amount:.2f} - {description}")


if __name__ == "__main__":
    main()
