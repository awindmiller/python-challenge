import pandas as pd
import csv
import os
import numpy

filename = "HW3/Budget_Data.csv"

ReadFile = pd.read_csv("Budget_Data.csv")

TotalMonths  = ReadFile["Profit/Losses"].count()
TotalRevenueChange = 0
PrevRevenue = 0
RevIncrease = 0
SumMonths = ReadFile.groupby(['Profit/Losses']).sum()
Total = ReadFile["Profit/Losses"].sum()
PL= ReadFile["Profit/Losses"]
Max = ReadFile["Profit/Losses"].max()
Min = ReadFile["Profit/Losses"].min()
RevenuesList = []
ChangesList = []
i = 0 
for i in range(len(PL)):
	RevIncrease = int(PL[i]) - PrevRevenue
	ChangesList = RevenuesList.append(RevIncrease)
	#print(RevIncrease)
	TotalRevenueChange = TotalRevenueChange + RevIncrease
	PrevRevenue = int(PL[i])
	#RevenuesList = RevenuesList.insert(0, RevIncrease)


Average = TotalRevenueChange/TotalMonths
#print (TotalRevenueChange)
#print(RevIncrease)
#print(ChangesList)
#print(Average)

#print (RevenuesList)

#print(TotalRevenueChange)


def content():
	print("Financial Analysis")
	print("----------------------------")
	print("Total Months: " + str(TotalMonths))
	print("Total: " + str(Total))
	print("Average Change: " + str(Average))
	print("Greatest increase in profits: " + str(Max))
	print("Greatest decrease in profits: " + str(Min))

	f = open("C:/Users/awind/Documents/DataHWs/HW3/PyBankTxt.txt", "w+")

	f.write("Financial Analysis\n")
	#f.write("\n")
	f.write("----------------------------")
	f.write("\n")
	f.write("Total Months: " + str(TotalMonths))
	f.write("\n")
	f.write("Total: " + str(Total))
	f.write("\n")
	f.write("Average Change: " + str(Average))
	f.write("\n")
	f.write("Greatest increase in profits: " + str(Max))
	f.write("\n")
	f.write("Greatest decrease in profits: " + str(Min))

	f.close()

content()

#for row in PL:
	#RevIncrease = int(row[1]) - PrevRevenue
	#TotalRevenueChange = TotalRevenueChange + RevIncrease
	#PrevRevenue = int(row[1])

#print(TotalRevenueChange)

#print(Total)
#print (SumMonths)




#print(SumMonths)

#MonthCount = sum(1 for row in ReadFile)

#print(MonthCount)
#for row in ReadFile:
#	Counter = Counter + 1
#print(Counter)

