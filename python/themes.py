from ast import Set
from settings import SettingsManager

class ThemeManager():

    def page_bg_colour(): return "white"

    def floating_button_hovered_selected_colour(): return 0.3, 1, 0.3, 1
    def floating_button_hovered_not_selected_colour(): return 0.65, 1, 0.65, 1
    def floating_button_not_hovered_selected_colour(): return 0.4, 1, 0.4, 1
    def floating_button_not_hovered_not_selected_colour(): return 0.75, 1, 0.75, 1

    def contents_button_hovered_selected_colour(): return 0.75, 1, 0.75, 1
    def contents_button_hovered_not_selected_colour(): return 0.9, 1, 0.9, 1
    def contents_button_not_hovered_selected_colour(): return 0.8, 1, 0.8, 1
    def contents_button_not_hovered_not_selected_colour(): return 1, 1, 1, 1

    def content_spacing(): return 2
    def content_padding(): return 16

    def default_font(): return "caveat"
    def default_font_colour(): return 0,0,0, 1
    def cursor_colour(): return 0.75, 1, 0.75, 1

    def header_font_size(): return 48 * SettingsManager.get_font_size_multiplier()
    def default_font_size(): return 24 * SettingsManager.get_font_size_multiplier()