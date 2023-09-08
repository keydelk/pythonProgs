from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.size_hint = (.5, .5)


class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton(
                     text="Funky Button",
                     pos=(20, 20)
                     )


if __name__ == '__main__':
    LanguageLearnerApp().run()
