import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

kivy.require("1.10.0")

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')
Config.set('graphics', 'fullscreen', '0')
Config.write()


class AppLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class QuadApp(App):
    def build(self):
        app_layout = AppLayout()
        grid_layout = GridLayout(cols=1, size_hint=(1, 1))
        b = Button(text="hello")
        grid_layout.add_widget(b)
        app_layout.add_widget(grid_layout)
        return app_layout


organizerApp = QuadApp()
organizerApp.run()
