from events import Events

class MyEvents(Events):
    __events__ = (
    "contents_button_pressed",
    "hover_button_pressed",
    "settings_slider_changed",
    "refresh_current_page",
    
    )

class EventsManager():
    my_events = MyEvents()

    def get_my_events(): return EventsManager.my_events