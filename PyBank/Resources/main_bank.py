import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

#For net profit/losses. I put the profit/loss data in a list because it was easier for me.
csvlists = []
the_months = []
total_prof = 0
total_loss = 0
totalmonths = 0
totalprofit_loss = 0

#For average
monthcount = 0
lastmonth = 0
currentmonth = 0
change = 0
averagelists = []
average = 0 

#For increase decrease
greatestincrease = 0
greatestdecrease = 0

print("Financial Analysis")
print("--------------------")
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        csvlists.append(row[1])
        the_months.append(row[0])
        totalmonths += 1
    print("Total Months: " + str(totalmonths))

    #Net profit/loss formula
    for csvlist in csvlists:
        if int(csvlist) > 0:
            total_prof = total_prof + int(csvlist)
        elif int(csvlist) < 0:
            total_loss = total_loss + int(csvlist)
    totalprofit_loss = total_prof + total_loss
    print("Total: $" + str(totalprofit_loss))

    #Average formula
    for csvlist in csvlists:
        monthcount += 1
        if monthcount == 1:
            lastmonth = csvlist
        elif monthcount == 2:
            currentmonth = csvlist
            change = int(currentmonth) - int(lastmonth)
            averagelists.append(change)
            lastmonth = csvlist
            monthcount = 1
    total = sum(averagelists)
    number_of = len(averagelists)
    average = round(total / number_of, 2)
    print("Average Change: $" + str(average))

    #Increase and Decrease
    for csvlist in csvlists:
        if int(csvlist) > greatestincrease:
            greatestincrease = int(csvlist)
        elif int(csvlist) < greatestdecrease:
            greatestdecrease = int(csvlist)
    print("Greatest Increase in profits: " + str(greatestincrease))
    print("Greatest Decrease in profits: " + str(greatestdecrease))

the_path = '/Users/tylerbrown/Documents/Data Science bootcamp/Homework 3/PyBank/Analysis/bank.txt'
with open(the_path, "x") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------")
    file.write("\n")
    file.write("Total Months: " + str(totalmonths))
    file.write("\n")
    file.write("Total: $" + str(totalprofit_loss))
    file.write("\n")
    file.write("Average Change: $" + str(average))
    file.write("\n")
    file.write("Greatest Increase in profits: " + str(greatestincrease))
    file.write("\n")
    file.write("Greatest Decrease in profits: " + str(greatestdecrease))
    




