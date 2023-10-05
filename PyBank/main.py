import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

revenue = []
with open(budget_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        revenue.append(float(row["Profit/Losses"]))

    

with open("analysis/PyBank.txt", "a") as f: 
    print("Financial Analysis",file=f)
    print("----------------------------",file=f)
    print("Total Months: ", len(revenue),file=f)
    print("Total:  $", sum(revenue),file=f)
    print("Average change: ", sum(revenue) / len(revenue),file=f)
    print("Greatest Increase in Profits: ", max(revenue),file=f)
    print("Greatest Decrease in Profits: ", min(revenue),file=f)