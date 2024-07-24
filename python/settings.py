from my_events import EventsManager

class SettingsManager():
    font_setting_slider = 1

    #There is a reason this is a function and not just a var, cant remember why but don't change it 
    def get_font_size_multiplier(): return SettingsManager.font_setting_slider * 0.2 + 1

    @staticmethod
    def setup():
        """Called on app initialisation, subscribes to events"""
        EventsManager.get_my_events().settings_slider_changed += SettingsManager.settings_slider_changed
    
    @staticmethod
    def settings_slider_changed(setting, value):
        """Called as event on touch_move and touch_up on settings slider"""
        if setting == "text_size": 
            SettingsManager.font_setting_slider = value
            EventsManager.get_my_events().refresh_current_page()
        else: raise ValueError(f"You haven't coded in what to do with this kind of settings slider: {setting}")