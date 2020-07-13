import pyglet

pyglet.resource.path = ['res']
pyglet.resource.reindex()

from game.director import GameDirector

CAPTION = "Caption"
WIDTH = 640
HEIGHT = 480

if __name__ == '__main__':
    window = GameDirector(width=WIDTH, height=HEIGHT, caption=CAPTION, resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
