## Updating the global ingredients and recipes database
import pymongo

# Should probably make this a class, so we can keep the mongo connection 
# and database as a class variable instead of a global
connection = pymongo.Connection()
# Name database 'db' for now. 
db = connection.db

# input  : ingredient object
def add_ingredient(ingredient):
	""" Adds ingredient to Ingredients collection """
	ingredients = db.ingredients
	ingredients.insert(ingredient)
  

# input  : recipe object
def add_recipe(recipe):
	""" Adds recipe to Recipes collection """
	recipes = db.recipes
	recipes.insert(recipes)


# input  : name of ingredient (as string)
# return : Ingredient Object
def get_ingredient_info_from_name(ingredient):
	ingredients = db.ingredients
	return ingredients.find_one({'name' : ingredient})

# input  : upc of ingredient (as num)
# return : Ingredient Object
def get_ingredient_info_from_upc(upc):
	ingredients = db.ingredients
	return ingredients.find_one({'upc' : upc})

# input  : name of recipe (as string)
# return : Recipe Object
def get_recipe_info(recipe):
	recipes = db.recipes
	return recipes.find_one({'name' : recipe})

# input  : name of recipe (as string)
# return : array of required Ingredients
def get_ingredients_by_recipe(recipe):
	recipe = get_recipe_info(recipe)
	return recipe['ingredients']

# input  : name of ingredient (as string)
# return : array of Recipes that use ingredient input
def get_recipes_by_ingredients(ingredient):
	pass

# return : entire Ingredients collection
def get_all_ingredients():
	pass

# return : entire Recipes collection
def get_all_recipes():
	pass

# input  : fridge ID or name
# return : array of current Ingredients
def get_current_ingredients(fridge):
	pass


# input  : ingredient name, fridge name
def insert_ingredient(ingredient, fridge):
	pass

# input  : ingredient name, quantity, fridge name
def update_ingredient(ingredient, quantity, fridge):
	pass

# input  : recipe name as string
# return : boolean representing if fridge has necessary ingredients
def can_cook(recipe, fridge):
	# check if recipe in recipes collection
	# look through Recipe Ingredient objects, compare to Fridge Ingredients
	# if all Recipe Ingredients are accounted for, return true
	# else, return false
	pass
