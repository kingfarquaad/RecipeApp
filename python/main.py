from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase

from popups import PopupManager
from ui import UIManager
from recipes import RecipeManager
from settings import SettingsManager

Builder.load_file('../kv/pages.kv')
Builder.load_file('../kv/interactables.kv')
Builder.load_file('../kv/popups.kv')

LabelBase.register(name='caveat',   fn_regular='../fonts/caveat.regular.ttf',
                                    fn_bold='../fonts/caveat.bold.ttf')

class RecipeApp(MDApp):
    title = 'RecipieApp'

    def build(self):
        """Called on app init by MDKivy"""
        self.icon = '../images/icon.ico'
        root = FloatLayout()
        RecipeManager.load_recipes()
        UIManager.setup(root)
        SettingsManager.setup()
        PopupManager.setup()
        return root

    def on_stop(self):
        """Called on app close"""
        UIManager.try_save_current_recipe()

if __name__ in ('__main__', '__android__'):
    RecipeApp().run()