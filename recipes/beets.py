#! /usr/bin/env python3

import json
import recipie_macros

print ("calculating macronutrients")
## mass of each ingredient in grams:
ingredients = {'beets':548,'carrots':272,'olive_oil':19}
## total cooked mass
mass_cooked = 747
## dish totals:
dish_totals = recipie_macros.calc_macros(ingredients,mass_cooked)
recipie_macros.print_ingredients(ingredients,mass_cooked)

recipie_macros.print_totals(dish_totals)

