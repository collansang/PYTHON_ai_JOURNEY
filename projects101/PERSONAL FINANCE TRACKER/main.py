import pandas as pd
import csv
from datetime import datetime
from data_entry import *
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT= "%d-%m-%Y"
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index = False)
        
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry= {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls. COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")
    
    @classmethod
    def get_transactions(cls, start_date,end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"]= pd.to_datetime(df["date"], format=cls.FORMAT)
        start_date= datetime.strptime(start_date,CSV.FORMAT)
        end_date= datetime.strptime(end_date,CSV.FORMAT)
        
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]#locates
        
        if filtered_df.empty:
            print("No transactions within the given date range")
            return pd.DataFrame()
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(
                filtered_df.to_string(
                index=False, formatters={"date":lambda x: x.strftime(CSV.FORMAT)}
                ))
            
            total_income = filtered_df[filtered_df["category"]=="income"]["amount"].sum()
            total_expense= filtered_df[filtered_df["category"]=="expense"]["amount"].sum()
            
            print(f"\n ----------------- SUMMARY ----------------- ")
            print(f"Total income: Ksh{total_income:.2f}")
            print(f"Total expense: Ksh{total_expense:.2f}")
            net = total_income - total_expense
            print(f"Net saving: Ksh{net:.2f}")
            return filtered_df
        

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of transaction dd-mm-yyyy or enter for default(today): ",allow_default=True)
    amount = get_amount()
    category= get_category()
    description=get_description()
    CSV.add_entry(date, amount,category,description)
    
  
def plot_transactions(df):
    if df is None or df.empty:
        print("No data available for plotting")
        return

    df = df.copy()
    df["category"] = df["category"].str.lower()
    df = df.set_index("date")

    income_df = df[df["category"] == "income"].resample("D")["amount"].sum()
    expense_df = df[df["category"] == "expense"].resample("D")["amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df, label="Income")
    plt.plot(expense_df.index, expense_df, label="Expense")

    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    
def main():
    while True:
        print("---------------------------------------------")
        print("\n1. Add new transaction")
        print("\n2. View Transaction and summary within a date range")
        print("\n3. Exit")
        print("---------------------------------------------")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add()
        elif choice =="2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if not df.empty and input("Do you want to see a plot?(y/n): ").lower()  =="y":
                plot_transactions(df)
            else:
                print("No data to plot")
            
        elif choice == "3":
            print("Exitting.......")
            break   
        
        else:
            print("Invalid choice. Enter 1,2,3: ")         

if __name__== "__main__":
    main()