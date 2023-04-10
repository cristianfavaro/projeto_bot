from bot.application.utils import CommandHandler, ConversationHandler
from bot.application.dispatcher import Dispatcher, Bot


def conversa(update, context):
    text = "olá  2"
    update.message.reply_text(text=text) #reply_markup=markup, parse_mode=ParseMode.MARKDOWN

def dentro_conversa(update, context):
    update.message.reply_text(text='Dentro da conversa') #reply_markup=markup, parse_mode=ParseMode.MARKDOWN

def empresas(update, context):
    text = "olá"
    update.message.reply_text(text=text) #reply_markup=markup, parse_mode=ParseMode.MARKDOWN
    # update.callback_query.edit_message_text(text=text) #reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN

    # return EMPRESA_PANEL?

empresas_command = CommandHandler("empresas", empresas)

conversa_command = CommandHandler('conv', conversa)

dentro_conversa_command = CommandHandler('dentro_conversa', dentro_conversa)

conversation_conv = ConversationHandler(
    'conv', 
    [conversa_command], 
    [dentro_conversa_command],
    )

bot = Bot("1523369372:AAH1QzZamQq09lwiMRVrlJT7ljIpT5hzHd0")

dispatcher = Dispatcher(bot)

dispatcher.add_handler(empresas_command)
dispatcher.add_handler(conversation_conv)
