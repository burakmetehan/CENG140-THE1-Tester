import os

case_number = int(input("Case Number: "))

for i in range(case_number): # test case number
	os.system(f"./e2468726_the1 < ./cases/case{i}.txt > ./results/result{i}.txt")