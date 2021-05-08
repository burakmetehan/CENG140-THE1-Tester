import os

number_of_fill = int(input("Number of F Operation Cases: "))
number_of_paste = int(input("Number of P Operation Cases: "))
number_of_rotate = int(input("Number of R Operation Cases: "))

f_1 = open("temp_fill", "w")
f_1.write(f"{number_of_fill}")
f_2 = open("temp_paste", "w")
f_2.write(f"{number_of_fill} \n{number_of_paste+number_of_fill}")
f_3 = open("temp_rotate", "w")
f_3.write(f"{number_of_paste+number_of_fill} \n{number_of_rotate+number_of_paste+number_of_fill}")

f_1.close()
f_2.close()
f_3.close()

os.system("python3 case_gen_fill.py < temp_fill > temp_output")
os.system("python3 case_gen_paste.py < temp_paste > temp_output")
os.system("python3 case_gen_rotate.py < temp_rotate > temp_output")

# Result Creating
for i in range(number_of_fill+number_of_paste+number_of_rotate):
	os.system(f"./e2468726_the1 < ./cases/case{i}.txt > ./results/result{i}.txt")

os.system("rm -f temp_fill temp_paste temp_rotate temp_output")
