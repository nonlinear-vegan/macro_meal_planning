#!/usr/bin/env python3
from termcolor import colored
import json
import sys
sys.path.append("../")
import utilities as ut

if __name__ == '__main__':
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
	print(colored("Day Hiking in Big Bend","red"))
	## BREAKFAST
	print(colored("Breakfast:",'blue'))
	breakfast = ut.calc_macros(['romain_lettuce','flax_oil','westsoy_tofu'])
	ut.print_totals(breakfast,False)
	## MORNING SNACK
	print(colored("Morning Snack:","blue"))
	morning_snack = ut.calc_macros(['performance_protein'])
	ut.print_totals(morning_snack,False)
	## LUNCH
	print(colored("Lunch:","blue"))
	lunch = ut.calc_macros(['carrots_100','flax_oil','brown_rice_dry','now_pea_protein','romain_lettuce','carrots_100'])
	ut.print_totals(lunch,False)
	## AFTERNOON SNACK (near workout time)
	print(colored("Afternoon snack:","blue"))
	afternoon_snack = ut.calc_macros(['brown_rice_dry','flake_coconut'])
	ut.print_totals(afternoon_snack,False)
	## DINNER
	print(colored("Dinner:","blue"))
	dinner = ut.calc_macros(['minute_rice','now_pea_protein','performance_protein'])
	ut.print_totals(dinner,False)
	## DAY TOTALS
	day_total,dt_calories = ut.day_totals(breakfast,morning_snack,lunch,afternoon_snack,dinner)
	print (colored("Day totals: ","red"))
	ut.print_totals(day_total,True)
	print ("Calories for the day: ", dt_calories)
	
