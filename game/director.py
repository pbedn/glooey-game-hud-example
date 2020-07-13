import pyglet
import glooey

from pyglet.window import key, mouse, FPSDisplay

from .gameplay import GamePlay, GameEnd, TransitionToGame, TransitionToEnd, GameExit, TransitionToExit
from .menu import GameMenu, TransitionToMenu, GameOptions, TransitionToOptions
from .fsm import FSM


class GameDirector(pyglet.window.Window):
    """
    Game Director managing all actions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(50, 50)  # location of upper left window corner
        self.batch = pyglet.graphics.Batch()
        self.group = pyglet.graphics.Group()
        # self.set_mouse_visible(False)
        self.frame_rate = 1/60.
        self.fps_display = FPSDisplay(self)

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.gui = glooey.Gui(self, batch=self.batch, group=self.group)

        # Set GAME Finite State Machine states and transitions
        self.fsm = FSM()
        self.fsm.states['MENU'] = GameMenu(self)
        self.fsm.states['GAME'] = GamePlay(self)
        self.fsm.states['OPTIONS'] = GameOptions(self)
        self.fsm.states['END'] = GameEnd(self)
        self.fsm.states['EXIT'] = GameExit(self)
        self.fsm.transitions['toMENU'] = TransitionToMenu('MENU', self)
        self.fsm.transitions['toGAME'] = TransitionToGame('GAME', self)
        self.fsm.transitions['toOPTIONS'] = TransitionToOptions('OPTIONS', self)
        self.fsm.transitions['toEND'] = TransitionToEnd('END', self)
        self.fsm.transitions['toEXIT'] = TransitionToEnd('EXIT', self)

        self.fsm.transition('toMENU')

    def on_key_press(self, symbol, modifiers):
        """Global key shortcuts"""
        if symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def update(self, dt):
        self.fsm.execute()
