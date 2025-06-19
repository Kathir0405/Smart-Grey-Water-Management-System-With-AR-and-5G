from kivy.app import App
from kivy.uix.webview import WebView

class FlaskApp(App):
    def build(self):
        webview = WebView(url='http://127.0.0.1:5000')
        return webview

FlaskApp().run()
