from popups import PopupManager
from recipes import RecipeManager
from recipes import Recipe
from pages import ContentsPage
from pages import RecipePage
from my_events import EventsManager
from interactables import FloatingButton
from interactables import FloatingButtonContainer

class UIManager():
    __root = None
    __current_page = None
    __hover_button_container = None
    __edit_button = None

    @staticmethod
    def setup(root): 
        """Called on app initialisation, subscribes to events and sets up UI"""
        EventsManager.get_my_events().contents_button_pressed += UIManager.show_recipe_page
        EventsManager.get_my_events().hover_button_pressed += UIManager.hover_button_pressed
        EventsManager.get_my_events().refresh_current_page += UIManager.refresh_current_page
        
        UIManager.__root = root
        UIManager.show_contents_page()

    @staticmethod
    def refresh_current_page():
        """Called on change of things like font size to show updated size"""
        current_page = UIManager.__current_page        
        if current_page.page_type == "Contents": UIManager.__set_new_page(ContentsPage(RecipeManager.get_chapters_and_recipes()))
        elif current_page.page_type == "Recipe": UIManager.__set_new_page(RecipePage(current_page.recipe))
        else: raise ValueError(f"You haven't coded in how to refresh this kind of page: {current_page.page_type}")

    @staticmethod
    def show_contents_page():
        """Shows contents page"""
        UIManager.__set_new_page(ContentsPage(RecipeManager.get_chapters_and_recipes()))
    
    @staticmethod
    def show_recipe_page(recipe):
        """Shows recipe page"""
        UIManager.__set_new_page(RecipePage(recipe))

    @staticmethod
    def try_save_current_recipe():
        "This is called every time a hover button is pressed, it checks if the original page was a recipe page and if so saves it in case it was edited"
        current_page = UIManager.__current_page
        if current_page.page_type != "Recipe": return
        edited_recipe = current_page.get_edited_page_as_recipe()
        RecipeManager.edit_recipe(current_page.recipe, edited_recipe)
        UIManager.show_recipe_page(edited_recipe)

    @staticmethod
    def __set_new_page(new_page):
        """Once the type of page has been worked out, this is called to remove old page and add new one"""
        current_page = UIManager.__current_page
        if (current_page): UIManager.__root.remove_widget(current_page)
        UIManager.__root.add_widget(new_page)
        UIManager.__current_page = new_page
        UIManager.__set_hover_buttons()
    
    @staticmethod
    def __set_hover_buttons():
        """Works out which of the hover buttons should be displayed, i.e. next page, home button, new, edit"""
        if UIManager.__hover_button_container: UIManager.__root.remove_widget(UIManager.__hover_button_container)
        UIManager.__edit_button = None
        
        buttons = []
        current_page = UIManager.__current_page
        buttons.append(FloatingButton("settings", "../images/settings.png"))
        if current_page.page_type == "Recipe":
            edit_button = FloatingButton("edit_recipe", "../images/edit.png")
            UIManager.__edit_button = edit_button
            buttons.append(edit_button)
            buttons.append(FloatingButton("delete_recipe", "../images/bin.png"))
            buttons.append(FloatingButton("new_recipe", "../images/add_new.png"))
            buttons.append(FloatingButton("home", "../images/home.png"))
        else:
            buttons.append(FloatingButton("new_recipe", "../images/add_new.png"))
        hover_button_container = FloatingButtonContainer(buttons)
        UIManager.__root.add_widget(hover_button_container)
        UIManager.__hover_button_container = hover_button_container

    @staticmethod
    def hover_button_pressed(button):

        action = button.action
        current_page = UIManager.__current_page
        recipe = None if current_page.page_type != "Recipe" else current_page.recipe

        if action == "home":
            UIManager.try_save_current_recipe()
            UIManager.show_contents_page()
        elif action == "new_recipe":
            UIManager.try_save_current_recipe()
            new_recipe = Recipe("","","","")
            RecipeManager.add_new_recipe(new_recipe)
            UIManager.show_recipe_page(new_recipe)
            UIManager.__current_page.set_editable()
            UIManager.set_edit_button_active(True)
        elif action == "edit_recipe":
            if current_page.page_type != "Recipe": return
            current_page.set_editable()
            UIManager.set_edit_button_active(current_page.get_if_editable())
        elif action == "delete_recipe":
            if not recipe: return
            RecipeManager.remove_recipe(recipe)
            UIManager.show_contents_page()
        elif action == "settings":
            UIManager.try_save_current_recipe()
            PopupManager.show_settings_popup()
        
        else: print(f"You haven't coded in hover button: {action}")
    
    @staticmethod
    def set_edit_button_active(active):
        edit_button = UIManager.__edit_button
        if not edit_button: return
        edit_button.set_if_selected(active)