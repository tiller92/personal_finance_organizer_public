from reader_funcs import * 

import os 
import time
from datetime import datetime
import sys

try:
    file_name = sys.argv[1]
except:
    print("Please list the name of the file")
    sys.exit("Stopping the program")


def get_m1_data():
    now = datetime.now()
    curr_month = str(now.month -1) + '-' + str(now.year) + '.pdf' 
    new_excel_name = str(now.month -1) + '-' + str(now.year) + '.xlxs' 
    m1_folder_path = '/Users/ryantiller/personal-finance-project/m1-statements'
    files = os.listdir(m1_folder_path)
    for i in range(0, len(files)):
        if curr_month == files[i]:
            data = m1_transactions(files[i])
            categorized_data = cate_transactions(data)
            data_insert_monthly_spend(categorized_data ,new_excel_name)    

get_m1_data()


# huntington data 






# pay stub data







# retitment dat
