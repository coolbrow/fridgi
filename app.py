## Creates endpoints for android device to access database operations ##

import tornado.ioloop
import tornado.web
import os
import fake_data
import api.database_api
import api.fridge_api
from bson.json_util import dumps
from bson.objectid import ObjectId

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello Fridgi")

class IngredientHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(dumps(apiObj.get_all_ingredients()))

class RecipeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(dumps(apiObj.get_all_recipes()))

class SearchRecipeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(dumps(apiObj.search_recipes(str(self.get_argument('tags')))))

class SearchFridgeRecipeHandler(tornado.web.RequestHandler):
	def get(self, slug):
		self.write(dumps(fridgeObj.search_fridge_recipes(str(self.get_argument('tags')), slug)))

class FridgeHandler(tornado.web.RequestHandler):
	def get(self, slug):
		self.write(dumps(apiObj.get_fridge(slug)))

class SuggestRecipeHandler(tornado.web.RequestHandler):
	def get(self, slug):
		self.write(dumps(fridgeObj.suggest_by_current_recipe(ObjectId(self.get_argument('recipe')), slug)))

class InsertHandler(tornado.web.RequestHandler):
	# Probably should make POST request instead of GET
	def get(self, slug):
		ingredient = apiObj.get_ingredient_info_from_upc(long(self.get_argument('upc')))
		fridge = apiObj.get_fridge(slug)
		if (fridge != None):
			apiObj.insert_ingredient(ingredient['name'], slug)
			self.write("Success")	# Change this to 200 later
			return
		self.write("Failure")		# Change this to 40X later

class UseRecipeHandler(tornado.web.RequestHandler):
	def get(self, slug):
		fridgeObj.use_recipe(ObjectId(self.get_argument('recipe')), slug)
		self.write("Success")

class AddToGroceryListHandler(tornado.web.RequestHandler):
	def get(self, slug):
		ingredient_id = ObjectId(self.get_argument('ingredient'))
		quantity = float(self.get_argument('quantity'))
		fridgeObj.add_item_to_grocery_list(ingredient_id, quantity, slug)
		self.write("Success")

class RemoveFromGroceryListHandler(tornado.web.RequestHandler):
	def get(self, slug):
		ingredient_id = ObjectId(self.get_argument('ingredient'))
		apiObj.remove_item_from_grocery_list(ingredient_id, slug)
		self.write("Success")

# FOR TESTING. REMOVE LATER
class ResetListHandler(tornado.web.RequestHandler):
	def get(self):
		fake_data.reset_db(apiObj)
		self.write("Database Reset!")

application = tornado.web.Application([
	(r"/", MainHandler),
    (r"/ingredients", IngredientHandler),
    (r"/recipes", RecipeHandler),
    (r"/fridge/([^/]+)", FridgeHandler),
    (r"/search", SearchRecipeHandler),
    (r"/fridge/([^/]+)/search", SearchFridgeRecipeHandler),
    (r"/fridge/([^/]+)/suggest", SuggestRecipeHandler),
    (r"/fridge/([^/]+)/insert", InsertHandler),
    (r"/fridge/([^/]+)/use", UseRecipeHandler),
    (r"/fridge/([^/]+)/add", AddToGroceryListHandler),
    (r"/fridge/([^/]+)/remove", RemoveFromGroceryListHandler),
    (r"/reset", ResetListHandler),
])

if __name__ == "__main__":
	# Create testing db
	apiObj = api.database_api.DatabaseApi()
	fridgeObj = api.fridge_api.FridgeApi(apiObj)
	fake_data.reset_db(apiObj)
	
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()
