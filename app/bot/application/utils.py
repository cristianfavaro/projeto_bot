class Handler: 
    def check_update(self, update):
        if update.message:
            if update.message.entities:
                if "type" in update.message.entities[0]:
                    if update.message.entities[0]["type"] == "bot_command":
                        print(f"São iguais? {self.command} - {update.message.text.replace('/', '')}")
                        return self.command == update.message.text.replace("/", "")    
                    
    def handle_update(self, update, context):
        if getattr(self, "func", False): 
            self.func(update, context)
        else: 
            for entry_point in self.entry_points:
                entry_point.func(update, context)


class ConversationHandler(Handler):
    def __init__(self, name, entry_points, states, fallbacks=[]):
        self.name=name
        self.entry_points=entry_points
        self.states=states

    def __str__(self):
        return f"Conversation: {self.name}"

    def toggle_conversation(self):
        #toggle conversation. Ele adiciona e tira quando termina. 
        #aqui eu defino o que ele faz. 
        from bot.models import ConversationContext
        conversation, created = ConversationContext.objects.get_or_create(
            name=self.name
        )

        if not created:
            conversation.delete()

    def check_update(self, update):
        for entry_point in self.entry_points:
            checked = entry_point.check_update(update)
            if checked:
                self.toggle_conversation()
                return checked
            

class CallbackContext:
    def __init__(self, dispatcher, update):
        self.dispatcher = dispatcher
        self.update = update

    @classmethod
    def from_update(cls, dispatcher, update):
        update = cls(dispatcher, update)      
        return update
    

class CallbackQuery:
    def de_json(self, update=None):
        return None


class CommandHandler(Handler):
    def __init__(self, command, func):
        self.command = command
        self.func = func 

    def __str__(self):
        return f"Commando: /{self.command}"


class Message:

    def __init__( self,
        data, 
        bot,
    ):
        self.__dict__.update(**data)
        self.bot = bot
        # self.message_id = message_id
        # self.date = date
        # self.from_user = from_user
        # self.text = text


    @classmethod
    def de_json(cls, update, bot): # eu tirei o bot daqui// bot
        """See :meth:`telegram.TelegramObject.de_json`."""
        if not update:
            return
        data = {
            "date": update.get("date"),
            "message_id": update.get("message_id"),
            "from_user": update.get("from"), #User.de_json(data.pop("from", None), bot)
            "entities": update.get("entities"),      
            "chat": update.get("chat"),
        }
        data["text"] =  update.get("text")

        # data["reply_markup"] = InlineKeyboardMarkup.de_json(data.get("reply_markup"), bot)      

        return Message(data, bot) # tirei o bot daqui tbm bot=bot

    def reply_text(self, text, reply_markup=None, parse_mode="Markdown"):
        self.bot.sendMessage(self.chat.get("id"), text, reply_markup=reply_markup)


