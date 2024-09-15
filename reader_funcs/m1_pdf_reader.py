from PyPDF2 import PdfReader
import re
import pandas as pd

def m1_transactions(file_name):
    reader = PdfReader(f"m1-statements/{file_name}")
    num_pages = len(reader.pages)
    text = ''
    for i in range(2,num_pages):
        page = reader.pages[i]
        text = text + page.extract_text()
    line_split = text.splitlines()
    ## find transcations 
    transaction_date = []
    for i in range(0, len(line_split)):
        if line_split[i] == "TRANSACTION\tDATE":
            transaction_date.append(i)
    #find last payment key word
    payments = []
    for i in range(0, len(line_split)):
        if "Payments" in line_split[i]: 
            payments.append(i)

    len_text = len(text)
    # strip escape characters
    processed_text = []
    text_holder = ''
    for i in range(0,len(line_split)):
        text_holder = line_split[i].replace('\t', " ")
        text_with_no_n_t = text_holder.replace('\n', " ") 
        processed_text.append(text_holder)
        text_holder = ''

    last_payment = len(payments)
    transaction_range = [transaction_date[0], payments[last_payment-1]]
    white_count = 0
    char_count = 0
    new_words = []
    new_string = ''
    transactions_price_location = []
    for i in range(0,len(processed_text)):
        if processed_text[i].startswith('$'):
            transactions_price_location.append([processed_text[i],processed_text[i+2]])
    return transactions_price_location






