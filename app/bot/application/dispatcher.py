import datetime
import json
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

    def sendMessage(self, chat_id, text, parse_mode="Markdown"):
        import requests

        url = '{}{}/{}'.format(self.base_url, self.token, "sendMessage")
        
        self.data = {
            "chat_id": chat_id, 
            "text": text, 
            "parse_mode": parse_mode,
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
        print('avaliando os handlers de conversa ', self.handlers)
        conversation = next( 
            (item for item in self.handlers["ConversationHandler"] if item.name == conversation_context[0].name),
            False,
        )
        if conversation:
            print('passei aqui no conversation')
            conversation.toggle_conversation() #apagando o registro da conversa apra nao entrar em loop
            self.handlers = {}
            print(' vendos e apagou os handlers', self.handlers)
            self.add_handlers(conversation.states)
            return self.process_update(update)

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
        #aqui eu acho que posso tratar os erros e tratar o smalltalk.


            

#         # key = self._get_key(update)
#         # state = self._conversations.get(key)
#         # check: Optional[object] = None

#         # # Resolve futures
#         # if isinstance(state, PendingState):
#         #     _logger.debug("Waiting for asyncio Task to finish ...")

#         #     # check if future is finished or not
#         #     if state.done():
#         #         res = state.resolve()
#         #         # Special case if an error was raised in a non-blocking entry-point
#         #         if state.old_state is None and state.task.exception():
#         #             self._conversations.pop(key, None)
#         #             state = None
#         #         else:
#         #             self._update_state(res, key)
#         #             state = self._conversations.get(key)

#         #     # if not then handle WAITING state instead
#         #     else:
#         #         handlers = self.states.get(self.WAITING, [])
#         #         for handler_ in handlers:
#         #             check = handler_.check_update(update)
#         #             if check is not None and check is not False:
#         #                 return self.WAITING, key, handler_, check
#         #         return None

#         # _logger.debug("Selecting conversation %s with state %s", str(key), str(state))

#         # handler: Optional[BaseHandler] = None

#         # # Search entry points for a match
#         # if state is None or self.allow_reentry:
#         #     for entry_point in self.entry_points:
#         #         check = entry_point.check_update(update)
#         #         if check is not None and check is not False:
#         #             handler = entry_point
#         #             break

#         #     else:
#         #         if state is None:
#         #             return None

#         # # Get the handler list for current state, if we didn't find one yet and we're still here
#         # if state is not None and handler is None:
#         #     for candidate in self.states.get(state, []):
#         #         check = candidate.check_update(update)
#         #         if check is not None and check is not False:
#         #             handler = candidate
#         #             break

#         #     # Find a fallback handler if all other handlers fail
#         #     else:
#         #         for fallback in self.fallbacks:
#         #             check = fallback.check_update(update)
#         #             if check is not None and check is not False:
#         #                 handler = fallback
#         #                 break

#         #         else:
#         #             return None

#         # return state, key, handler, check  # type: ignore[return-value]

