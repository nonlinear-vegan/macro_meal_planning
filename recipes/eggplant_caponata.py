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
recipie_macros.print_ingredients(ingredients,mass_cooked)

recipie_macros.print_totals(dish_totals)

