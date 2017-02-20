#!/usr/bin/env python3

import json

# protein: 163 g
# fat:      58 g
# carbs:   185 g
#
# 4 meals and 2 snacks
# same fraction of protein in each
# 50 g carbs before workout
# 50 g carbs after workout
# fats in morning or dinner, not near workout

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
	beets         = {'cal':43,'fat':0.2,'carbs':10,'prot':1.6}
	carrots       = {'cal':41,'fat':0.4,'carbs':10,'prot':0.9}
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
			totals[macro] = totals[macro] + ingredients[ingredient] * macros[macro] / 100.
			#print ("totals: ",totals[macro])
	for key in totals:
		totals[key] = totals[key] * 100.0 / mass_cooked
		#totals[key] = totals[key] / mass_cooked
	#print ('mass_cooked: ',mass_cooked)
	return totals

def print_totals(dish_totals):
	print ("\nMacronutrients per 100g:\n")
	print ("cal:    {0:>4.0f}".format(dish_totals['cal']))
	print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
	print ("carbs:  {0:>4.0f}".format(dish_totals["carbs"]))
	print ("prot:   {0:>4.0f}".format(dish_totals["prot"]))
	#print ("cal:   ",dish_totals['cal'])
	#print ("fat:   ",dish_totals['fat'])
	#print ("carbs: ",dish_totals['carbs'])
	#print ("prot:  ",dish_totals['prot'])

def print_ingredients(ingredients,mass_cooked):
	print ("\nIngredients: \n")
	for ingredient in ingredients:
		print(ingredient)
