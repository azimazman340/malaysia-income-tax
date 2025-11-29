from function import verify_user, calculate_tax, save_to_csv, read_from_csv

def get_valid_ic():
    """Prompts user for a valid 12-digit IC number."""
    while True:
        ic = input("Enter your IC number (12 digits): ").strip()

        if ic.isdigit() and len(ic) == 12:
            return ic
        else:
            print("Invalid IC! IC must be exactly 12 digits.")


def get_positive_number(prompt):
    """Prompts user for a positive number. Used for income & tax relief."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def main():
    print("=====================================")
    print("     MALAYSIAN TAX INPUT SYSTEM      ")
    print("=====================================")

    ic_number = get_valid_ic()
    password = input("Enter your password (last 4 digits of IC): ").strip()

    if not verify_user(ic_number, password):
        print("Login failed! Incorrect IC or password.")
        return

    print("Login successful!")

    income = get_positive_number("Enter your annual income (RM): ")
    tax_relief = get_positive_number("Enter your total tax relief (RM): ")

    try:
        tax_amount = calculate_tax(income, tax_relief)
    except ValueError as e:
        print("Error calculating tax: {e}")
        return

    print("-------------------------------------")
    print(f"Your tax payable is: RM {tax_amount:.2f}")
    print("-------------------------------------")

    record = {
        "IC_Number": ic_number,
        "Income": income,
        "Tax_Relief": tax_relief,
        "Tax_Payable": tax_amount
    }

    save_to_csv(record, "tax_data.csv")
    print("Your record has been successfully saved!")

    print("========== All Stored Records ==========")
    df = read_from_csv("tax_data.csv")

    if df is not None:
        print(df.to_string(index=False))
    else:
        print("No data found in CSV file.")

    print("Thank you for using the Malaysian Tax Input System!")


if __name__ == "__main__":
    main()