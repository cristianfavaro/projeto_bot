from bot.application.utils import CommandHandler, ConversationHandler
from bot.application.dispatcher import Dispatcher, Bot
from decouple import config
from bot.application.inline import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(config("TOKEN"))
dispatcher = Dispatcher(bot)

def start(update, context):
    text = "olá, boas vindas ao bot do Cristian. Atenção... estou um pouco confuso ainda.... Enviei /help para saber o que eu já consigo fazer."
    update.message.reply_text(text=text) 

dispatcher.add_handler(CommandHandler("start", start))


def help(update, context):
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text="Testando", callback_data="aqui_volta"),
            InlineKeyboardButton(text="Testando 2", callback_data="aqui_volta2")
        ]]
    )

    # aqui eu vou criar os teclado


dispatcher.add_handler(CommandHandler("help", help))


def empresas(update, context):
    text = "olá  2"
    update.message.reply_text(text=text) 
empresas_command = CommandHandler('empresas', empresas)
dispatcher.add_handler(empresas_command)


###### Modelo de como funciona a conversa 

def conversa(update, context):
    text = "olá, estamos dentro da conversa."
    update.message.reply_text(text=text) 
    
conversa_command = CommandHandler('conv', conversa)

def dentro_conversa(update, context):
    update.message.reply_text(text='Dentro da conversa') 
dentro_conversa_command = CommandHandler('dentro_conversa', dentro_conversa)


dispatcher.add_handler(ConversationHandler(
        'conv', 
        [conversa_command], 
        [dentro_conversa_command],
    )
)