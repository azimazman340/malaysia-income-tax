import function 
import pandas as pd

def main():
    print("--- LHDN Tax Calculator System ---")
    
    ic = input("Enter 12-digit IC: ")
    password = input("Enter Password (last 4 digits of IC): ")
    
    if function.verify_user(ic, password):
        print("\nVerification Successful!")
        
        salary = float(input("Enter Annual Salary: "))
        bonus = float(input("Enter Annual Bonus: "))
       
        total_income = function.calculate_total(salary, bonus)
        relief = float(input("Enter Tax Relief: "))
        
        tax_due = function.calculate_tax(total_income, relief)
       
        print(f"Total Income: {function.format_rm(total_income)}")
        print(f"Tax Payable: {function.format_rm(tax_due)}")
        
        record = {
            "IC": ic,
            "Total_Income": total_income,
            "Tax_Paid": tax_due
        }
       
        function.save_record(record, "tax_records.csv")
        print("\nRecord successfully saved to tax_records.csv")
        
    else:
        print("\nError: IC or Password incorrect.")

if __name__ == "__main__":
    main()
