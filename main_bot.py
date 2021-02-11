from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random
import os
import mysql.connector

kydb = mysql.connector.connect(
    host = "bjngncktssejoh2aveqb-mysql.services.clever-cloud.com",
    user = "u46ncc7myfzsh8zr",
    password = "BVK9GOH4hnPr7PB9QcCp",
    database = 'bjngncktssejoh2aveqb'
)
kycursor = kydb.cursor()
quer_sal = "SELECT url FROM url_imag WHERE tipo = 'saludo'"
quer_hit = "SELECT url FROM url_imag WHERE tipo = 'golpe'"
quer_kiss = "SELECT url FROM url_imag WHERE tipo = 'beso'"
kycursor.execute(quer_sal)
resultado = kycursor.fetchall()
kycursor.execute(quer_hit)
resultado_hit = kycursor.fetchall()
kycursor.execute(quer_kiss)
resultado_kiss = kycursor.fetchall()

class ky2():
    """
    La clase ky2 sirve para el bot de telegram ky2bot.

        Atributos:

        Métodos:
            start(self, update, context)

            echo(self, update, context)

            caps(self, update, context)

            unknown(self, update, context)

            resp_pablo(self, update, context)

            lista_miembros(self, update, context)

            gei(self, update, context)

            lol(self, update, context)

            lineas(self, update, context)

            hi(self, update, context)

            hit(self, update, context)

            kiss(self, update, context)

            campeon(self, update, context)

            tw(self, update, context)

            ball(self, update, context)
    """

    def __init__(self):
        self.db = db_ky2()
        self.resp_pablo_data = ["No podría estar más de acuerdo","Me parece un excelente argumento", "Sin duda lo mejor que he oído desde Vietnam","Interesante pero discutible", "No tengo el suficiente conocimiento del tema así que le doy la razón", "No estoy de acuerdo pero no creo que discutirlo nos lleve a algo","Me parece un argumento totalmente válido", "Comparto la opinión del compañero", "Efectivamente", "Un comentario acertado para alguien de la nacional", "Me pareció interesante, sobre todo la parte en la que menciona a Palestina"]
        self.miembros = []
        self.frases = ["No hay jungla", "mancos todos", "no vuelvo a venirme con Nicolás soporte", "Diego regaló la partida otra vez", "No hay equipo", "Cómprense un par de manos mancos hptas"]
        self.bola8 = ["En mi opinión, sí","Es cierto","Probablemente","Todo apunta a que sí","Sin duda","Si","Definitivamente","Pregunta en otro momento", "Intenta de nuevo","Será mejor que no te lo diga ahora","No puedo predecirlo ahora","Puede ser","No cuentes con ello","No","Muy dudoso","Mis fuentes me dicen que no","Las perspectivas no son buenas"]

    def start(self, update, context):
        nombre = update.message.from_user.first_name
        mensaje = "hola {} soy ky2bot, el mejor de to2 los bots".format(nombre)
        context.bot.send_message(chat_id = update.effective_chat.id,text = mensaje)

    def echo(self, update, context):
        nombre = update.message.from_user.first_name
        if nombre is not None and nombre not in self.miembros:
            self.miembros.append(nombre)

    def unknown(self, update, context):
        context.bot.send_message(chat_id = update.effective_chat.id, text = "¿De qué me hablas viejo?")

    def resp_pablo(self, update, context):
        respuesta = random.randint(0,len(self.resp_pablo_data)-1)
        context.bot.send_message(chat_id = update.effective_chat.id, text = self.resp_pablo_data[respuesta])

    def lista_miembros(self, update, context):
        texto = ' \n'.join(self.miembros)
        update.message.reply_text(text = texto, quote = True)

    def gei(self, update, context):
        miembro = random.randint(0,len(self.miembros)-1)
        respuesta = '{} es gei.'.format(self.miembros[miembro])
        context.bot.send_message(chat_id = update.effective_chat.id, text = respuesta)

    def lol(self, update, context):
        linea = random.randint(0,len(self.frases)-1)
        context.bot.send_message(chat_id = update.effective_chat.id, text = self.frases[linea])

    def lineas(self, update, context):
        jugadores = update.message.text
        jugadores = jugadores[8:]
        jugadores = jugadores.split(' ')
        random.shuffle(jugadores)
        posiciones = " Top: {} \n Jungla: {} \n Mid: {} \n Sup: {} \n ADC: {}".format(jugadores[0],jugadores[1],jugadores[2],jugadores[3],jugadores[4])
        context.bot.send_message(chat_id = update.effective_chat.id, text = posiciones)

    def hi(self, update, context):
        nombre = update.message.from_user.first_name
        num = random.randint(0,len(resultado)-1)
        context.bot.sendAnimation(chat_id = update.effective_chat.id, animation = resultado[num][0], caption = "¡{} ha saludado a todos!".format(nombre))

    def hit(self, update, context):
        nombre = update.message.from_user.first_name
        golpeado = context.args
        num = random.randint(0,len(resultado_hit)-1)
        context.bot.sendAnimation(chat_id = update.effective_chat.id, animation = resultado_hit[num][0], caption = "¡{} ha golpeado a {}!".format(nombre,golpeado[0]))

    def kiss(self, update, context):
        nombre = update.message.from_user.first_name
        besito = context.args
        num = random.randint(0,len(resultado_kiss)-1)
        context.bot.sendAnimation(chat_id = update.effective_chat.id, animation = resultado_bis[num][0], caption = "¡{} ha besado a {}! <3".format(nombre,besito[0]))

    def campeon(self, update, context):
        dato = update.message.text
        dato = dato[9:]
        numero = str(random.randint(1,int(dato)))
        context.bot.send_message(chat_id=update.effective_chat.id, text = numero)

    def tw(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text = "THAT'S WHAT SHE SAID")

    def ball(self, update, context):
        Pronostico = random.randint(0,len(bola8)-1)
        context.bot.send_message(chat_id=update.effective_chat.id, text = bola8[Pronostico])

