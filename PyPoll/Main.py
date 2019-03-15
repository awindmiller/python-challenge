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
for row in PL:
	RevIncrease = int(PL[0]) - PrevRevenue
	TotalRevenueChange = TotalRevenueChange + RevIncrease
	PrevRevenue = int(PL[0])
	#RevenuesList = RevenuesList.insert(0, RevIncrease)

Average = TotalRevenueChange/TotalMonths
#print (TotalRevenueChange)
#print(RevIncrease)
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

