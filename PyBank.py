# Import Data
import os
import csv
# Variables for the bank data analysis
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
# Set path for the file to be read
userhome = os.path.expanduser('~')
csvpath = userhome + '/Desktop/Python_PyBank_budget_data.csv'

# Open & Read PyBank CSV File
with open(csvpath, 'rU') as f:
    
    csvreader = csv.reader(f, delimiter = ',')
    
    csv_header = next(csvreader)
    row = next(csvreader)
   
    # Calculate Total Number Of Months, "Profit/Loss" & Variables For Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
   
    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        total_months += 1
        
        net_amount += int(row[1])
     
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
       
        # Calculate The Greatest Increase over the period
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
           
        # Calculate The Greatest Decrease over the period
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0] 
        
    # Calculate The Average change over the period
    average_change = sum(monthly_change)/ len(monthly_change)
   
    highest = max(monthly_change)
    lowest = min(monthly_change)
# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_amount}")
print(f"---------------------------")
print(f"Average Change: ${average_change:.2f}")
print(f"---------------------------")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, ${highest:.2f}")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, ${lowest:.2f}")