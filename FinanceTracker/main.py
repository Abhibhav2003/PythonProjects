import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv" # class variable
    
    @classmethod # This is a classmethod -> It has access to the class but not the instance of the class
    def initialize_csv(cls):
        try:
            pd.