from random import choice
from random import choices
import os


def choose_coor_color():
	return str(choices([choice(range(25)), choice(range(-100,0)), choice(range(25,100))], [50, 25, 25])[0])

def choose_coor_pixel():
	return str(choice(range(25)))

colors = ["0","1","2","3","4","5","6","7"]
N = 25 # dimension

case_number = int(input("Case Number: "))

for file_no in range(case_number):
	lst_fill=[]
	with open(f"./cases/case{file_no}.txt", "w") as case:
		for _ in range(N):
			case.write(" ".join(choices(colors, k=N)))
			case.write("\n")

		case.write("F\n")
		color_coor = [choose_coor_color(), choose_coor_color()]
		pixel_coor = [choose_coor_pixel(), choose_coor_pixel()]			
		case.write(" ".join(color_coor))
		case.write("\n")
		case.write(" ".join(pixel_coor))
