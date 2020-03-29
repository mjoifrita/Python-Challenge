#import os and csv modules
import os
import csv

#create path for csv file
py_bank = os.path.join('Resources/budget_data.csv')

#open csv dataset with reader
with open(py_bank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')   
    for row in csvreader:
        print(row)

#show header row only
print(f'{csv_header}')

#set variables - integers and strings
total_months = []
profit_loss = []
diff = []
total_chng_profit = [] 
date = []
greatest_increase = ""
greatest_decrease = ""

#open csv dataset with reader
with open(py_bank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(int(row[1]))

#display total number of months
len(total_months)

#display profit_loss total
sum(profit_loss)