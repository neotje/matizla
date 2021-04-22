from typing import List
import webview
from webview import Window
from matizla import ui


def get_by_uuid_window(uuid: str) -> Window:
    for w in webview.windows:
        if w.uuid == uuid:
            return w

def get_window_by_title(title: str) -> Window:
    for w in webview.windows:
        if w.title == title:
            return w

class MatizlaWebApi:
    def __init__(self) -> None:
        pass

    def showWindow(self, title: str):
        w = get_window_by_title(title)

        if w is not None:
            w.show()

    def hideWindow(self, title: str):
        w = get_window_by_title(title)

        if w is not None:
            w.hide()

    def fadeInMainWindow(self):
        ui.MainScreen.fade_in()

    def windowList(self) -> List:
        r = []

        for w in webview.windows:
            r.append({
                'uid': w.uid,
                'title': w.title,
                'hidden': w.hidden
            })

        return r
