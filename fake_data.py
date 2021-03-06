## Used to populate our DB ##

import api.database_api
import api.creator

count = 0

def d_i(api, c, upc, name, quantity, unit):
	ingredient = c.create_ingredient(upc = upc, name = name, quantity = quantity, unit = unit)
	api.add_ingredient(ingredient)

def r_i(api, name, quantity):
	ingredient = {}
	ingredient['name'] = name
	ingredient['ingredient'] = api.get_ingredient_info_from_name(name)['_id']
	ingredient ['quantity'] = quantity
	ingredient['unit'] = api.get_ingredient_info_from_name(name)['unit']
	return ingredient

def f_i(api, name, number):
	i = 0
	while i < number:
		api.insert_ingredient(name, 'fridgi')
		i += 1

def all_i(api, c, name, quantity, unit, number_to_insert_into_fridge):
	global count
	count += 1
	d_i(api, c, count, name, quantity, unit)
	f_i(api, name, number_to_insert_into_fridge)
	return r_i(api, name, quantity)

def all_i_upc(api, c, name, quantity, unit, number_to_insert_into_fridge, upc):
	d_i(api, c, upc, name, quantity, unit)
	f_i(api, name, number_to_insert_into_fridge)
	return r_i(api, name, quantity)

def insert_some_recipes(api, c):
	
	global count

	api.add_fridge('fridgi')
	cup = 'cup'
	oz = 'ounce'
	na = ''
	tsp = 'teaspoon'
	tbsp = 'tablespoon'
	clove = 'clove'
	lb = 'pound'
	t = True
	f = False

	chicken = all_i(api, c, 'chicken breast', 5, cup, 2)
	onion = all_i(api, c, 'onion', 2, na, 1)
	penne = all_i(api, c, 'penne', 12, oz, 1)
	tomatoes = all_i(api, c, 'cherry tomato', 2, cup, 25)
	arugula = all_i(api, c, 'arugula leaves', 2, cup, 10)
	feta = all_i(api, c, 'feta cheese', 1, cup, 10)
	olive_oil = all_i(api, c, 'olive oil', 8, tsp, 2)
	garlic = all_i(api, c, 'garlic', 2, clove, 25)
	crushed_red_pepper = all_i(api, c, 'crushed red pepper', 1, tsp, 20)
	apple_juice = all_i(api, c, 'apple juice', 10, cup, 1)
	peach = all_i(api, c, 'peach', 1, na, 1)
	banana = all_i(api, c, 'banana', 1, na, 1)
	vanilla_yogurt = all_i(api, c, 'vanilla yogurt', 10, tsp, 1)
	ice_cubes = all_i(api, c, 'ice cube', 1, na, 1)
	honey = all_i(api, c, 'honey', 2, tsp, 1)
	flaxseed_oil = all_i(api, c, 'flaxseed oil', 2, tsp, 1)
	porcini_mushroom = all_i(api, c, 'porcini mushroom', 0.5, oz, 1)
	butter = all_i(api, c, 'butter', 6, tsp, 3)
	shiitake_mushroom = all_i(api, c, 'shiitake mushroom', 6, oz, 1)
	flour = all_i(api, c, 'flour', 2.5, tbsp, 1)
	whole_milk = all_i(api, c, 'whole milk', 2.5, cup, 10)
	parmesan_cheese = all_i(api, c, 'parmesan cheese', 0.75, cup, 1)
	chives = all_i(api, c, 'chives', 0.5, cup, 1)
	breadcrumbs = all_i(api, c, 'breadcrumbs', 0.5, cup, 1)
	baguette = all_i(api, c, 'baguette', 1, na, 1)
	egg = all_i(api, c, 'egg', 1, na, 24)
	lemon_juice = all_i(api, c, 'lemon juice', 2, tbsp, 10)

	anchovy_paste = all_i_upc(api, c, 'anchovy paste', 1, tbsp, 0, 48000002624)
	
	basil = all_i(api, c, 'basil leaves', 1, cup, 1)
	parsley = all_i(api, c, 'parsley', 0.5, cup, 1)
	romaine = all_i(api, c, 'romaine hearts', 1, lb, 1)

	mexican_cheese = all_i_upc(api, c, 'mexican cheese', 1, cup, 0, 21000601516)

	potato = all_i(api, c, 'potatoes', 2, lb, 3)
	salt = all_i(api, c, 'salt', 1.5, tsp, 20)
	white_pepper = all_i(api, c, 'white pepper', 0.25, tsp, 30)
	sherry_vinegar = all_i(api, c, 'sherry vinegar', 2, tsp, 1)
	sea_salt = all_i(api, c, 'sea salt', 0.25, tsp, 1)
	dijon_mustard = all_i(api, c, 'dijon mustard', 0.5, tsp, 1)
	mixed_salad_greens = all_i(api, c, 'mixed salad greens', 7, oz, 1)
	peach_schnapps = all_i(api, c, 'peach schnapps', 0.5, cup, 1)
	sugar = all_i(api, c, 'sugar', 0.5, cup, 1)
	chilled_rose_wine = all_i(api, c, 'chilled rose wine', 3, cup, 0)
	chilled_sparkling_water = all_i(api, c, 'chilled sparkling water', 2, cup, 0)
	gruyere = all_i(api, c, 'gruyere', 4, oz, 1)
	chocolate = all_i(api, c, 'chocolate', 5, oz, 1)
	instant_espresso_powder = all_i(api, c, 'instant espresso powder', 2, tsp, 0)
	vanilla_extract = all_i(api, c, 'vanilla extract', 1, tsp, 1)
	cinnamon = all_i(api, c, 'cinnamon', 1, tbsp, 1)
	chocolate_chips = all_i(api, c, 'chocolate chips', 0.75, cup, 1)
	watermelon = all_i(api, c, 'watermelon', 2, cup, 1)
	lemonade_concentrate = all_i(api, c, 'lemonade concentrate', 0.75, cup, 1)
	strawberries = all_i(api, c, 'strawberries', 2, cup, 1)
	balsamic_vinegar = all_i(api, c, 'balsamic vinegar', 2.5, tbsp, 1)
	bacon = all_i(api, c, 'bacon', 8, 'slices', 1)

	campanelle = all_i(api, c, 'campanelle', 1, lb, 1)
	zucchini = all_i(api, c, 'zucchini', 2, lb, 1)
	oregano = all_i(api, c, 'oregano', 2, tbsp, 1)
	pecorino_cheese = all_i(api, c, 'pecorino cheese', 0.5, cup, 1)

	green_beans = all_i(api, c, 'green beans', 2, lb, 1)
	lemon = all_i(api, c, 'lemon', 1, na, 1)

	# chicken penne pasta
	ingredients = [tomatoes, olive_oil, garlic, crushed_red_pepper, chicken, penne, arugula, feta]
	step1 = "Preheat oven to 475F. Mix cherry tomatoes, oil, garlic, and crushed red pepper on rimmed baking sheet. Sprinkle with salt and pepper. Bake until tomatoes are soft and beginning to brown in spots, stirring occasionally, about 20 minutes. Transfer tomato mixture, including any juices, from sheet to large skillet. Add chicken to skillet and simmer until heated through, about 5 minutes."
	step2 = "Meanwhile, cook pasta in large pot of boiling salted water until just tender but still firm to bite, stirring occasionally. Ladle out 1/4 cup pasta cooking water and reserve. Drain pasta; return to pot."
	step3 = "Add tomato mixture, arugula, and reserved 1/4 cup pasta cooking water to pasta; toss over medium heat just until arugula begins to wilt, about 30 seconds. Season to taste with salt and pepper. Transfer pasta to bowl. Sprinkle with feta cheese and serve."
	steps = [step1, step2, step3]
	chicken_pasta = c.create_recipe(name = 'chicken penne pasta', ingredients = ingredients, instructions = steps, tags = [], serving_size = 4)
	api.add_recipe(chicken_pasta)

	# baked mushroom penne pasta
	ingredients = [porcini_mushroom, butter, shiitake_mushroom, flour, whole_milk, parmesan_cheese, chives, breadcrumbs]
	step1 = "Place porcini in small bowl. Add 2 cups hot water and let soften 20 minutes. Using slotted spoon, remove porcini. Reserve liquid. Coarsely chop porcini."
	step2 = "Melt 3 tablespoons butter in heavy large skillet over medium-high heat. Add onions and saute until soft, about 5 minutes. Add button and shiitake mushrooms and saute 5 minutes. Mix in porcini and reserved soaking liquid, leaving any sediment behind in bowl. Simmer over medium-high heat 10 minutes."
	step3 = "Melt remaining 3 tablespoons butter in heavy medium saucepan over medium heat. Add flour and stir constantly until golden, about 2 minutes. Gradually whisk in milk. Stir until sauce thickens and boils, about 3 minutes. Stir into mushroom mixture. Simmer 2 minutes, stirring occasionally. Stir in 1/2 cup Parmesan cheese and chives. Season sauce to taste with salt and pepper. Set aside. (Sauce can be prepared 1 day ahead. Cover and refrigerate. Rewarm over medium-low heat before continuing.)"
	step4 = "Preheat oven to 425F. Butter 13 x 9 x 2-inch glass baking dish. Cook pasta in large pot of boiling salted water until tender but still firm to bite. Drain well. Return to pot. Add mushroom sauce and toss well to coat. Transfer to prepared baking dish. Sprinkle breadcrumbs and remaining 1/4 cup Parmesan over. Bake casserole until heated through and light golden, about 25 minutes."
	steps = [step1, step2, step3, step4]
	baked_mushroom_penne_pasta = c.create_recipe(name = 'baked mushroom penne pasta', ingredients = ingredients, instructions = steps)
	api.add_recipe(baked_mushroom_penne_pasta)

	# scrambled egg pasta
	ingredients = [egg, parmesan_cheese, bacon, onion, penne]
	s1 = "1. In a small bowl, beat together the eggs and cheese; set aside."
	s2 = "2. In a large skillet, fry the bacon and onion together until the meat is browned and crispy and the onion has begun to caramelize."
	s3 = "3. Add the pasta (if using cold day-old pasta, cook until it's just warmed through, about 1 minute)."
	s4 = "4. Pour the egg-and-cheese mixture into the skillet and reduce heat to low. Stir continuously until the pasta is coated with the eggs and they have begun to solidify."
	s5 = "5. Season with the salt and pepper, then serve immediately, with extra grated Parmesan on the side."
	steps = [s1, s2, s3, s4, s5]
	scrambled_egg_pasta = c.create_recipe(name = 'scrambled egg pasta', ingredients = ingredients, instructions = steps)
	api.add_recipe(scrambled_egg_pasta)

	# zucchini and oregano pasta
	ingredients = [campanelle, olive_oil, zucchini, garlic, oregano, pecorino_cheese]
	s1 = "Cook pasta in large pot of boiling salted water until tender but still firm to bite, stirring occasionally. Drain, reserving 1 cup cooking liquid. Return pasta to pot."
	s2 = "Heat 2 tablespoons oil in heavy large skillet over high heat. Add zucchini; saute until tender and beginning to brown, about 8 minutes. Mix in garlic and oregano; remove from heat. Add zucchini mixture to pasta, adding reserved pasta cooking liquid by 1/4 cupfuls as needed to moisten. Add 1/2 cup cheese; stir until melted. Transfer to large bowl. Serve, passing additional cheese for sprinkling."
	steps = [s1, s2]
	zucchini_and_oregano_pasta = c.create_recipe(name = 'zucchini and oregano pasta', ingredients = ingredients, instructions = steps)
	api.add_recipe(zucchini_and_oregano_pasta)

	# sweet peach smoothie
	ingredients = [apple_juice, peach, banana, vanilla_yogurt, ice_cubes, honey, flaxseed_oil]
	step1 = "Combine the apple juice, peach, banana, yogurt, and ice in a blender and puree until smooth. Add the honey and flaxseed oil and puree briefly to incorporate."
	step2 = "Pour into glasses and serve right away."
	steps = [step1, step2]
	sweet_peach_smoothie = c.create_recipe(name = 'sweet peach smoothie', ingredients = ingredients, instructions = steps, tags = [])
	api.add_recipe(sweet_peach_smoothie)

	# peach sangria
	ingredients = [peach, peach_schnapps, sugar, chilled_rose_wine, chilled_sparkling_water]
	s1 = "Stir together peaches, schnapps, and sugar in a large pitcher until sugar is dissolved and let stand 1 hour."
	s2 = "Stir in wine, sparkling water, and some ice."
	steps = [s1, s2]
	peach_sangria = c.create_recipe(name = 'peach sangria', ingredients = ingredients, instructions = steps)
	api.add_recipe(peach_sangria)

	# basil caesar salad
	ingredients = [baguette, egg, lemon_juice, anchovy_paste, basil, parsley, romaine, mexican_cheese]
	step1 = "Preheat oven to 375F with rack in middle."
	step2 = "Toss bread with 2 tablespoons oil and 1/4 teaspoon each of salt and pepper in a large 4-sided sheet pan, then spread out in 1 layer. Toast in oven, stirring halfway through, until golden, 12 to 15 minutes."
	step3 = " Meanwhile, with motor running, drop garlic into a food processor and finely chop. Add egg, lemon juice, anchovy paste, and 1/2 teaspoon pepper and pulse until combined. With motor running, add remaining 6 tablespoons oil in a slow stream, blending until emulsified. Add herbs and blend until dressing turns green and herbs are finely chopped."
	step4 = "Toss romaine with dressing, croutons, and half of cheese in a large bowl. Sprinkle with remaining cheese."
	steps = [step1, step2, step3, step4]
	basil_caesar_salad = c.create_recipe(name = 'basil caesar salad', ingredients = ingredients, instructions = steps)
	api.add_recipe(basil_caesar_salad)

	# green salad with oil and vinegar dressing
	ingredients = [sherry_vinegar, sea_salt, dijon_mustard, garlic, olive_oil, mixed_salad_greens]
	s1 = "1. Place the vinegar, salt, pepper, mustard, and garlic in a medium-size bowl and whisk together until blended. Slowly add the olive oil, whisking constantly, until the dressing is emulsified."
	s2 = "2. Add the greens and toss well until they are coated with the dressing. Season with pepper to taste and serve the salad immediately."
	steps = [s1, s2]
	green_salad_with_oil_and_vinegar_dressing = c.create_recipe(name = 'green salad with oil and vinegar dressing', ingredients = ingredients, instructions = steps)
	api.add_recipe(green_salad_with_oil_and_vinegar_dressing)

	# light and silky mashed potatoes
	ingredients = [potato, salt, whole_milk, butter, white_pepper]
	s1 = "Peel potatoes and cut into 1-inch cubes. Transfer to a 3-quart heavy saucepan and add 5 cups cold water and 1 teaspoon salt, then bring to a boil. Reduce heat and simmer, partially covered, until potatoes are tender, 10 to 15 minutes."
	s2 = "Drain potatoes in a colander, then return to pan and cook over moderate heat, shaking pan occasionally, until dry, 1 to 2 minutes. Transfer potatoes to a bowl and keep hot, covered. Heat milk, butter, white pepper, and remaining 1/2 teaspoon salt in saucepan over moderate heat until butter is melted."
	s3 = "Force potatoes through food mill or ricer into hot milk mixture in pan and gently stir with a large heatproof rubber spatula just until combined."
	steps = [s1, s2, s3]
	light_and_silky_mashed_potatoes = c.create_recipe(name = 'light and silky mashed potatoes', ingredients = ingredients, instructions = steps)
	api.add_recipe(light_and_silky_mashed_potatoes)

	# golden scalloped potatoes
	ingredients = [potato, butter, flour, whole_milk, gruyere]
	s1 = "Heat oven to 375F with rack in middle. Butter baking dish."
	s2 = "Peel and thinly slice potatoes into a large bowl and toss with butter. Spread potatoes in an even layer in the baking dish."
	s3 = "Put flour, 1 teaspoon salt, and 1/4 teaspoon pepper in a heavy medium saucepan and slowly whisk in milk until the mixture is smooth."
	s4 = "Bring milk mixture just to a boil over medium heat, whisking constantly (it will thicken slightly), and pour it over the potatoes. Cover pan tightly with foil and bake in oven until potatoes are tender, 35 to 40 minutes."
	s5 = "Remove foil and sprinkle with cheese, if using. Reset oven to broil and broil potatoes, about 4 to 5 inches from heat, until browned and bubbling, 2 to 3 minutes."
	steps = [s1, s2, s3, s4, s5]
	golden_scalloped_potatoes = c.create_recipe(name = 'golden scalloped potatoes', ingredients = ingredients, instructions = steps)
	api.add_recipe(golden_scalloped_potatoes)

	# fudge coffee brownies
	ingredients = [butter, chocolate, instant_espresso_powder, sugar, vanilla_extract, egg, flour, cinnamon, salt]
	s1 = "Preheat oven to 350F with rack in middle. Butter and flour a 13- by 9-inch baking pan."
	s2 = "Melt butter and chocolate with espresso powder in a 3-quart heavy saucepan over low heat, whisking until smooth. Remove from heat and cool to lukewarm. Whisk in sugar and vanilla. Whisk in eggs 1 at a time until mixture is glossy and smooth."
	s3 = "Whisk together flour, cinnamon, and salt, then whisk into chocolate mixture."
	s4 = "Spread batter in pan and bake until a wooden pick inserted in center comes out with crumbs adhering, 25 to 30 minutes. Cool completely before cutting."
	steps = [s1, s2, s3, s4]
	fudge_coffee_brownies = c.create_recipe(name = 'fudge coffee brownies', ingredients = ingredients, instructions = steps, tags = ['dessert'])
	api.add_recipe(fudge_coffee_brownies)

	# double chocolate mocha brownies
	ingredients = [butter, chocolate, sugar, instant_espresso_powder, vanilla_extract, salt, egg, flour, chocolate_chips]
	s1 = "Preheat oven to 375F. Line a 15- by 10- by 1-inch baking pan with foil, allowing 2 inches of foil to hang over ends of pan, and grease foil well (except overhang) with 1 tablespoon butter."
	s2 = "Melt remaining 11 tablespoons butter with unsweetened chocolate in a large metal bowl set over a pan of barely simmering water, stirring until smooth. Remove bowl from heat and whisk in sugar, espresso powder, vanilla, and salt (mixture will be grainy), then add eggs 1 at a time, whisking after each addition until batter is smooth."
	s3 = "Toss together flour and chocolate chips in another bowl and add to batter, stirring until just combined."
	s4 = "Spread batter evenly in baking pan and bake in middle of oven until top is firm and edges just begin to pull away from sides of pan, about 20 minutes (do not overbake)."
	s5 = "Cool in pan on a rack 5 minutes, then carefully lift brownies from pan by grasping both ends of foil and transfer to rack to cool 10 minutes more. Cut into 32 squares and lift brownies off foil with a spatula."
	steps = [s1, s2, s3, s4, s5]
	double_chocolate_mocha_brownies = c.create_recipe(name = 'double chocolate mocha brownies', ingredients = ingredients, instructions = steps, tags = ['dessert'])
	api.add_recipe(double_chocolate_mocha_brownies)

	# watermelon-lemonade ice pops
	ingredients = [watermelon, lemonade_concentrate, sugar]
	steps = ["Combine all ingredients in processor. Puree until very smooth. Divide mixture among 8 ice pop molds (each about 1/4 to 1/3 cup capacity). Cover and freeze until firm, at least 4 hours and up to 5 days."]	
	watermelon_lemonade_ice_pops = c.create_recipe(name = 'watermelon-lemonade ice pops', ingredients = ingredients, instructions = steps, tags = ['dessert'])
	api.add_recipe(watermelon_lemonade_ice_pops)

	# balsamic-strawberry pops
	ingredients = [strawberries, sugar, balsamic_vinegar]
	s1 = "Place the strawberries and sugar in a food processor and pulse just until the mixture is finely chopped and juicy but still chunky; you don't want a smooth puree. Transfer to a bowl and stir in the balsamic vinegar and a few grinds of pepper."
	s2 = "Spoon the mixture into ice pop molds and insert sticks. Freeze until firm, at least 6 hours or up to 1 week."
	s3 = "To unmold the pops, run hot water over the outsides of the molds for a few seconds, then gently pull the sticks."
	steps = [s1, s2, s3]
	balsamic_strawberry_pops = c.create_recipe(name = 'balsamic-strawberry pops', ingredients = ingredients, instructions = steps, tags = ['dessert'])
	api.add_recipe(balsamic_strawberry_pops)

	# green bean and lemon casserole
	ingredients = [green_beans, butter, olive_oil, lemon]
	s1 = "Bring a big pot of water to the boil, while you top and tail (trim) the beans. Once the water has come to the boil, salt it and cook the beans until they have lost their rawness (about 6 minutes after the water comes back to the boil), but retain a bit of crunch."
	s2 = "Strain them, and put the pot back on the stove over a low heat with the butter and olive oil. While the butter melts, chop up the lemon. Put it on a chopping board, cut a slice off each end, just enough to remove skin and pith, and then cut downwards, turning the lemon as you go, to peel the fruit fully. Don't worry if in order to remove all the pith you cut into the fruit a bit: just take the pieces of fruity peel over to the pan and squeeze in any juice you can. Then cut the lemon up on the board: I just slice and let each slice tumble into bits on its own. Add the lemon pieces and all the juice that collects to the melted butter and stir well with a wooden spoon, adding the drained beans."
	s3 = "Swirl the pan vigorously and turn the beans in the lemony butter. Add salt to taste and lots of freshly ground pepper. I love white pepper (out of deference to my mother's taste and practice) or the much-abominated 1980s restaurant-style mixed pepper, but neither is crucial."
	s4 = "Remove to a warmed casserole making sure you don't leave any lemony, buttery juices behind."
	steps = [s1, s2, s3, s4]
	green_bean_and_lemon_casserole = c.create_recipe(name = 'green bean and lemon casserole', ingredients = ingredients, instructions = steps)
	api.add_recipe(green_bean_and_lemon_casserole)

	count = 0


def insert_recent_recipes(api):
	fridgi = 'fridgi'
	chicken_penne_pasta = api.get_recipe_info('chicken penne pasta')
	sweet_peach_smoothie = api.get_recipe_info('sweet peach smoothie')
	basil_caesar_salad = api.get_recipe_info('basil caesar salad')
	fudge_coffee_brownies = api.get_recipe_info('fudge coffee brownies')
	watermelon_lemonade_ice_pops = api.get_recipe_info('watermelon-lemonade ice pops')
	
	api.update_recent_recipes(chicken_penne_pasta, fridgi)
	api.update_recent_recipes(sweet_peach_smoothie, fridgi)
	api.update_recent_recipes(basil_caesar_salad, fridgi)	
	api.update_recent_recipes(fudge_coffee_brownies, fridgi)
	api.update_recent_recipes(watermelon_lemonade_ice_pops, fridgi)

def reset_db(apiInstance):
	c = api.creator.ObjectCreator()
	# Clear previous test data
	apiInstance.clear_db()
	insert_some_recipes(apiInstance, c)
	insert_recent_recipes(apiInstance)


