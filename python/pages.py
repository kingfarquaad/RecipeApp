from msilib import MSIDBOPEN_CREATE
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import BaseButton
from interactables import CustomLabel
from interactables import ContentsPageButton
from interactables import RecipeInput
from recipes import Recipe
from themes import ThemeManager

class Page(MDFloatLayout): 
    page_type = "Undefined"
    __contents_section = None

class ContentsPage(Page): 
    page_type = "Contents"

    def __init__(self, chapters_and_recipes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        contents_section = ContentsPageSection(chapters_and_recipes)
        self.__contents_section = contents_section
        self.ids.page_section_ins_point.add_widget(contents_section)

class ContentsPageSection(MDGridLayout):
    def __init__(self, chapters_and_recipes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for chapter in chapters_and_recipes:
            chapter_name = CustomLabel(chapter)
            chapter_name.bold = True
            self.add_widget(chapter_name)
            recipes = chapters_and_recipes[chapter]
            for recipe in recipes:
                button = ContentsPageButton(recipe)
                self.add_widget(button)

class RecipePage(Page):
    page_type = "Recipe"

    def __init__(self, recipe, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipe = recipe
        self.__editable = False
        contents_section = RecipePageSection(recipe)
        self.__contents_section = contents_section
        self.ids.page_section_ins_point.add_widget(contents_section)
    
    def set_editable(self):
        editable = not self.__editable
        self.__editable = editable
        cursor_colour = ThemeManager.cursor_colour() if editable else (0, 0, 0, 0)
        recipe_section = self.__contents_section
        for child in recipe_section.children:
            if not isinstance(child, RecipeInput): continue
            child.cursor_color = cursor_colour
            child.readonly = not editable
        
        recipe_section.ids.recipe_name.focus = True

    def get_if_editable(self): return self.__editable
    
    def get_edited_page_as_recipe(self):
        """This returns the page as is, as a recipe - this is how you get the edited version of the recipe"""
        recipe_section = self.__contents_section
        recipe_name = recipe_section.ids.recipe_name.text
        chapter = recipe_section.ids.recipe_chapter.text
        ingredients = recipe_section.ids.recipe_ingredients.text
        method = recipe_section.ids.recipe_method.text
        new_recipe = Recipe(
            recipe_name,
            chapter,
            ingredients,
            method
        )
        return new_recipe

class RecipePageSection(MDGridLayout):
    def __init__(self, recipe, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.recipe_name.text = recipe.name if recipe.name != "Unnamed Recipe" else ""
        self.ids.recipe_chapter.text = recipe.chapter if recipe.chapter != "Other" else ""
        self.ids.recipe_ingredients.text = recipe.ingredients
        self.ids.recipe_method.text = recipe.method