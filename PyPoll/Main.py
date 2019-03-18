import pandas as pd
import csv
import os
import numpy

ReadFile = pd.read_csv("election_data.csv")

TotalVotes = ReadFile["Voter ID"].count()
Khan = 0
Correy = 0 
Li = 0
OTooley = 0

f = open("C:/Users/awind/Documents/DataHWs/HW3/PyPollTxt.txt", "w+")

for row in ReadFile["Candidate"]:
	if row == "Khan":
		Khan = Khan + 1
	elif row == "Correy":
		Correy = Correy + 1
	elif row == "Li":
		Li = Li + 1
	else:
		OTooley = OTooley + 1


KhanPercent = (Khan / TotalVotes)*100
CorreyPercent = (Correy / TotalVotes)*100
LiPercent = (Li / TotalVotes)*100
OTooleyPercent = (OTooley / TotalVotes)*100
print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(TotalVotes))
print("-------------------------")
print("Khan: " + str(int(KhanPercent)) + "% " + str(Khan) + " Votes")
print("Correy: " + str(int(CorreyPercent))+"% " + str(Correy) + " Votes")
print ("Li: " + str(int(LiPercent))+"% " + str(Li) + " Votes")
print("O'Tooley: " +str(int(OTooleyPercent)) + "% " + str(OTooley) + " Votes")
print("-------------------------")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: "+ str(TotalVotes)+ "\n")
f.write("-------------------------\n")
f.write("Khan: " + str(int(KhanPercent)) + "% " + str(Khan) + " Votes\n")
f.write("Correy: " + str(int(CorreyPercent))+"% " + str(Correy) + " Votes\n")
f.write("Li: " + str(int(LiPercent))+"% " + str(Li) + " Votes\n")
f.write("O'Tooley: " +str(int(OTooleyPercent)) + "% " + str(OTooley) + " Votes\n")
CandidateList = [KhanPercent, CorreyPercent , LiPercent, OTooleyPercent]
if max(CandidateList) == KhanPercent:
	print("Winner: Khan")
	f.write("Winner: Khan\n")
elif max(CandidateList) == CorreyPercent:
	print("Winner: Correy")
	f.write("Winner: Correy\n")
elif max(CandidateList) == LiPercent:
	print("Winner: Li")
	f.write("Winner: Li\n")
elif max(CandidateList) == OTooleyPercent:
	print("Winner: O'Tooley")
	f.write("Winner: O'Tooley\n")
print("-------------------------")
f.write("-------------------------\n")



# f.write("Election Results\n")
# f.write("-------------------------\n")
# f.write("Total Votes: "+ str(TotalVotes)+ "\n")
# f.write("-------------------------\n")
# f.write("Khan: " + str(int(KhanPercent)) + "% " + str(Khan) + " Votes\n")
# f.write("Correy: " + str(int(CorreyPercent))+"% " + str(Correy) + " Votes\n")
# f.write("Li: " + str(int(LiPercent))+"% " + str(Li) + " Votes\n")
# f.write("O'Tooley: " +str(int(OTooleyPercent)) + "% " + str(OTooley) + " Votes\n")


f.close()
