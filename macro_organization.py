#!/usr/bin/env python3
from termcolor import colored
import json

def get_ingredient_macros(ingredient):
	""" macros for each ingredient quanity given in comment"""
	eggplant      = {'cal':25,'fat':0.2,'carbs':6,'prot':1,'amount':'100g'}
	cherry_tomato = {'cal':18,'fat':0.2,'carbs':3.9,'prot':0.9,'amount':'100g'}
	olives        = {'cal':4000/15.,'fat':400/15.,'carbs':100./15.,'prot':0,'amount':'100g'}
	#westsoy_tofu  = {'cal':9500./79,'fat':500./79,'carbs':300./79,'prot':1000./79}  
	westsoy_tofu  = {'cal':237,'fat':13,'carbs':7.5,'prot':25,'amount':'1/2brick'}  ## 1 brick
	cauliflower   = {'cal':25,'fat':0.3,'carbs':5,'prot':1.9,'amount':'100g'}
	onion         = {'cal':40,'fat':0.1,'carbs':9,'prot':1.1,'amount':'100g'}
	summer_squash = {'cal':16,'fat':0.2,'carbs':3.4,'prot':1.2,'amount':'100g'}
	beets         = {'cal':43,'fat':0.2,'carbs':10,'prot':1.6,'amount':'100g'}
	carrots       = {'cal':41,'fat':0.4,'carbs':10,'prot':0.9,'amount':'100g'}
	performance_protein= {'cal':160,'fat':3,'carbs':6,'prot':30,'amount':'1scoop'} ## 1 scoop
	vega_smoothie      = {'cal':90,'fat':0.5,'carbs':5,'prot':15,'amount':'1scoop'}
	flax_oil           = {'cal':40, 'fat':5,'carbs':0,'prot':0,'amount':'1tsp'}  ## 1 tsp
	nutritional_yeast  = {'cal':20,'fat':0,'carbs':2,'prot':3,'amount':'1T'}    ## 2 TABLE
	romain_lettuce     = {'cal':17,'fat':0,'carbs':3,'prot':1,'amount':'100g'}    ## 100 g
	green_leaf_lettuce = {'cal':15,'fat':0,'carbs':3,'prot':1,'amount':'100g'}
	pinto_beans        = {'cal':60,'fat':0,'carbs':22,'prot':7,'amount':'1/4drycup'}   ## 1/4 cup dry
	coconut_water_MP   = {'cal':60,'fat':0,'carbs':15,'prot':0,'amount':'1boxserving'}  ## 1 serving box
	coconut_oil        = {'cal':20,'fat':2.3,'carbs':0,'prot':0,'amount':'1/2teasp'}
	orange             = {'cal':69,'fat':0,'carbs':18,'prot':1,'amount':'1orange'}
	acorn_squash       = {'cal':40,'fat':0,'carbs':10,'prot':1,'amount':'100g'}   ## 100 g
	sweet_potato       = {'cal':86,'fat':0,'carbs':20,'prot':2,'amount':'100g'}
	red_pepper_bell    = {'cal':15,'fat':0,'carbs':3,'prot':0,'amount':'50g'}
	return eval(ingredient)

## clculate the macros for meal using common amounts of each
def calc_macros(ingredients):
	"""calc macros of meal"""
	totals = {'cal':0,'fat':0,'carbs':0,'prot':0}
	for ingredient in ingredients:
		macros = get_ingredient_macros(ingredient)
		print (colored(("Ingredient", ingredient, " macros: ",macros), 'green'))
		for macro in ['cal','fat','carbs','prot']:
			totals[macro] = totals[macro] + macros[macro]
	return totals

def print_totals(dish_totals,day):
	#print ("cal:    {0:>4.0f}".format(dish_totals['cal']))
	if day:
		print ("fat:    {0:>4.0f} (daily goal:  58)".format(dish_totals['fat']))
		print ("carbs:  {0:>4.0f} (daily goal: 185)".format(dish_totals["carbs"]))
		print ("prot:   {0:>4.0f} (daily goal: 163)".format(dish_totals["prot"]))
	else:
		print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
		print ("carbs:  {0:>4.0f}".format(dish_totals["carbs"]))
		print ("prot:   {0:>4.0f}".format(dish_totals["prot"]))

def day_totals():
	sum = {'fat':0,'carbs':0,'prot':0}
	for macro in ['fat','carbs','prot']:
		sum[macro] = breakfast[macro] + morning_snack[macro] + lunch[macro] + afternoon_snack[macro] + dinner[macro]
	return sum

if __name__ == '__main__':
	print ("total protein: 163g")
	print ("total fats:     58g")
	print ("total carbs:   185g\n\n")
	print ("Protein in each snack: {0:>4.0f} g".format(163.0/6))
	print ("Fat in each meal:      {0:>4.0f} g".format(58.0/3))
	print ("Carbs in non-breakfast/non-workout:  {0:>4.0f} g".format((185-100)/3))
	print ("\n")
	## BREAKFAST
	print(colored("Breakfast:",'blue'))
	breakfast = calc_macros(['romain_lettuce','romain_lettuce','nutritional_yeast','westsoy_tofu','flax_oil','red_pepper_bell'])
	print_totals(breakfast,False)
	## MORNING SNACK
	print(colored("Morning Snack:","blue"))
	morning_snack = calc_macros(['performance_protein'])
	print_totals(morning_snack,False)
	## LUNCH
	print(colored("Lunch:","blue"))
	lunch = calc_macros(['romain_lettuce','romain_lettuce','nutritional_yeast','westsoy_tofu','flax_oil','beets','orange'])
	print_totals(lunch,False)
	## AFTERNOON SNACK (near workout time)
	print(colored("Afternoon snack:","blue"))
	afternoon_snack = calc_macros(["coconut_water_MP",'vega_smoothie','orange','beets'])
	print_totals(afternoon_snack,False)
	## DINNER
	print(colored("Dinner:","blue"))
	dinner = calc_macros(["performance_protein","acorn_squash","acorn_squash","coconut_oil","westsoy_tofu","sweet_potato","sweet_potato"])
	print_totals(dinner,False)
	## DAY TOTALS
	day_total = day_totals()
	print ("Day totals: ")
	print_totals(day_total,True)

# 4 meals and 2 snacks
# same fraction of protein in each
# 50 g carbs before workout
# 50 g carbs after workout
# fats in morning or dinner, not near workout

