import os
import csv

csvpath = os.path.join ('PyBank_budget_data.csv')

total_months = 0
total_profit = 0
date = []
monthly_profit_change = 0
previous_profit = 0
list_of_delta_profits = []
total_delta = 0


with open(csvpath, "r") as csvfile:

    reader = csv.reader(csvfile, delimiter = ',')
    header_row = next(reader)



    for row in reader:
        total_months += 1
        #change in profit
        delta_profit =  int(row[1]) - previous_profit
  
        list_of_delta_profits.append(delta_profit)
        monthly_profit_change += delta_profit
        previous_profit = int(row[1])
        total_profit = total_profit + int(row[1])


for delta in list_of_delta_profits[1:]:
    total_delta += delta

#average
average_profit = total_delta/(total_months -1)

#Greatest increase in profits
increase = max(list_of_delta_profits)
#Greatest decease in profits
decrease = min(list_of_delta_profits)

print('Financial Analysis')
print('--------------------------------')
print('Total Months: ' + str(total_months))
print('Total Profit: ' + str(total_profit))
print('Average Change:' + str(round(average_profit, 2)))
print('Greatest Increase in profits:'+ str(increase))
print('Greatest Decrease in profits:'+ str(decrease))


with open('Financial_Analysis.txt', 'w') as text:
    text.write('Financial Analysis' + '\n')
    text.write('--------------------------------' + '\n')
    text.write('Total Months: ' + str(total_months) + '\n')
    text.write('Total Profit: ' + str(total_profit) + '\n')
    text.write('Average Change: ' + str(round(average_profit, 2)) + '\n')
    text.write('Greatest Increase in profits: ' + str(increase) + '\n')
    text.write('Greatest Decrease in profits: ' + str(decrease) + '\n')
    