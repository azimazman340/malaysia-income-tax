import pandas as pd


# -----------------------------------------------------------
# a) User Verification Function
# -----------------------------------------------------------
def verify_user(ic_number, password):
    
    if not ic_number.isdigit() or len(ic_number) != 12:
        return False

    expected_password = ic_number[-4:]

    return password == expected_password



# -----------------------------------------------------------
# b) Tax Calculation Function (Malaysia LHDN Brackets)
# -----------------------------------------------------------
def calculate_tax(income, tax_relief):

    if income < 0 or tax_relief < 0:
        raise ValueError("Income and tax relief must be positive values.")

    chargeable = max(0, income - tax_relief)

    tax = 0

    if chargeable <= 5000:
        tax = 0

    elif chargeable <= 20000:
        tax = (chargeable - 5000) * 0.01

    elif chargeable <= 35000:
        tax = (15000 * 0.01) + (chargeable - 20000) * 0.03

    elif chargeable <= 50000:
        tax = (15000 * 0.01) + (15000 * 0.03) + (chargeable - 35000) * 0.06

    elif chargeable <= 70000:
        tax = (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + (chargeable - 50000) * 0.11

    elif chargeable <= 100000:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 +
            20000 * 0.11 + (chargeable - 70000) * 0.19
        )

    elif chargeable <= 250000:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 +
            20000 * 0.11 + 30000 * 0.19 +
            (chargeable - 100000) * 0.25
        )

    elif chargeable <= 400000:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 + 20000 * 0.11 +
            30000 * 0.19 + 150000 * 0.25 +
            (chargeable - 250000) * 0.26
        )

    elif chargeable <= 600000:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 + 20000 * 0.11 +
            30000 * 0.19 + 150000 * 0.25 + 150000 * 0.26 +
            (chargeable - 400000) * 0.28
        )

    elif chargeable <= 1000000:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 +
            20000 * 0.11 + 30000 * 0.19 + 150000 * 0.25 + 150000 * 0.26 +
            200000 * 0.28 +
            (chargeable - 600000) * 0.30
        )

    elif chargeable <= 2000000:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 + 20000 * 0.11 +
            30000 * 0.19 + 150000 * 0.25 + 150000 * 0.26 +
            200000 * 0.28 + 400000 * 0.30 +
            (chargeable - 1000000) * 0.32
        )

    else:
        tax = (
            15000 * 0.01 + 15000 * 0.03 + 15000 * 0.06 + 20000 * 0.11 +
            30000 * 0.19 + 150000 * 0.25 + 150000 * 0.26 +
            200000 * 0.28 + 400000 * 0.30 + 1000000 * 0.32 +
            (chargeable - 2000000) * 0.33
        )

    return tax



# -----------------------------------------------------------
# c) Save Data to CSV File
# -----------------------------------------------------------
def save_to_csv(data, filename):
   
    try:
        df = pd.read_csv(filename)
        df.loc[len(df)] = data  
    except FileNotFoundError:
        df = pd.DataFrame([data])
    except Exception as e:
        print("Error while saving data:", e)
        return

    df.to_csv(filename, index=False)



# -----------------------------------------------------------
# d) Read Data from CSV File
# -----------------------------------------------------------
def read_from_csv(filename):
   
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("CSV file not found.")
        return None
    except Exception as e:
        print("Error reading CSV:", e)
        return None