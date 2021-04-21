import webview

def start():
    webview.create_window("matizla", html="<h1>Hello</h1>", width=800, height=480, resizable=False)
    webview.start()