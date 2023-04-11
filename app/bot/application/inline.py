class InlineKeyboardButton:
    def __init__(
        self,
        text="",
        url="",
        callback_data="",
    ):
        self.text=text
        # Optionals
        self.url=url
        self.callback_data=callback_data
    @classmethod
    def de_json(cls, data):
        return cls(**data) 


class InlineKeyboardMarkup:
    def __init__(self, inline_keyboard):
        self.inline_keyboard = inline_keyboard
    @classmethod
    def de_json(cls, data): #ele passou o bot aqui tbm 
        
        keyboard = []
        for row in data["inline_keyboard"]:
            tmp = []
            for col in row:
                btn = InlineKeyboardButton.de_json(col)
                if btn:
                    tmp.append(btn)
            keyboard.append(tmp)

        update = cls(keyboard)
        return update

    def __iter__(self):
        keyboard = []
        for row in self.inline_keyboard:
            tmp = []
            for col in row:
                btn = col.__dict__
                if btn:
                    tmp.append(btn)
            keyboard.append(tmp)
        return keyboard

