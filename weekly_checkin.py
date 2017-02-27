#!/usr/bin/env python3
from termcolor import colored
import json

def print_totals(dish_totals,day):
	"""Pretty-ish print the fat/carbs/protein from input. If day=True, print the goals for the day"""
	if day:
		print ("fat:    {0:>4.0f} (daily goal:  58)".format(dish_totals['fat']))
		print ("carbs:  {0:>4.0f} (daily goal: 185)".format(dish_totals["carbs"]))
		print ("prot:   {0:>4.0f} (daily goal: 163)".format(dish_totals["prot"]))
	else:
		print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
		print ("carbs:  {0:>4.0f}".format(dish_totals["carbs"]))
		print ("prot:   {0:>4.0f}".format(dish_totals["prot"]))

def day_mark(day):
	goals ={'prot':163,'carbs':185,'fat':58}
	

if __name__ == '__main__':
	#print ("Daily macro goals:")
	#print ("total protein: 163g")
	#print ("total fats:     58g")
	#print ("total carbs:   185g\n\n")
	#print ("\n")
	goals ={'prot':163,'carbs':185,'fat':58}
	dates = ["2017-02-20","2017-02-21","2017-02-22","2017-02-23","2017-02-24","2017-02-25"]
	file_name = "Exports/Nutrition-Summary-2017-02-19-to-2017-02-26.csv"
	with open(file_name,'r') as f:
		data = f.readlines();
	header = data[0].split(',')
	carbs_idx = 11
	prot_idx  = 14
	fat_idx   = 3
	date_idx  = 0
	meal_idx  = 1
	data.pop(0)  ## remove header
	print ("Total: {0} {1} {2} {3}".format("Date","Carbs","Fat","Protein"))
	#print (colored("Day totals: ","red"))
	for date in dates:  ## loop over dates
		carbs = 0
		prot  = 0
		fat   = 0
		for item in data:
			d = item.split(',')  ## list of data for a given meal
			if d[0] == date:
				#print (d)
				carbs = carbs + float(d[carbs_idx])
				prot  = prot  + float(d[prot_idx])
				fat   = fat   + float(d[fat_idx])
		#print ("Total: " ,date,carbs, prot, fat)
		#print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
		print ("{0} {1:4.0f} {2:4.0f} {3:4.0f}".format(date,carbs,fat,prot))





