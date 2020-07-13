"""Some elements are using default settings and few are specified from
'kenney' theme, from glooey package."""

import pyglet
import glooey
from glooey.themes.kenney import BigLabel, HBox, GreyRadioButton
from .fsm import State

###################
# MAIN MENU
###################

class StartLabel(BigLabel):
    custom_top_padding = 80
    custom_text = "Start Game"
    custom_alignment = "center"
    custom_font_size = 40

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.fsm.transition('toGAME')

    def on_mouse_enter(self, x, y):
        self.font_size = self.custom_font_size + 5

    def on_mouse_leave(self, x, y):
        self.font_size = self.custom_font_size


class OptionsLabel(BigLabel):
    custom_text_alignment = "center"
    custom_text = "Options"
    custom_alignment = "center"
    custom_font_size = 40

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.fsm.transition('toOPTIONS')

    def on_mouse_enter(self, x, y):
        self.font_size = self.custom_font_size + 5

    def on_mouse_leave(self, x, y):
        self.font_size = self.custom_font_size


class ExitLabel(BigLabel):
    custom_top_padding = -80
    custom_text = "Exit"
    custom_alignment = "center"
    custom_font_size = 40

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.fsm.transition('toEXIT')

    def on_mouse_enter(self, x, y):
        self.font_size = self.custom_font_size + 5

    def on_mouse_leave(self, x, y):
        self.font_size = self.custom_font_size


class GameMenu(State):
    def __init__(self, *args):
        super().__init__(*args)

    def execute(self):
        pass


class TransitionToMenu(State):
    def __init__(self, to_state, *args):
        super().__init__(*args)
        self.to_state = to_state

    def execute(self):
        """Draw Main Menu"""

        self.d.gui.clear()
        vbox = glooey.VBox()
        self.d.gui.add(vbox)

        hbox = HBox()
        hbox2 = HBox()
        hbox3 = HBox()
        vbox.add(hbox)
        vbox.add(hbox2)
        vbox.add(hbox3)

        hbox.add(StartLabel())
        hbox2.add(OptionsLabel())
        hbox3.add(ExitLabel())

        self.d.fsm.set_state('MENU')


###################
# OPTIONS MENU
###################


class OptionsTitleLabel(BigLabel):
    custom_top_padding = 80
    custom_text = "Options"
    custom_alignment = "center"
    custom_font_size = 30


class DifficultyLabel(BigLabel):
    custom_text_alignment = "center"
    custom_font_size = 25
    modes = {'easy': 'Easy Mode',
             'hard': 'Hard Mode'}
    current_mode = 'easy'
    custom_text = modes[current_mode]

    def on_mouse_press(self, x, y, button, modifiers):
        self.select_next_mode()

    def select_next_mode(self):
        if self.current_mode == 'easy':
            self.text = self.modes['hard']
            self.current_mode = 'hard'
        else:
            self.text = self.modes['easy']
            self.current_mode = 'easy'
        self.window.current_mode = self.current_mode


class OptionsBackLabel(BigLabel):
    custom_top_padding = -80
    custom_text = "Back"
    custom_alignment = "center"
    custom_font_size = 30

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.fsm.transition('toMENU')

    def on_mouse_enter(self, x, y):
        self.font_size = self.custom_font_size + 5

    def on_mouse_leave(self, x, y):
        self.font_size = self.custom_font_size


class GameOptions(State):
    def execute(self):
        pass


class TransitionToOptions(State):
    def __init__(self, to_state, *args):
        super().__init__(*args)
        self.to_state = to_state

    def execute(self):
        """Draw Options Menu"""
        
        self.d.gui.clear()
        vbox = glooey.VBox()
        self.d.gui.add(vbox)

        hbox = HBox()
        hbox2 = HBox()
        hbox3 = HBox()
        vbox.add(hbox)
        vbox.add(hbox2)
        vbox.add(hbox3)

        hbox.add(OptionsTitleLabel())
        hbox2.add(DifficultyLabel())
        hbox3.add(OptionsBackLabel())

        self.d.fsm.set_state('OPTIONS')
