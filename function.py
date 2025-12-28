import pandas as pd

def verify_user(ic_number, password):
   
    if not ic_number.isdigit() or len(ic_number) != 12:
        return False
   
    expected_password = ic_number[-4:]
    return password == expected_password

def calculate_tax(income, tax_relief):
   
    chargeable = max(0, income - tax_relief)
   
    if chargeable <= 5000:
        return 0
    elif chargeable <= 20000:
        return (chargeable - 5000) * 0.01
    elif chargeable <= 35000:
        return (15000 * 0.01) + (chargeable - 20000) * 0.03
    else:
        return (15000 * 0.01) + (15000 * 0.03) + (chargeable - 35000) * 0.06

def calculate_total(*args):
   
    sum_val = 0
    for arg in args:
        sum_val += arg
    return sum_val

format_rm = lambda x: f"RM {x:,.2f}"

def save_record(data_dict, filename):
  
    try:
   
        df = pd.read_csv(filename)
        df.loc[len(df)] = data_dict
    except FileNotFoundError:
        df = pd.DataFrame([data_dict])
    
    df.to_csv(filename, index=False)