k = ky2()
PORT = int(os.environ.get('PORT',5000))
TOKEN = '1595251301:AAHYRJnjRfWgVPccN1gmmqpf-LfMGaeY0Y8'

updater = Updater(token=TOKEN, use_context = True)
dispatcher = updater.dispatcher

## Handler
start_handler = CommandHandler('start', k.start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler((~Filters.command), k.echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', k.caps)
dispatcher.add_handler(caps_handler)

resp_pablo_handler = CommandHandler('pablo', k.resp_pablo)
dispatcher.add_handler(resp_pablo_handler)

lista_miembros_handler = CommandHandler('lista', k.lista_miembros)
dispatcher.add_handler(lista_miembros_handler)

gei_handler = CommandHandler('gei', k.gei)
dispatcher.add_handler(gei_handler)

lol_handler = CommandHandler('lol', k.lol)
dispatcher.add_handler(lol_handler)

lineas_handler = CommandHandler('lineas', k.lineas)
dispatcher.add_handler(lineas_handler)

saludo_handler = CommandHandler('hi', k.hi)
dispatcher.add_handler(saludo_handler)

hit_handler = CommandHandler('hit', k.hit)
dispatcher.add_handler(hit_handler)

kiss_handler = CommandHandler('kiss', k.kiss)
dispatcher.add_handler(kiss_handler)

campeon_handler = CommandHandler('campeon', k.campeon)
dispatcher.add_handler(campeon_handler)

tw_handler = CommandHandler('tw', k.tw)
dispatcher.add_handler(tw_handler)

ball_handler = CommandHandler('8ball', k.ball)
dispatcher.add_handler(ball_handler)

unknown_handler = MessageHandler (Filters.command, k.unknown)
dispatcher.add_handler(unknown_handler)

updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)

updater.bot.setWebhook('https://ky2bot.herokuapp.com/' + TOKEN)

updater.idle()
