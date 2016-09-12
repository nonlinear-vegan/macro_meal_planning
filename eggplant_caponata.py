#!/usr/bin/env python3

import json
import recipie_macros
import sys

print ("\n\nCalculating macronutrients for "+ sys.argv[0][:-3])
## mass of each ingredient in grams:
ingredients = {'eggplant':535,'cherry_tomato':164,'olives':94,'westsoy_tofu':397,'olive_oil':99}
## total cooked mass
mass_cooked =876
## dish totals:
dish_totals = recipie_macros.calc_macros(ingredients,mass_cooked)

print ("Macronutrients per 100g:")

print ("cal:    {0:>4.0f}".format(dish_totals['cal']))
print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
print ("carbs:  {0:>4.0f}".format(dish_totals["carbs"]))
print ("prot:   {0:>4.0f}".format(dish_totals["prot"]))


#print ("cal:  %f2" % dish_totals['cal'])
#print ("fat:   ",dish_totals['fat'])
#print ("carbs: ",dish_totals['carbs'])
#print ("prot:  ",dish_totals['prot'])
