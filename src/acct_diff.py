""" Module Name: acct_diff
# 
# This code module takes 2 lists of transactions and lists the differences between 
# them. Should be run from a command prompt 
# >> python acct_diff.py f1 f2 
"""
import re
import sys
import os
import csv
import pathlib
import csv 
from datetime import datetime, timedelta



def Read_File(FileName):
   """Return a line of text from a file.
   Args:
      Filename: The filename that should be read
   Returns:
      The next line of text in the file, otherwise, 1
   """
   try:
      with open(FileName, 'r') as File:
         for Line in File:
            yield Line
   except:
      #Print an error if the file is invalid
      print ('The file ', FileName, ' does not exist')
      return 1


def is_Match(row1, row2):
   """Determines if 2 financial transactions match, for use in balancing personal
      accounting with bank records.
   Args:
      row1, row2: tuples of format [type, date, vendor, amount]
   Returns:
      True -> rows have the same amount and dates are within 4 days
      False -> Otherwise
   """
   if row1["amount"] == row2["amount"]:
       if row2["date"] >= (row1["date"] - timedelta(days=4)) and \
          row2["date"] <= (row1["date"] + timedelta(days=4)):
          return True
   else:
      return False        


def Print_to_File(line, out_file):
   """Appends a line of text to a file.
   Args:
      line: line of text to append to a file
      out_file: the file to add the line to
   Returns:
      None
   """
   with open(out_file,'a') as file:
      file.write(line)

   return 1       




def Main():
# Parse the command line arguments to get the filenames to be compared.
# Files should be csv files formatted as fields ['Type', 'Date', 'Vendor', 'Amount']
# **********************************************************************************  
   if len(sys.argv) == 3:  
      myAcct_file = sys.argv[1] 
      bank_file   = sys.argv[2]  
   # Display error and return if the input file name is not passed in.
   else:   
      print ('Proper usage:')
      print ('python acct_diff.py <filename1> <filename2>' )
      return 1

# Read in files to 2 tuple arrays 
   myAcct_Dict    = list()     
   bank_Dict      = list() 
   outfile = "diff_0527.txt" 


# Read in the file contents to dictionaries myAcct_Dict and bank_Dict
# **********************************************************************************  
   with open(myAcct_file, 'r') as csvnew:
      #fieldnames = ['type', 'date', 'vendor', 'amount']
      reader = csv.DictReader(csvnew)
      for row in reader:
        myAcct_Dict.append(row)

   with open(bank_file, 'r') as csvnew:
      #fieldnames = ['type', 'date', 'vendor', 'amount']
      reader = csv.DictReader(csvnew)
      for row in reader:
        bank_Dict.append(row)  
  
# Data Conversion (amount:strings => floats, date; strings => mm/dd/yyyy )
# **********************************************************************************
   for row in myAcct_Dict:
      row["matched"] = "no"
      row["amount"] = float(row["amount"])
      row["date"] = datetime.strptime(row["date"], "%m/%d/%Y").date()
      print(row["matched"], row['type'],row['vendor'], row['date'],  row['amount'])   
   for row in bank_Dict:
      row["matched"] = "no"
      row["amount"] = float(row["amount"])
      row["date"] = datetime.strptime(row["date"], "%m/%d/%Y").date()
      #print(row)    



# Cycle through all transactions in both accounts, whenever a matching transaction 
# is found, mark it and exit loop
# **********************************************************************************       
   for acctRow in myAcct_Dict:
      for bankRow in bank_Dict:
        if bankRow["matched"] == "no":
            if is_Match(acctRow, bankRow):
               bankRow["matched"] = "yes"
               break;
        
   for bankRow in bank_Dict:
      for acctRow in myAcct_Dict:
        if acctRow["matched"] == "no":
            if is_Match(acctRow, bankRow):
               acctRow["matched"] = "yes"
               break;  



# Print any unmatched entries
# **********************************************************************************   
   line = "\nUnmatched transaction, MyAcct\n" + \
          "********************************************\n"  
   Print_to_File(line, outfile) 
   for row in myAcct_Dict:
      if row["matched"] == "no":
         line = row['type'] + ", " + row['vendor'] + ", " + str(row['date']) + ", " + str(row['amount'])+ "\n"  
         Print_to_File(line, outfile) 
              
   line = "\nUnmatched transaction, Bank\n" + \
          "********************************************\n"  
   Print_to_File(line, outfile) 
   for row in bank_Dict:
      if row["matched"] == "no":
         line = row['type'] + ", " + row['vendor'] + ", " + str(row['date']) + ", " + str(row['amount']) + "\n"
         Print_to_File(line, outfile)   


   
if __name__ == "__main__":
   Main()
