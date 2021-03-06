## Class for creating JSON objects (dictionaries) to place in data table ##
class ObjectCreator:

    def create_ingredient(self, upc = 0, name = '', quantity = 0, unit = '', shelf_life = 0, price = 0, calories = 0, default_tags = []):
        ingredient = {}
        ingredient['upc'] = upc
        ingredient['name'] = name
        ingredient['quantity'] = quantity
        ingredient['unit'] = unit
        ingredient['shelf_life'] = shelf_life
        ingredient['price'] = price
        ingredient['calories'] = calories
        ingredient['default_tags'] = default_tags
        return ingredient

    def create_recipe(self, name = '', ingredients = [], instructions = [], rating = 0, tags = [], last_used = 0, serving_size = 0):
        recipe = {}
        recipe['name'] = name
        recipe['ingredients'] = ingredients
        recipe['instructions'] = instructions
        recipe['rating'] = rating
        recipe['tags'] = str.split(name) + tags
        recipe['last_used'] = last_used
        recipe['serving_size'] = serving_size
        return recipe

    def create_fridge_ingredient(self, ingredient, name = '', quantity = 0, unit = '', insert_time = 0, count = 0, tags = []):
        fridge_ingredient = {}
        fridge_ingredient['ingredient'] = ingredient
        fridge_ingredient['name'] = name
        fridge_ingredient['quantity'] = quantity
        fridge_ingredient['unit'] = unit
        fridge_ingredient['insert_time'] = insert_time
        fridge_ingredient['count'] = count
        fridge_ingredient['tags'] = tags
        return fridge_ingredient

    def create_recipe_ingredient(self, ingredient, name = '', quantity = 0, unit = ''):
        recipe_ingredient = {}
        recipe_ingredient['ingredient'] = ingredient
        recipe_ingredient['name'] = name
        recipe_ingredient['quantity'] = quantity
        recipe_ingredient['unit'] = unit
        return recipe_ingredient

