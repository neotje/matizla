from flask.helpers import send_from_directory
from matizla.assets import LoadingScreen
from webview.window import Window
from matizla.api import MatizlaWebApi
import webview
import platform
from time import sleep
from flask import Flask, render_template

""" Main window flask stuff """
from matizla.assets import MainScreen

main_window_server = Flask(
    __name__,
    static_folder=MainScreen.__path__[0],
    template_folder=MainScreen.__path__[0],
    static_url_path=''
)
main_window_server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1


""" Loading window flask stuff """

loading_window_server = Flask(
    __name__,
    static_folder=LoadingScreen.__path__[0],
    template_folder=LoadingScreen.__path__[0],
    static_url_path=''
)
loading_window_server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1


@loading_window_server.route('/')
@main_window_server.route('/')
def loadingIndex():
    return render_template('index.html')


@main_window_server.after_request
@loading_window_server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


_api = MatizlaWebApi()


class MainScreen:
    WINDOW: Window = webview.create_window(
        "main",
        main_window_server,
        width=800,
        height=480,
        resizable=False,
        fullscreen=(platform.machine() == "armv7l"),
        on_top=False,
        js_api=_api
    )

    @staticmethod
    def hide():
        MainScreen.WINDOW.hide()

    @staticmethod
    def show():
        MainScreen.WINDOW.show()

    @staticmethod
    def fade_out():
        MainScreen.WINDOW.evaluate_js("fadeOut();")

    @staticmethod
    def fade_in():
        MainScreen.WINDOW.evaluate_js("fadeIn();")
        MainScreen.show()


class LoadingScreen:
    WINDOW: Window = webview.create_window(
        "load",
        loading_window_server,
        width=800,
        height=480,
        resizable=False,
        fullscreen=(platform.machine() == "armv7l"),
        on_top=True,
        transparent=False,
        js_api=_api
    )

    @staticmethod
    def show_progres_bar():
        LoadingScreen.WINDOW.evaluate_js("showProgressBar();")

    @staticmethod
    def hide_progress_bar():
        LoadingScreen.WINDOW.evaluate_js("hideProgressBar();")

    @staticmethod
    def set_progress(p: float):
        LoadingScreen.WINDOW.evaluate_js(f"progress = {p};")

    @staticmethod
    def get_progress() -> float:
        return float(LoadingScreen.WINDOW.evaluate_js("progress;"))

    @staticmethod
    def hide():
        LoadingScreen.WINDOW.hide()

    @staticmethod
    def show():
        LoadingScreen.WINDOW.show()

    @staticmethod
    def fade_out():
        LoadingScreen.WINDOW.evaluate_js("fadeOut();")

    @staticmethod
    def fade_in():
        LoadingScreen.WINDOW.evaluate_js("fadeIn();")
        LoadingScreen.show()


def switchToMain():
    LoadingScreen.fade_out()
    sleep(0.95)
    MainScreen.fade_in()


def switchToLoad():
    MainScreen.fade_out()
    sleep(0.95)
    LoadingScreen.fade_in()


def close():
    for w in webview.windows:
        w.destroy()


def start(func):
    MainScreen.WINDOW.closed += close
    LoadingScreen.WINDOW.closed += close

    webview.start(debug=True, func=func)
