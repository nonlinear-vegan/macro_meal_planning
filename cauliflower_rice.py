#!/usr/bin/env python3

import json
import recipie_macros

print ("calculating macronutrients")
## mass of each ingredient in grams:
ingredients = {'cauliflower':1205,'onion':105,'olive_oil':33}
## total cooked mass
mass_cooked = 1014
## dish totals:
dish_totals = recipie_macros.calc_macros(ingredients,mass_cooked)

print ("Macronutrients per 100g:")

print ("cal:    {0:>4.0f}".format(dish_totals['cal']))
print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
print ("carbs:  {0:>4.0f}".format(dish_totals["carbs"]))
print ("prot:   {0:>4.0f}".format(dish_totals["prot"]))

