import os
import csv

#Pulling in the CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    budget_data = csv.reader(csvfile, delimiter=',')

    print(budget_data)

    csv_header = next(budget_data)
    # print(f"{csv_header}")

    #Storing the data into new lists
    dates = []
    profit_loss = []
    
    for row in budget_data:
        dates.append(row[0])
        profit_loss.append(float(row[1]))
    # print(dates)
    # print(profit_loss)

    #Combining the 2 seperate lists back together
    combined_list = dict(zip(dates, profit_loss))
    
    #Calculating the Total Months
    num_months = len(dates)
    # print(num_months)

    #Calculating the Total Profit
    total_prof = round(sum(profit_loss))
    # print(total_prof)

    #Calculating the Average Changes
    changes = []
    for x in range(1,len(profit_loss)):
        change = profit_loss[x] - profit_loss[x-1]
        changes.append(change) 

    avg_changes = round((sum(changes)/len(changes)),2)
    # print(avg_changes)

    #Calculating the Greatest Increase and Decrease
    maximum = round(max(changes))
    max_month = max(combined_list, key=combined_list.get)
    minimum = round(min(changes))
    min_month = min(combined_list, key=combined_list.get)

    # print(maximum)
    # print(minimum)

    #Printing the Final Results
    print("---------------------------")
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${total_prof}")
    print(f"Average Change: ${avg_changes}")
    print(f"Greatest Increase in Profits: {max_month} (${maximum})")
    print(f"Greatest Decrease in Profits: {min_month} (${minimum})")
    print("---------------------------")

#Text File Analysis
file = open('Analysis/PybankAnalysis.txt', 'w')
file.write("---------------------------")
file.write("\nFinancial Analysis")
file.write("\n---------------------------")
file.write(f"\nTotal Months: {num_months}")
file.write(f"\nTotal: ${total_prof}")
file.write(f"\nAverage Change: ${avg_changes}")
file.write(f"\nGreatest Increase in Profits: {max_month} (${maximum})")
file.write(f"\nGreatest Decrease in Profits: {min_month} (${minimum})")
file.write("\n---------------------------")
file.close

    

