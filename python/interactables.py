from cgitb import text
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider

from my_events import EventsManager
from themes import ThemeManager

#region Labels And Inputs
class CustomLabel(Label):
    def __init__(self, text_as_string = "", **kwargs):
        super().__init__(**kwargs)
        if text_as_string != "": self.text = text_as_string
        self.font_size = ThemeManager.default_font_size()

class CustomInput(TextInput): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = ThemeManager.default_font_size()

class RecipeInput(CustomInput): pass
#endregion

#region Hoverables And Buttons
class HoverableItem(HoverBehavior): 
    selected = False
    not_selected_default_background_colour = (1, 0, 0, 0.25)
    not_selected_on_hover_bacgkround_colour = (1, 0, 0, 0.5)
    selected_default_background_colour = (1, 0, 0, 0.75)
    selected_on_hover_background_colour = (1, 0, 0, 1)

    def on_enter(self, *args):
        """Called by HoverBehaviour when mouse enters object, used to change colour to show interactability"""
        if self.selected: self.background_color = self.selected_on_hover_background_colour
        else: self.background_color = self.not_selected_on_hover_bacgkround_colour

    def on_leave(self, *args):
        """Called by HoverBehaviour when mouse exits object, used to revert colour to default"""
        if self.selected: self.background_color = self.selected_default_background_colour
        else: self.background_color = self.not_selected_default_background_colour

    def set_if_selected(self, selected):
        self.selected = selected
        self.on_leave(None) 

class CustomButton(Button, HoverableItem): pass

class CustomIconButton(Button, HoverableItem): 
    def __init__(self, action, image_source, **kwargs):
        super().__init__(**kwargs)
        self.action = action
        self.ids.button_image.source = image_source

class ContentsPageButton(CustomButton):  
    not_selected_default_background_colour = ThemeManager.contents_button_not_hovered_not_selected_colour()
    not_selected_on_hover_bacgkround_colour = ThemeManager.contents_button_hovered_not_selected_colour()
    selected_default_background_colour = ThemeManager.contents_button_not_hovered_selected_colour()
    selected_on_hover_background_colour = ThemeManager.contents_button_hovered_selected_colour()

    recipe = None

    def __init__(self, recipe, **kwargs):
        super().__init__(**kwargs)
        self.recipe = recipe
        self.text = f"   {recipe.name}"

    def on_click(self):
        EventsManager.get_my_events().contents_button_pressed(self.recipe)

class FloatingButton(CustomIconButton): 
    not_selected_default_background_colour = ThemeManager.floating_button_not_hovered_not_selected_colour()
    not_selected_on_hover_bacgkround_colour = ThemeManager.floating_button_hovered_not_selected_colour()
    selected_default_background_colour = ThemeManager.floating_button_not_hovered_selected_colour()
    selected_on_hover_background_colour = ThemeManager.floating_button_hovered_selected_colour()

    def on_click(self):
        EventsManager.get_my_events().hover_button_pressed(self)
    
class FloatingButtonContainer(MDBoxLayout): 
    """Widget that contains the individual hover buttons, buttons needed sent through on init"""
    def __init__(self, buttons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for button in buttons: 
            self.ids.buttons_ins_point.add_widget(button)

class CustomSlider(Slider): pass

class SettingsSlider(CustomSlider):
    action = "unset"

    def on_touch_move(self, touch):
        EventsManager.get_my_events().settings_slider_changed(self.action, self.value)
        return super().on_touch_move(touch)
    
    def on_touch_up(self, touch):
        EventsManager.get_my_events().settings_slider_changed(self.action, self.value)
        return super().on_touch_up(touch)
#endregion