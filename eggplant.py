import json

## macros for ingredients per 100 g
def get_ingredient_macros(ingredient):
	eggplant      = {'cal':25,'fat':0.2,'carbs':6,'prot':1}
	cherry_tomato = {'cal':18,'fat':0.2,'carbs':3.9,'prot':0.9}
	olives        = {'cal':4000/15.,'fat':400/15.,'carbs':100./15.,'prot':0}
	westsoy_tofu  = {'cal':9500./79,'fat':500./79,'carbs':300./79,'prot':1000./79}
	olive_oil     = {'cal':884,'fat':100,'carbs':0,'prot':0}
	return eval(ingredient)

def calc_macros(ingredients,mass_cooked,totals):
	for ingredient in ingredients:
		macros = get_ingredient_macros(ingredient)
		for macro in ['cal','fat','carbs','prot']:
			totals[macro] += ingredients[ingredient] * macros[macro] / 100.
	for key in totals:
		totals[key] = totals[key] * 100.0 / mass_cooked
	return totals

def main():
	print ("calculating macronutrients")
	## mass of each ingredient in grams:
	ingredients = {'eggplant':535,'cherry_tomato':164,'olives':94,'westsoy_tofu':397,'olive_oil':99}
	mass_cooked =876
	totals = {'cal':0,'fat':0,'carbs':0,'prot':0}
	dish_totals = calc_macros(ingredients,mass_cooked,totals)
	print ("Macronutrients per 100g:")
	print (json.dumps(totals,indent=4))


if __name__ == '__main__':
	main()

#totals = {'cal':0,'fat':0,'carbs':0,'prot':0}
#macros = ['cal','fat','carbs','prot']

#def calc_macros(ingredients,mass_cooked):
#	for key in ingredients:
#		print ('key: ',key)
#		try:
#			for macro in macros:
#				print ('key[',macro,']: ',eval(key)[macro])
#				totals[macro] += ingredients[key] * eval(key)[macro] / 100.
#		except:
#			print ("fail for key: ",key)

#for key in totals:
#	totals[key] = totals[key] * 100.0 / mass_cooked

#print ("Macronutrients per 100 g")
#print (json.dumps(totals,indent=4))
#
#print ("calling calcme")
#calcme()
