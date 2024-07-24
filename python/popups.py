from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

from my_events import EventsManager

class PopupManager():
    current_popup = None

    @staticmethod
    def setup():
        """Called on app start, subscribes to events"""
        EventsManager.get_my_events().refresh_current_page += PopupManager.refresh_current_popup

    @staticmethod
    def refresh_current_popup():
        current_popup = PopupManager.current_popup
        if not current_popup: return
        if current_popup.title == "Settings": PopupManager.show_settings_popup()
        else: raise ValueError(f"You haven't coded in how to refresh this kind of popup: {current_popup.title}")
        
    @staticmethod
    def show_settings_popup():
        popup = CustomPopup("Settings")
        settings_popup_section = SettingsPopupSection()
        popup.add_section(settings_popup_section)
        PopupManager.__show_new_popup(popup)

    @staticmethod
    def __show_new_popup(popup_to_show):
        PopupManager.close_current_popup()
        popup_to_show.open()
        PopupManager.current_popup = popup_to_show

    @staticmethod
    def close_current_popup():
        current_popup = PopupManager.current_popup
        if not current_popup: return
        current_popup.dismiss()

class CustomPopup(Popup): 
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        print(self.title_size)

    def add_section(self, section):
        self.ids.content.add_widget(section)

class SettingsPopupSection(MDBoxLayout): pass
