#!/usr/bin/env python3

import json
import recipie_macros
import sys

print ("\n\nCalculating macronutrients for "+ sys.argv[0][:-3])
## mass of each ingredient in grams:
ingredients = {'eggplant':100,'cauliflower':100}
## total cooked mass
mass_cooked =200
## dish totals:
dish_totals = recipie_macros.calc_macros(ingredients,mass_cooked)

recipie_macros.print_ingredients(ingredients,mass_cooked)

recipie_macros.print_totals(dish_totals)
