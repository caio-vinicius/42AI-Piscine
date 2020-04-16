cookbook = {
        'salad': {
            'ingredients': ['Avocado', 'Arugula', 'Tomatoes', 'Spinach'],
            'meal': 'lunch',
            'prep_time': '15',
        }, 
        'cake': {
            'ingredients': ['Flour', 'Sugar', 'Eggs'],
            'meal': 'dessert',
            'prep_time': '60',
        },
        'sandwich': {
            'ingredients': ['Ham', 'Bread', 'Cheese', 'Tomatoes'],
            'meal': 'lunch',
            'prep_time': '10',
            
        } 
    }

def getRecipes():
    try: 
        for recipe in cookbook:
            print (recipe.title())
        return 1
    except:
        return 0

def getRecipeInfo(name):
    try:
        for recipe, recipe_info in cookbook.items():
            if recipe == name:
                print (recipe_info)
        return 1
    except:
        return 0

def delRecipe(name):
    try:
        del cookbook[name]
        return 1
    except:
        return 0

def addRecipe(name, meal, prep_time, *ingredients):
    try:
        cookbook[name] = {
                    'ingredients': ingredients[0],
                    'meal': meal,
                    'prep_time': prep_time
                }
        return 1
    except:
        return 0

#switcher = {
#        1: addRecipe("cafe", "drink", "Water", "Coffe"),
#        2: delRecipe("cafe"),
#        3: getRecipeInfo("salad"),
#        4: getRecipes(),
#        5: "",
#    }

option = 0

option = input("Please select a option by type the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n> ")

#for key, value in switcher.items():
#    if key == int(option):
#        print ("value:", value)

if option == '1':
    name = input("Name of recipe:\n>> ")
    ingredients = list(input("Enter ingredients (separate with spaces):\n>> ").split())
    meal = input("Name of meal:\n>> ")
    prep_time = int(input("Preparation time (minutes):\n>> "))
    
    addRecipe(name, meal, prep_time, ingredients)
elif option == '2':
    name = input("Name of recipe to delete:\n>> ")
    delRecipe(name)
elif option == '3':
    name = input("Name of recipe:\n>> ")
    getRecipeInfo(name)
elif option == '4':
    getRecipes()
elif option == '5':
    print ("Closed")
    pass
else:
    print ("This option isn't valid, try something else.")

