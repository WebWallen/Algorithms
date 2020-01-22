#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 200, 'butter': 100, 'flour': 51 }
not_enough_ingredients = { 'milk': 50, 'butter': 25, 'flour': 2 }

def recipe_batches(recipe, ingredients):
  # Step 1: loop through values of recipe/ingredients so we can do math on the amounts
  for recipe_value in recipe.values():
    # Step 2: label the values very specifically to prevent confusion
    for ingredient_value in ingredients.values():
      # Step 3: if the recipe calls for a higher amount than ingredients, return 0 (can't make it)
      if recipe_value > ingredient_value:
        print('Sorry, you have to buy some groceries before you can make this!')
        return 0
      # Step 4: otherwise, divide total ingredients by amount demaned in recipe to determine how many batches can be made
      else:
        batches = ingredient_value // recipe_value
        print(f"{batches} batches can be made from the available ingredients: {ingredients}.")
        return batches

recipe_batches(recipe, ingredients)
recipe_batches(recipe, not_enough_ingredients)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 200, 'butter': 100, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))