import curses, time, threading
from splinter.scenes.menu import MainMenu
from splinter import __v__


def main():
    global win, stdscr, options, scene

    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        curses.curs_set(0)
        win = curses.newwin(curses.LINES-1, curses.COLS-1, 0, 0)

        InputThread()
        scene = MainMenu()
        scene()
        while __v__.running:
            scene.draw(win)
            win.refresh()
            time.sleep(0.025)
    finally:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.curs_set(1)
        curses.endwin()


# Input Thread
class InputThread(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        global win, stdscr, selected, scene, ltime
        while True:
            input = stdscr.getch()
            if input == curses.KEY_HOME:
                __v__.running = False
            scene.input(input)


if __name__ == "__main__":
    main()