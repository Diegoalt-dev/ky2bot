from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random
import os
PORT = int(os.environ.get('PORT',5000))
TOKEN = '1595251301:AAHYRJnjRfWgVPccN1gmmqpf-LfMGaeY0Y8'
updater = Updater(token=TOKEN, use_context = True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

##Data

resp_pablo_data = ["No podría estar más de acuerdo","Me parece un excelente argumento", "Sin duda lo mejor que he oído desde Vietnam","Interesante pero discutible", "No tengo el suficiente conocimiento del tema así que le doy la razón", "No estoy de acuerdo pero no creo que discutirlo nos lleve a algo","Me parece un argumento totalmente válido", "Comparto la opinión del compañero", "Efectivamente", "Un comentario acertado para alguien de la nacional"]
miembros = []

frases = ["No hay jungla", "mancos todos", "no vuelvo a venirme con Nicolás soporte", "Diego regaló la partida otra vez", "No hay equipo", "Cómprense un par de manos mancos hptas"]
## Funciones
def start(update,context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    mensaje = "hola {} soy un bot".format(first_name)
    context.bot.send_message(chat_id=update.effective_chat.id,text=mensaje)

def echo(update,context):
    first_name = update.message.from_user.first_name
    if first_name is not None and first_name not in miembros:
        miembros.append(first_name)
    print(miembros)
    #context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,text = text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "¿De qué me hablas viejo?")

def resp_pablo(update,context):
    respuesta = random.randint(0,len(resp_pablo_data)-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text = resp_pablo_data[respuesta])

def lista_miembros(update,context):
    texto = ' \n'.join(miembros)
    update.message.reply_text(text = texto, quote = True)
    #context.bot.send_message(chat_id=update.effective_chat.id, text = texto)

def gei(update,context):
    miembro = random.randint(0,len(miembros)-1)
    respuesta = '{} es gei'.format(miembros[miembro])
    context.bot.send_message(chat_id=update.effective_chat.id, text = respuesta)

def lol(update,context):
    linea = random.randint(0,len(frases)-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text = frases[linea])

def lineas(update,context):
    jugadores = update.message.text
    jugadores = jugadores[8:]
    print(jugadores)
    
    jugadores = jugadores.split(' ')
    random.shuffle(jugadores)
    print("jugadores: ", jugadores)
    posiciones = " Top: {} \n Jungla: {} \n Mid: {} \n Sup: {} \n ADC: {}".format(jugadores[0],jugadores[1],jugadores[2],jugadores[3],jugadores[4]) 
    
    context.bot.send_message(chat_id=update.effective_chat.id, text = posiciones)



## Handler
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler((~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps',caps)
dispatcher.add_handler(caps_handler)

resp_pablo_handler = CommandHandler('pablo',resp_pablo)
dispatcher.add_handler(resp_pablo_handler)

lista_miembros_handler = CommandHandler('lista',lista_miembros)
dispatcher.add_handler(lista_miembros_handler)

gei_handler = CommandHandler('gei',gei)
dispatcher.add_handler(gei_handler)

lol_handler = CommandHandler('lol', lol)
dispatcher.add_handler(lol_handler)

lineas_handler = CommandHandler('lineas', lineas)
dispatcher.add_handler(lineas_handler)

unknown_handler = MessageHandler (Filters.command,unknown)
dispatcher.add_handler(unknown_handler)



#updater.start_polling()

updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://ky2bot.herokuapp.com/' + TOKEN)

updater.idle()
