'''
Tasks for this script:
-1 The total number of months included in the dataset
-2 The net total amount of "Profit/Losses" over the entire period
-3 The changes in "Profit/Losses" over the entire period, and then the average of those changes
-4 The greatest increase in profits (date and amount) over the entire period
-5 The greatest decrease in profits (date and amount) over the entire period
''' 

import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

#lists to store months and financial data
header = []
months = []
profit_loss = []
diff_pl = []

#declare variables
net_total = 0
net_diff = 0
diff_total = 0
avg_diff = 0
month_count = 0
average = 0

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    header = next(csvreader)
    #print(header) #test for header output

    for row in csvreader:  
        # add month entry to end of list, from first column of csv file
        months.append(row[0])
        # Add profit/loss entry to end of list, from second column of csv file
        profit_loss.append(int(row[1]))

    #Task 1, count number of months in months list
    month_count = len(months)

    #Task 2, calculate net total of profit/losses
    #sum all entries in profit_loss list
    for x in profit_loss:
        net_total += x
    
    #Task 3, calculate total change and then the average change in profit/losses
    #start at second entry [1] in list because there is nothing to subtract for the first month [0]
    #Task 4 & 5, list recording each calculated 'net_diff' in 'diff_pl' list
    for x in profit_loss[1: : ]:
        net_diff = x - profit_loss[profit_loss.index(x) - 1]
        diff_pl.append(net_diff) 
        diff_total += net_diff

    #Task 3 - continued: calculate average change, month_count -1 to account for first month not having a change
    avg_diff = diff_total / ((month_count)-1)

print('Financial Analysis')
print('--------------------------------------------')
print(f'Total Months: {month_count}')
print(f'Total Profit/Loss: ${net_total}')
print(f'Average Change: ${avg_diff:.2f}')
#Task 4 & 5 - continued: use index max/min value that corresponsd with correct month, index is shifted by 1 to account for previous loop starting at [1] since first month has no change
print(f'Greatest Increase in Profits: {months[diff_pl.index(max(diff_pl))+1]} (${max(diff_pl)})')
print(f'Greatest Decrease in Profits: {months[diff_pl.index(min(diff_pl))+1]} (${min(diff_pl)})')


#output results to target file
output_file = os.path.join("Analysis", "budget_analysis.txt")

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)

    # Write results to each row in text file, []'s is used to write each line as a continue string
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------------------------------"])
    writer.writerow([f'Total Months: {month_count}'])
    writer.writerow([f'Total Profit/Loss: ${net_total}'])
    writer.writerow([f'Average Change: ${avg_diff:.2f}'])
    writer.writerow([f'Greatest Increase in Profits: {months[diff_pl.index(max(diff_pl))+1]} (${max(diff_pl)})'])
    writer.writerow([f'Greatest Decrease in Profits: {months[diff_pl.index(min(diff_pl))+1]} (${min(diff_pl)})'])