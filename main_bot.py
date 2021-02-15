from telegram.ext import Updater
import telegram
import logging
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

PORT = int(os.environ.get('PORT',5000))
TOKEN = '1595251301:AAHYRJnjRfWgVPccN1gmmqpf-LfMGaeY0Y8'
updater = Updater(token=TOKEN, use_context = True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

##Data
resp_pablo_data = ["No podría estar más de acuerdo","Me parece un excelente argumento", "Sin duda lo mejor que he oído desde Vietnam","Interesante pero discutible", "No tengo el suficiente conocimiento del tema así que le doy la razón", "No estoy de acuerdo pero no creo que discutirlo nos lleve a algo","Me parece un argumento totalmente válido", "Comparto la opinión del compañero", "Efectivamente", "Un comentario acertado para alguien de la nacional", "Me pareció interesante, sobre todo la parte en la que menciona a Palestina"]
miembros = []
personas = ["Alvaro", "Diego", "Guaro", "Jessica", "Camilo", "Camila", "Risca", "Miguel", "Pablo G.", "Pablo S.", "Pablo N.", "Santi", "Fernando", "Samuel", "Valentina", "Maria P", "Paisa", "Julian", "ky2bot"]
vida = []
bola8 = ["En mi opinión, sí","Es cierto","Probablemente","Todo apunta a que sí","Sin duda","Si","Definitivamente","Pregunta en otro momento", "Intenta de nuevo","Será mejor que no te lo diga ahora","No puedo predecirlo ahora","Puede ser","No cuentes con ello","No","Muy dudoso","Mis fuentes me dicen que no","Las perspectivas no son buenas"]
frases = ["No hay jungla.", "mancos todos.","Paisa carreenos.", "no vuelvo a venirme con Fabio support.", "Diego regaló la partida otra vez.", "gg no team.", "Cómprense un par de manos mancos hptas.", "Montaña es el peor mid del mundo.", "Vallejo otra vez en farm simulator."]

## Funciones
def start(update,context):
    first_name = update.message.chat.first_name
    mensaje = "hola {} soy ky2bot, el mejor de to2 los bots".format(first_name)
    context.bot.send_message(chat_id=update.effective_chat.id,text=mensaje)

def echo(update,context):
    first_name = update.message.from_user.first_name
    if first_name is not None and first_name not in miembros:
        miembros.append(first_name)
    print(miembros)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,text = text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "¿De qué me hablas viejo?")

def resp_pablo(update,context):
    respuesta = random.randint(0,len(resp_pablo_data)-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text = resp_pablo_data[respuesta])

def lista_miembros(update,context):
    """miembro=[]
    to2 = context.bot.get_chat_administrators(chat_id=update.effective_chat.id)
    for persona in to2:
        miembro.append(persona.user.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text = str(miembro))"""

    texto = ' \n'.join(miembros)
    update.message.reply_text(text = texto, quote = True)

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

def hi(update,context):
    nombre = update.message.from_user.first_name
    num = random.randint(0,len(resultado)-1)
    print("saludo "+ str(num) +" escogido")
    context.bot.sendAnimation(chat_id = update.effective_chat.id, animation = resultado[num][0], caption = "¡{} ha saludado a todos!".format(nombre))

def hit(update,context):
    nombre = update.message.from_user.first_name
    golpeado = context.args
    num = random.randint(0,len(resultado_hit)-1)
    print("golpe "+ str(num) +" escogido")

    num2 = personas.index(golpeado)
    life = int(vida[num2].split('h')[0])
    barra = vida[num2].split()[1]

    if life > 0:
        golpe = random.randint(0,5000-1)
        life = life - golpe
        if life > 9999:
            barra = "██████████"
        if life > 8999 and life < 9999:
            barra = " █████████░"
        if life > 7999 and life < 8999:
            barra = " ████████░░"
        if life > 6999 and life < 7999:
            barra = " ███████░░░"
        if life > 5999 and life < 6999:
            barra = " ██████░░░░"
        if life > 4999 and life < 5999:
            barra = " █████░░░░░"
        if life > 3999 and life < 4999:
            barra = " ████░░░░░░"
        if life > 2999 and life < 3999:
            barra = " ███░░░░░░░"
        if life > 1999 and life < 2999:
            barra = " ██░░░░░░░░"
        if life > 999 and life < 1999:
            barra = " █░░░░░░░░░"
        if life < 0:
            barra = " ░░░░░░░░░░"
            life = 0
    newvida = vida[num].replace(vida[num].split('h')[0],str(life))
    newvida = newvida.replace(vida[num].split()[1],barra)

    vida[num]=newvida
   
    context.bot.sendAnimation(chat_id = update.effective_chat.id, animation = resultado_hit[num][0], caption = "{} ha golpeado a {} y le hizo {} de daño!".format(nombre, personas[num2], golpe))

