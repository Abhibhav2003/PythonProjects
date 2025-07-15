import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv" # class variable
    COLUMNS  = ['date','amount','category','description']
    FILE_PATH = f'FinanceTracker/{CSV_FILE}'
    @classmethod # This is a classmethod -> It has access to the class but not the instance of the class
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.FILE_PATH,index=False)
    
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.FILE_PATH,'a',newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print('''
              +------------------------------+
              |                              |
              |  Entry Added Successfully !! |
              |                              |
              +------------------------------+
              ''')
        

CSV.initialize_csv()
CSV.add_entry("15-07-25",1000,"Income","Salary")