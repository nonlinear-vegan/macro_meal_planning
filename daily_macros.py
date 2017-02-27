#!/usr/bin/env python3
from termcolor import colored
import json

def get_ingredient_macros(ingredient):
	""" macros for each ingredient quanity given amount field"""
	### fats
	flax_oil           = {'cal':40, 'fat':5,   'carbs':0, 'prot':0, 'amount':'1tsp'}  
	coconut_oil        = {'cal':20, 'fat':2.3, 'carbs':0, 'prot':0, 'amount':'1/2teasp'}
	### proteins
	westsoy_tofu        = {'cal':237, 'fat':13,  'carbs':7.5, 'prot':25,  'amount':'1/2brick'}
	nigari_tofu         = {'cal':70,  'fat':4.2, 'carbs':1.7, 'prot':8.2, 'amount':'100g'}
	banyan_tofu         = {'cal':225, 'fat':10,  'carbs':7.5, 'prot':25,  'amount':'1/2package'}
	performance_protein = {'cal':160, 'fat':3,   'carbs':6,   'prot':30,  'amount':'1scoop'} 
	vega_smoothie       = {'cal':90,  'fat':0.5, 'carbs':5,   'prot':15,  'amount':'1scoop'}
	now_pea_protein     = {'cal':120, 'fat':2,   'carbs':1,   'prot':24,  'amount':'1levelscoop'}
	nutritional_yeast   = {'cal':20,  'fat':0,   'carbs':2,   'prot':3,   'amount':'1T'}    
	### carbs
	brown_rice_dry     = {'cal':171,'fat':1,  'carbs':36, 'prot':4, 'amount':'1/4cupdry'}
	rolled_oats        = {'cal':160,'fat':2.5,'carbs':27, 'prot':7, 'amount':'1/2cupdry'}
	sweet_potato       = {'cal':86, 'fat':0,  'carbs':20, 'prot':2, 'amount':'100g'}
	acorn_squash       = {'cal':40, 'fat':0,  'carbs':10, 'prot':1, 'amount':'100g'}   
	butternut_squash   = {'cal':60, 'fat':0,  'carbs':48, 'prot':4, 'amount':'1bag'}
	## sugar carbs
	coconut_water_MP   = {'cal':60,  'fat':0,'carbs':15,'prot':0,'amount':'1boxserving'} 
	orange             = {'cal':49,  'fat':0,'carbs':13,'prot':1,'amount':'100g'}
	banana             = {'cal':110, 'fat':0,'carbs':29,'prot':1,'amount':'1medium'}
	### veggies
	onion         = {'cal':40, 'fat':0.1, 'carbs':9,   'prot':1.1, 'amount':'100g'}
	summer_squash = {'cal':16, 'fat':0.2, 'carbs':3.4, 'prot':1.2, 'amount':'100g'}
	beets         = {'cal':43, 'fat':0.2, 'carbs':10,  'prot':1.6, 'amount':'100g'}
	carrots       = {'cal':41, 'fat':0.4, 'carbs':10,  'prot':0.9, 'amount':'100g'}
	cauliflower   = {'cal':25, 'fat':0.3, 'carbs':5,   'prot':1.9, 'amount':'100g'}
	broccoli      = {'cal':17, 'fat':0,   'carbs':3.5, 'prot':1.5, 'amount':'50g'}
	### other 
	romain_lettuce     = {'cal':17, 'fat':0,   'carbs':3,   'prot':1,   'amount':'100g'}  
	green_leaf_lettuce = {'cal':15, 'fat':0,   'carbs':3,   'prot':1,   'amount':'100g'}
	green_beans        = {'cal':15, 'fat':0,   'carbs':3.5, 'prot':1,   'amount':'50g'}
	pinto_beans        = {'cal':60, 'fat':0,   'carbs':22,  'prot':7,   'amount':'1/4drycup'}  
	pea_pods           = {'cal':42, 'fat':0.2, 'carbs':7.8, 'prot':2.8, 'amount':'100g'}
	red_pepper_bell    = {'cal':15, 'fat':0,   'carbs':3,   'prot':0,   'amount':'50g'}
	eggplant           = {'cal':25, 'fat':0.2, 'carbs':6,   'prot':1,   'amount':'100g'}
	cherry_tomato      = {'cal':18, 'fat':0.2, 'carbs':3.9, 'prot':0.9, 'amount':'100g'}
	tomato_red         = {'cal':32, 'fat':0,   'carbs':7,   'prot':2,   'amount':'1cupchopped'}
	return eval(ingredient)

def calc_macros(ingredients):
	"""calc macros of meal using the commonly used amounts"""
	totals = {'cal':0,'fat':0,'carbs':0,'prot':0}
	for ingredient in ingredients:
		macros = get_ingredient_macros(ingredient)
		print (colored(("Ingredient", ingredient, " macros: ",macros), 'green'))
		for macro in ['cal','fat','carbs','prot']:
			totals[macro] = totals[macro] + macros[macro]
	return totals

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

def day_totals():
	"""Sum up the totals for the day"""
	sum = {'fat':0,'carbs':0,'prot':0}
	for macro in ['fat','carbs','prot']:
		sum[macro] = breakfast[macro] + morning_snack[macro] + lunch[macro] + afternoon_snack[macro] + dinner[macro]
	return sum

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
	breakfast = calc_macros(['westsoy_tofu','flax_oil','nutritional_yeast','romain_lettuce','red_pepper_bell','green_beans'])
	print_totals(breakfast,False)
	## MORNING SNACK
	print(colored("Morning Snack:","blue"))
	morning_snack = calc_macros(['performance_protein'])
	print_totals(morning_snack,False)
	## LUNCH
	print(colored("Lunch:","blue"))
	lunch = calc_macros(['westsoy_tofu','nutritional_yeast','flax_oil','romain_lettuce','romain_lettuce','red_pepper_bell','green_beans'])
	print_totals(lunch,False)
	## AFTERNOON SNACK (near workout time)
	print(colored("Afternoon snack:","blue"))
	afternoon_snack = calc_macros(['coconut_water_MP','vega_smoothie','orange','banana'])
	print_totals(afternoon_snack,False)
	## DINNER
	print(colored("Dinner:","blue"))
	dinner = calc_macros(['broccoli','flax_oil','flax_oil','performance_protein','acorn_squash','acorn_squash','acorn_squash','now_pea_protein','brown_rice_dry'])
	print_totals(dinner,False)
	## DAY TOTALS
	day_total = day_totals()
	print (colored("Day totals: ","red"))
	print_totals(day_total,True)

# 4 meals and 2 snacks
# same fraction of protein in each
# 50 g carbs before workout
# 50 g carbs after workout
# fats in morning or dinner, not near workout

