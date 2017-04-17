#!/usr/bin/env python3
from termcolor import colored
import json
import sys
sys.path.append("../")
import utilities as ut

if __name__ == '__main__':
	today = sys.argv[0][2:-3]
	f = open('plan_'+today+".txt",'w')
	f.write ('\nFOOD FOR: ' + today+"\n")
	carbs,prot,fat = ut.macro_cals()
	carbs_per_day = 185.0
	prot_per_day  = 163.0
	fat_per_day   = 58.0
	cal_per_day = carbs*carbs_per_day + prot*prot_per_day + fat*fat_per_day
	print (colored("\n\nDaily macro goals:","red"))
	print ("total protein: " , prot_per_day)
	print ("total fats:    " , fat_per_day)
	print ("total carbs:   " , carbs_per_day )
	print ("calories per day: " , cal_per_day)
	print ("Protein in each snack: {0:>4.0f} g".format(prot_per_day/6))
	print ("Fat in each meal:      {0:>4.0f} g".format(fat_per_day/3))
	print ("Carbs in non-breakfast/non-workout:  {0:>4.0f} g".format((carbs_per_day)/3))
	print ("\n")
	print(colored("Day 2 of backpack","red"))
	f.write("Day 2 of backpack\n")
	## BREAKFAST
	print(colored("Breakfast:",'blue'))
	breakfast = ut.calc_macros(['rolled_oats','performance_protein'],'BREAKFAST',f)
	ut.print_totals(breakfast,False,f,'BREAKFAST')
	## MORNING SNACK
	print(colored("Morning Snack:","blue"))
	morning_snack = ut.calc_macros(['performance_protein'],'MORNING SNACK',f)
	ut.print_totals(morning_snack,False,f,'MORNING SNACK')
	## LUNCH
	print(colored("Lunch:","blue"))
	lunch = ut.calc_macros(['almonds','cranberries','minute_rice','now_pea_protein'],'LUNCH',f)
	ut.print_totals(lunch,False,f,'LUNCH')
	## AFTERNOON SNACK (near workout time)
	print(colored("Afternoon snack:","blue"))
	afternoon_snack = ut.calc_macros(['flake_coconut_half','cranberries'],'AFTERNOON SNACK',f)
	ut.print_totals(afternoon_snack,False,f,'AFTERNOON SNACK')
	## DINNER
	print(colored("Dinner:","blue"))
	dinner = ut.calc_macros(['minute_rice','now_pea_protein','performance_protein','flake_coconut_half'],'DINNER',f)
	ut.print_totals(dinner,False,f,'DINNER')
	## DAY TOTALS
	day_total,dt_calories = ut.day_totals(breakfast,morning_snack,lunch,afternoon_snack,dinner)
	print (colored("Day totals: ","red"))
	f.write("\n\nDAY TOTALS\n")
	ut.print_totals(day_total,True,f,'DAY TOTAL')
	print ("Calories for the day: ", dt_calories)
	f.close()
