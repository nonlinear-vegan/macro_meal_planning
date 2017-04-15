#!/usr/bin/env python3
from termcolor import colored
import json
import utilities as ut

if __name__ == '__main__':
	print ("Daily macro goals:")
	print ("total protein: 163g")
	print ("total fats:     58g")
	print ("total carbs:   185g\n\n")
	print ("Protein in each snack: {0:>4.0f} g".format(163.0/6))
	print ("Fat in each meal:      {0:>4.0f} g".format(58.0/3))
	print ("Carbs in non-breakfast/non-workout:  {0:>4.0f} g".format((185-100)/3))
	print ("\n")
	## BREAKFAST
	print(colored("Breakfast:",'blue'))
	breakfast = ut.calc_macros(['westsoy_tofu','flax_oil','romain_lettuce','romain_lettuce'])
	ut.print_totals(breakfast,False)
	## MORNING SNACK
	print(colored("Morning Snack:","blue"))
	morning_snack = ut.calc_macros(['romain_lettuce','rolled_oats','performance_protein'])
	ut.print_totals(morning_snack,False)
	## LUNCH
	print(colored("Lunch:","blue"))
	lunch = ut.calc_macros(['canola_oil_t','rolled_oats','canola_oil_t','carrots_100','carrots_100','now_pea_protein_half'])
	ut.print_totals(lunch,False)
	## AFTERNOON SNACK (near workout time)
	print(colored("Afternoon snack:","blue"))
	afternoon_snack = ut.calc_macros(['vega_smoothie'])
	ut.print_totals(afternoon_snack,False)
	## DINNER
	print(colored("Dinner:","blue"))
	dinner = ut.calc_macros(['sweet_potato_100','sweet_potato_100','sweet_potato_100','flax_oil'])
	ut.print_totals(dinner,False)
	## DAY TOTALS
	day_total = ut.day_totals(breakfast,morning_snack,lunch,afternoon_snack,dinner)
	print (colored("Day totals: ","red"))
	ut.print_totals(day_total,True)

# 4 meals and 2 snacks
# same fraction of protein in each
# 50 g carbs before workout
# 50 g carbs after workout
# fats in morning or dinner, not near workout

