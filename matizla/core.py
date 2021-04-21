from time import sleep
from matizla import ui

def run():
    ui.start(_after_ui_start)

def _after_ui_start():
    ui.LOAD_WINDOW.show()

    sleep(5)

    #ui.LOAD_WINDOW.hide()