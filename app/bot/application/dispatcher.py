from .utils import CallbackContext

class Bot:
    def __init__(
        self,
        token: str,
        base_url: str = "https://api.telegram.org/bot",
        # request: BaseRequest = None,
        # get_updates_request: BaseRequest = None,
        # private_key: bytes = None,
        # private_key_password: bytes = None,
        # local_mode: bool = False,
    ):
        if not token:
            raise ValueError("You must pass the token you received from https://t.me/Botfather!")
        
        self.token = token
        self.data = False
        self.base_url = base_url

    def sendMessage(self, chat_id, text, parse_mode="Markdown", reply_markup=None):
        import requests

        url = '{}{}/{}'.format(self.base_url, self.token, "sendMessage")
        
        self.data = {
            "chat_id": chat_id, 
            "text": text, 
            "parse_mode": parse_mode,
            "reply_markup": reply_markup, 
        }
        self.response = requests.post(url, self.data, verify=False)

    def delete_message(self):
        pass


# todo callback eu adiciono no db quando ele for chamado

class Dispatcher:
    def __init__(self, bot, context=CallbackContext):
        self.handlers = {}
        self.bot = bot
        self.context = context

    def add_handler(self, handler):
        self.handlers.setdefault(handler.__class__.__name__ , []).append(handler)

    def add_handlers(self, handlers):
        for handler in handlers:
            self.handlers.setdefault(handler.__class__.__name__ , []).append(handler)

    def handle_conversation_update(self, conversation_context, update):
        
        temp_handlers = self.handlers

        conversation = next( 
            (item for item in self.handlers["ConversationHandler"] if item.name == conversation_context[0].name),
            False,
        )

        if conversation:
            conversation.toggle_conversation() #apagando o registro da conversa apra nao entrar em loop
            self.handlers = {}
            self.add_handlers(conversation.states)
            self.process_update(update)
        
        self.handlers = temp_handlers

    def process_update(self, update):
        import itertools
        from bot.models import ConversationContext
        self.context = self.context.from_update(self, update) #atualizando o context com o novo carinha. 

        print('to aqui no process')
        #AJUSTE PARA ELE PEGAR TODOS OS QUE ESTAO DENTRO DAS CONVERSAS. FUNCIONA BEM. 
        conversation_context = ConversationContext.objects.all()
        print('Conversation? ', conversation_context)
        if conversation_context:
            self.handle_conversation_update(conversation_context, update)

        else:            
            handler = next(
                (item for item in list(itertools.chain(*self.handlers.values())) if item.check_update(update)),
                False                                             
            )
            if handler:
                print(handler, ' vendo o handler')
                handler.handle_update(update, self.context)
            
        return 
    