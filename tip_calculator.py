"""Calculate tip amount and total bill based on user input."""

# Common tip percentage options
VALID_TIP_PERCENTAGES = (15, 18, 20)


def main() -> None:
    # Get the bill amount from the user
    bill_amount = float(input("Enter the bill amount: $"))

    # Ask for tip percentage and validate the choice
    print(f"Choose a tip percentage: {', '.join(str(p) for p in VALID_TIP_PERCENTAGES)}")
    tip_percentage = int(input("Enter tip percentage: "))

    if tip_percentage not in VALID_TIP_PERCENTAGES:
        print(f"Invalid tip percentage. Please choose {', '.join(str(p) for p in VALID_TIP_PERCENTAGES)}.")
        return

    # Calculate tip and total (tip_percentage is converted to a decimal)
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount

    # Display the results
    print(f"\nBill amount:  ${bill_amount:.2f}")
    print(f"Tip ({tip_percentage}%):   ${tip_amount:.2f}")
    print(f"Total bill:   ${total_bill:.2f}")


if __name__ == "__main__":
    main()
