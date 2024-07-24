
from save_load import SaveLoadManager

class RecipeManager():
    __chapters_and_recipes = {}

    @staticmethod
    def get_chapters_and_recipes(): return RecipeManager.__chapters_and_recipes

    @staticmethod
    def load_recipes(): 
        """Called at application initialisation, loads preexisting recipes from save load manager"""
        RecipeManager.__chapters_and_recipes = SaveLoadManager.load()

    @staticmethod
    def save_recipes(): 
        """Saves all recipes"""
        SaveLoadManager.save(RecipeManager.__chapters_and_recipes)

    @staticmethod 
    def add_new_recipe(recipe):
        """Potentially creates new chapter key in chapters dict for recipe chapter, then adds recipe to list that is the value to that key"""
        if recipe.name == "": recipe.name = "Unnamed Recipe"
        if recipe.chapter == "": recipe.chapter = "Other"
        chapters_and_recipes = RecipeManager.__chapters_and_recipes
        chapter = recipe.chapter
        if chapter not in chapters_and_recipes: 
            chapters_and_recipes[chapter] = [recipe]
        else: chapters_and_recipes[chapter].append(recipe)
        recipes = chapters_and_recipes[chapter]
        """This sorts the chapters and recipes into alphabetical order
            ToDo: MOVE THIS TO UI MANAGER SO IT JUST SHOWS THEM ALPHABETICALLY"""
        recipes = sorted(chapters_and_recipes[chapter],
                         key = lambda x: x.name)
        chapters_and_recipes[chapter] = recipes
        RecipeManager.save_recipes()

    @staticmethod
    def edit_recipe(original_recipe, edited_recipe):
        """Edits recipe, either replacing the old recipe if same chapter, or removing old and creating new if not"""
        RecipeManager.remove_recipe(original_recipe)
        RecipeManager.add_new_recipe(edited_recipe)
        RecipeManager.save_recipes()

    @staticmethod 
    def remove_recipe(recipe):
        """Removes recipe from recipe list and chapter list. If chapter now contains 0 recipes, also remove the chapter from chapter list"""
        chapters = RecipeManager.__chapters_and_recipes

        chapter = recipe.chapter
        if chapter not in chapters: raise NotImplementedError("Tried to remove recipe but couldn't find it's chapter")
        recipes = chapters[chapter]
        if recipe not in recipes: raise NotImplementedError("Tried to remove recipe but couldn't find it in recipes")

        recipes.remove(recipe)
        if len(recipes) == 0: del RecipeManager.__chapters_and_recipes[chapter]
        else: RecipeManager.__chapters_and_recipes[chapter] = recipes
        RecipeManager.save_recipes()
        
    @staticmethod
    def debug_print_all_recipes():
        """Debug method for printing all recipes in readable format"""
        for chapter in RecipeManager.__chapters_and_recipes:
            print (f"   Chapter: {chapter}")
            for recipe in RecipeManager.__chapters_and_recipes[chapter]:
                print (f"      Recipe: {recipe.name}")

class Recipe():
    def __init__(self, name, chapter, ingredients, method) -> None:
        self.name = name
        self.chapter = chapter
        self.ingredients = ingredients
        self.method = method