def kiss(update,context):
    nombre = update.message.from_user.first_name
    besito = context.args
    num = random.randint(0,len(resultado_kiss)-1)
    print("beso "+ str(num) +" escogido")
    context.bot.sendAnimation(chat_id = update.effective_chat.id, animation = resultado_kiss[num][0], caption = "¡{} ha besado a {}! <3".format(nombre,besito[0]))

def actdb(update,context):
    try:
        kydb = mysql.connector.connect(
        host = "bjngncktssejoh2aveqb-mysql.services.clever-cloud.com",
        user = "u46ncc7myfzsh8zr",
        password = "BVK9GOH4hnPr7PB9QcCp",
        database = 'bjngncktssejoh2aveqb'
        )
        kycursor = kydb.cursor()
        kycursor.execute(quer_sal)
        resultado = kycursor.fetchall()
        kycursor.execute(quer_hit)
        resultado_hit = kycursor.fetchall()
        update.message.reply_text(text = "Base de datos reconectada", quote = True)
    except:
        update.message.reply_text(text = "Error en reconexión a base de datos", quote = True)

def campeon(update,context):
    dato = update.message.text
    dato = dato[9:]
    numero = str(random.randint(1,int(dato)))
    context.bot.send_message(chat_id=update.effective_chat.id, text = numero)

def tw(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "THAT'S WHAT SHE SAID")

def ball(update,context):
    if update.message.text != '/8ball':
        Pronostico = random.randint(0,len(bola8)-1)
        context.bot.send_message(chat_id=update.effective_chat.id, text = bola8[Pronostico])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "Falta la pregunta crack.")

def pvida(update,context):
    vidas = "{}=    {}\n{}=     {}\n{}=     {}\n{}=   {}\n{}=    {}\n{}=    {}\n{}=      {}\n{}=    {}\n{}=  {}\n{}=  {}\n{}=  {}\n{}=        {}\n{}= {}\n{}=    {}\n{}= {}\n{}=   {}\n{}=       {}\n{}=      {}\n{}=    {}\n".format(personas[0],vida[0], personas[1],vida[1],personas[2],vida[2],personas[3],vida[3],personas[4],vida[4],personas[5],vida[5],personas[6],vida[6],personas[7],vida[7], personas[8],vida[8], personas[9],vida[9],personas[10],vida[10],personas[11],vida[11],personas[12],vida[12],personas[13],vida[13],personas[14],vida[14],personas[15],vida[15], personas[16],vida[16],personas[17],vida[17],personas[18],vida[18])
    context.bot.send_message(chat_id=update.effective_chat.id, text = vida)


def reset(update,context):
    cont = 0
    vida = []
    while cont < 19:
        vida.append("10000hp ██████████")
        cont=cont+1
    vidas = "{}=    {}\n{}=     {}\n{}=     {}\n{}=   {}\n{}=    {}\n{}=    {}\n{}=      {}\n{}=    {}\n{}=  {}\n{}=  {}\n{}=  {}\n{}=        {}\n{}= {}\n{}=    {}\n{}= {}\n{}=   {}\n{}=       {}\n{}=      {}\n{}=    {}\n".format(personas[0],vida[0], personas[1],vida[1],personas[2],vida[2],personas[3],vida[3],personas[4],vida[4],personas[5],vida[5],personas[6],vida[6],personas[7],vida[7], personas[8],vida[8], personas[9],vida[9],personas[10],vida[10],personas[11],vida[11],personas[12],vida[12],personas[13],vida[13],personas[14],vida[14],personas[15],vida[15], personas[16],vida[16],personas[17],vida[17],personas[18],vida[18])
    context.bot.send_message(chat_id=update.effective_chat.id, text = vidas)

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

saludo_handler = CommandHandler('hi',hi)
dispatcher.add_handler(saludo_handler)

hit_handler = CommandHandler('hit',hit)
dispatcher.add_handler(hit_handler)

kiss_handler = CommandHandler('kiss',kiss)
dispatcher.add_handler(kiss_handler)

campeon_handler = CommandHandler('campeon',campeon)
dispatcher.add_handler(campeon_handler)

act_db_handler = CommandHandler('actdb',actdb)
dispatcher.add_handler(act_db_handler)

tw_handler = CommandHandler('tw',tw)
dispatcher.add_handler(tw_handler)

ball_handler = CommandHandler('8ball',ball)
dispatcher.add_handler(ball_handler)

pvida_handler = CommandHandler('pvida',pvida)
dispatcher.add_handler(pvida_handler)

reset_handler = CommandHandler('reset',reset)
dispatcher.add_handler(reset_handler)

unknown_handler = MessageHandler (Filters.command,unknown)
dispatcher.add_handler(unknown_handler)


updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://ky2bot.herokuapp.com/' + TOKEN)

updater.idle()
