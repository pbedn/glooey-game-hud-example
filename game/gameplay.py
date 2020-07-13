"""Transition to Scene can be used to draw objects, and generally init 
everything before entering Game State (for example GamePlay), 
where post processing is done."""

import pyglet
from pyglet.window import key

from .fsm import State


class GamePlay(State):
    def execute(self):
        if self.d.keys[key.R]:
            self.d.fsm.transition('toGAME')
        if self.d.keys[key.F10]:
            self.d.fsm.transition('toMENU')


class TransitionToGame(State):
    def __init__(self, to_state, *args):
        super().__init__(*args)
        self.to_state = to_state

    def execute(self):
        # initialize game objects, sprites etc.

        self.d.fsm.set_state('GAME')


class GameEnd(State):
    def execute(self):
        if self.d.keys[key.R]:
            self.d.fsm.transition('toGAME')
        if self.d.keys[key.F10]:
            self.d.fsm.transition('toMENU')


class TransitionToEnd(State):
    def __init__(self, to_state, *args):
        super().__init__(*args)
        self.to_state = to_state

    def execute(self):
        self.d.fsm.set_state('END')


class GameExit(State):
    def execute(self):
        pyglet.app.exit()


class TransitionToExit(State):
    def __init__(self, to_state, *args):
        super().__init__(*args)
        self.to_state = to_state

    def execute(self):
        self.d.fsm.set_state('EXIT')
