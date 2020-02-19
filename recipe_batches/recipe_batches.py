#!/usr/bin/python

import math
from types import SimpleNamespace

# get recipe ingredient names (keys)
# create a variable for each key
# get ratio of each ingredient / recipe
# find the smallest value and round down
# return the value

ingredients = {
  'eggs': 5,
  'butter': 23,
  'sugar': 8,
}

recipe = {
  'butter': 10,
  'sugar': 8,
  'flour': 15
}

# def recipe_batches(recipe, ingredients):
# 	smallest_ratio = math.inf
# 	for key in recipe.keys():
# 		try:
# 			current_ratio = ingredients[key] // recipe[key]
# 		except KeyError:
# 			current_ratio = 0
# 		if current_ratio < smallest_ratio:
# 				smallest_ratio = current_ratio
# 	return smallest_ratio


def recipe_batches(recipe, ingredients):
  smallest_ratio = math.inf

  for key in recipe.keys():
    try:
      current_ratio = ingredients[key] // recipe[key]
      # print(current_ratio, key)
    except:
      current_ratio = 0
      # print('error on', key, ':', current_ratio)
    smallest_ratio = min(current_ratio, smallest_ratio)
  
  return smallest_ratio

# recipe_batches(recipe, ingredients)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

