""" Module Name: update_json
# 
# https://www.kdnuggets.com/10-python-one-liners-for-json-parsing-and-processing
# This code module takes a Banking account as an input and allows you to add a transaction 
# to it. Should be run from a command prompt 
# >> python update_json.py f1 
"""
import json
import sys
# import re
# import os
# import csv
# import pathlib
# from datetime import datetime, timedelta

file_path = "utilities/my_acct.json"
output_path = "../test/test_output.json"

new_transaction = { "type": "credit",
                    "Date": "08/07/2026", 
                    "Vendor": "InSight Global",
                     "Amount": "1,911.94"
                  }



with open(file_path, 'r+', encoding='utf-8') as json_file:
    bank_acct = json.load(json_file)


    # get_balances
    print(bank_acct['institution']['routing_number'])

    # \d{1,3}(,\d{3})
    for item in bank_acct['transactions']:
        print(item['Amount'])
        item['Amount'] = float(item['Amount'])


    balance = 0
    purchases = 0
    deposits = 0

    for item in bank_acct['transactions']:
        print(item['Type'])
        if item['Type'] == "credit":
            deposits += item["Amount"]
        if item['Type'] == "debit":
            purchases += item["Amount"]

    balance = deposits - purchases    
    print(f"Balance is {balance} \nDeposits are {deposits} and Purchases are {purchases}")


    # bank_acct["transactions"].append(new_transaction)

    # place the cursor at the beginning of the file
    json_file.seek(0)

    json.dump(bank_acct, json_file,indent=0)
    json_file.truncate()

    print('JSON file updated successfully')