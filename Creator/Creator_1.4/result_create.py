import os

total_cases = int(input("Total test cases"))

for i in range(total_cases): # test case number
	os.system(f"./e2468726_the1 < ./cases/case{i}.txt > ./results/result{i}.txt")
