import tinyengine

class Label(tinyengine.Entity):

    def __init__(self, x=0, y=0, width=150, height=50, text="", textSize = 30):

        self._textRenderer = tinyengine.TextRenderer()

        super().__init__(x, y, [self._textRenderer])