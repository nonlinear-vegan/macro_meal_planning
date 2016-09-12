#!/usr/bin/env python3

import json

def get_ingredient_macros(ingredient):
	""" macros for each ingredient per 100 g"""
	eggplant      = {'cal':25,'fat':0.2,'carbs':6,'prot':1}
	cherry_tomato = {'cal':18,'fat':0.2,'carbs':3.9,'prot':0.9}
	olives        = {'cal':4000/15.,'fat':400/15.,'carbs':100./15.,'prot':0}
	westsoy_tofu  = {'cal':9500./79,'fat':500./79,'carbs':300./79,'prot':1000./79}
	olive_oil     = {'cal':884,'fat':100,'carbs':0,'prot':0}
	cauliflower   = {'cal':25,'fat':0.3,'carbs':5,'prot':1.9}
	onion         = {'cal':40,'fat':0.1,'carbs':9,'prot':1.1}
	summer_squash = {'cal':16,'fat':0.2,'carbs':3.4,'prot':1.2}
	return eval(ingredient)

## clculate the macros for whole dish based on ingredients
def calc_macros(ingredients,mass_cooked):
	""" calculate macros for whole dish per 100 g 
	Input a dictionary of ingredients and grams of each ingredient, and the total cooked mass
	Output a set of macros per 100 g of cooked dish
	"""
	totals = {'cal':0,'fat':0,'carbs':0,'prot':0}
	for ingredient in ingredients:
		macros = get_ingredient_macros(ingredient)
		for macro in ['cal','fat','carbs','prot']:
			totals[macro] += ingredients[ingredient] * macros[macro] / 100.
	for key in totals:
		totals[key] = totals[key] * 100.0 / mass_cooked
	return totals

#def main():
#	print ("calculating macronutrients")
#	## mass of each ingredient in grams#:
#	ingredients = {'eggplant':535,'cher#ry_tomato':164,'olives':94,'westsoy_tofu':397,'olive_oil':99}
#	## total cooked mass
#	mass_cooked =876
#	dish_totals = calc_macros(ingredients,mass_cooked)
#	print ("Macronutrients per 100g:")
#	print (json.dumps(totals,indent=4))


#if __name__ == '__main__':
#	main()

