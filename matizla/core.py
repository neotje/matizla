from time import sleep
from matizla import ui
from matizla import power

def run():
    ui.start(_after_ui_start)


def _after_ui_start():
    #sleep(3)

    ui.LoadingScreen.hide()
    ui.MainScreen.hide()
    power.HaltOnGPIO.enable()
    """ui.LoadingScreen.show_progres_bar()

    for i in range(20):
        ui.LoadingScreen.set_progress((1 + i) * (1/20))
        sleep(0.1)

    ui.switchToMain()"""
