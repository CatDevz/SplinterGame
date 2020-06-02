from splinter.scenes import AbstractScene
import curses
from splinter import __v__


class MainMenu(AbstractScene, runtime_scene=True):
    def __init__(self):
        self.selected = 0
        self.buttons = [
            {'text': 'Play', 'position': 0},
            {'text': 'Options', 'position': 1},
            {'text': 'About', 'position': 2},
            {'text': 'Exit', 'position': 4}
        ]

    def __call__(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)

    def draw(self, window):
        window.clear()
        window.addstr(1, 2, '   _____ ____  __    _____   __________________  ')
        window.addstr(2, 2, '  / ___// __ \/ /   /  _/ | / /_  __/ ____/ __ \ ')
        window.addstr(3, 2, '  \__ \/ /_/ / /    / //  |/ / / / / __/ / /_/ / ')
        window.addstr(4, 2, ' ___/ / ____/ /____/ // /|  / / / / /___/ _, _/  ')
        window.addstr(5, 2, '/____/_/   /_____/___/_/ |_/ /_/ /_____/_/ |_|   ')

        for btn in self.buttons:
            window.addstr(7+btn['position'], 2, btn['text'], curses.color_pair(2) if self.buttons[self.selected] == btn else curses.color_pair(0))

    def input(self, key):
        if key == curses.KEY_UP:
            if self.selected == 0:
                self.selected = len(self.buttons)-1
            else:
                self.selected -= 1
        elif key == curses.KEY_DOWN:
            if self.selected == len(self.buttons)-1:
                self.selected = 0
            else:
                self.selected += 1
        elif key == 10:
            if self.selected == 3:
                __v__.running = False