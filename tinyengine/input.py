class InputListener():

    def on_key_down(self, key):
        return
    
    def on_key_up(self, key):
        return
    
    def on_key_held(self, key):
        return
    
    def on_mouse_down(self, pos, button):
        return
    
    def on_mouse_up(self, pos, button):
        return
    
    def on_mouse_clicked(self, pos, button):
        return

    def on_mouse_move(self, pos):
        return


class InputDispatcher():

    # Properties
    listeners : list[InputListener] = []
    key_repeat_interval = 0.1
    button_click_threshold = 0.1

    # Members
    _pressed_keys = dict()
    _pressed_buttons = dict()

    def __init__(self, repeat_interval : float):
        self.key_repeat_interval = repeat_interval

    def addListener(self, listener : InputListener):
        self.listeners.append(listener)

    def update(self, deltaTime : float):

        # Update held keys
        for k,v in self._pressed_keys.items():
            new_v = v + deltaTime
            while new_v > self.key_repeat_interval:
                for listener in self.listeners:
                    listener.on_key_held(k)
                new_v -= self.key_repeat_interval

            self._pressed_keys.update({k: new_v})

        # Update held buttons
        for k,v in self._pressed_buttons.items():
            new_v = v + deltaTime
            self._pressed_buttons.update({k: new_v})


    def on_key_down(self, key):
        self._pressed_keys[key] = 0
        for listener in self.listeners:
            listener.on_key_down(key)


    def on_key_up(self, key):
        self._pressed_keys.pop(key)
        for listener in self.listeners:
            listener.on_key_up(key)


    def on_mouse_down(self, pos, button):
        self._pressed_buttons[button] = 0
        for listener in self.listeners:
            listener.on_mouse_down(pos, button)


    def on_mouse_up(self, pos, button):
        buttonHoldTime = self._pressed_buttons.pop(button)
        doClick = buttonHoldTime <= self.button_click_threshold

        for listener in self.listeners:
            listener.on_mouse_up(pos, button)
            if doClick:
                listener.on_mouse_clicked(pos, button)


    def on_mouse_move(self, pos):
        for listener in self.listeners:
            listener.on_mouse_move(pos)