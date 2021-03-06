#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if recipe.keys() == ingredients.keys():
    counter = 0
    arr = []
    for key in ingredients:
      if ingredients[key] >= recipe[key]:
        batch = ingredients[key] // recipe[key]
        arr.append(batch)
        counter = min(arr)
        return counter
        print ("You have enough ingredients for",{counter},"batch(es).")
    else:
      print("Not enough ingredients.")
  return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 480, 'flour': 510 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
