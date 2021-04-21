from typing import List
import webview
from webview import Window
from matizla import ui


def get_by_uuid_window(uuid: str) -> Window:
    for w in webview.windows:
        if w.uuid == uuid:
            return Window


class MatizlaWebApi:
    def __init__(self) -> None:
        pass

    def showWindow(self, uuid: str):
        w = get_by_uuid_window(uuid)

        if w is not None:
            w.show()

    def hideWindow(self, uuid: str):
        w = get_by_uuid_window(uuid)

        if w is not None:
            w.hide()

    def windowList(self) -> List:
        r = []

        for w in webview.windows:
            r.append({
                'uid': w.uid,
                'title': w.title,
                'hidden': w.hidden
            })

        return r
