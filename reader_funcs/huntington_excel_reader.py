import openpyxl
import csv
path_to_huntington_statements = '/Users/ryantiller/personal-finance-project/huntington_statements'

def huntington_reader(file_name):
   ## return a list of list with 0 index the price and the 1 index the location
    target_file = path_to_huntington_statements + '/' + file_name
    with open(target_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        transactions_col = [] 
        data = []
        price_col= [] 
        for row in reader:
            if row[4].startswith('-') and not row[2] == 'M1 Card*DESERVE PAYMENT':
                stripped = row[3].replace('-','')
                data.append([stripped,row[1]])
        print(len(data))
        return data

