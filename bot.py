import discord


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("Hola! Soy un reciclador profesional y quería enseñarte cómo hacerlo de una manera divertida. Por eso quiero saber que material tienes a tu dispocicion: biodegradable ($biodegradable) o  reciclable ($reciclable)")
    elif message.content.startswith("$biodegradable"):
            await message.channel.send("Por lo que he visto tienes materiales biodegradables que sirven como abono para tus plantas. Aqui te enseñare como cortar ese material biodegradable y prepararlo para tus plantas ($preparar) o si quieres te enseño como cuidar tus plantas ($cuidar)")
    elif message.content.startswith("$preparar"):
         await message.channel.send("OK. Para poder preparar tus materiales biodegradables para tus plantas debes seguir los pasos que se te indican en este video: https://www.youtube.com/watch?v=hMvDB9bcJ5Y")
    elif message.content.startswith("$cuidar"):
         await message.channel.send("WOW. Me impresiona que quieras cuidar tus plantas mejor. Esto las ayudara a crecer sanas y fuertes y te daran los mejores frutos que jamas se hallan cosechado en el mundo. Para lograr eso, sigue los pasos del siguiente video: https://www.youtube.com/watch?v=Y1jTRsBRh3g")
    elif message.content.startswith("$reciclable"):
         await message.channel.send("Interesante. Al parecer quieres ver que hacer con tus materiales reciclables. Pues bueno yo te dire que puedes hacer. Tengo para ti 3 manualidades con materiales caseros: puedes hacer una matera ($matera), un muñequito ($juguete) o un barquito ($barco). ¡Tienes todas estas opciones a tu elección, dale, elige una!")
    elif message.content.startswith("$barco"):
         await message.channel.send("Que buena elección, un barquito. Una gran invención si me preguntas. Para lograr hacer esta manualidad sigue los pasos de este video: https://www.youtube.com/watch?v=078ZelYhyAc")
    elif message.content.startswith('$adios'):
        await message.channel.send("Hasta la proxima!")





client.run("TU TOKEN")
