import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send("Archivo guardado")
            class_name = get_class("keras_model.h5","labels.txt",file_name)
            await ctx.send(class_name)

            try:
                class_name = get_class("keras_model.h5","labels.txt",file_name)
                if class_name [0] == "Paloma":
                    await ctx.send("Esto es una paloma, es una especie de ave columbiforme de la familia de las colúmbidas​ nativa del sur de Eurasia y del norte de África y las palomas suelen comer semillas, granos, frutas, bayas, e incluso insectos y lombrices.")
                    
                elif class_name[0] == "Gorrion":
                    await ctx.send("Esto es un gorrion es una especie de ave paseriforme de la familia Passeridae y los gorriones viven en zonas urbanas y rurales cerca de asentamientos humanos, incluyendo ciudades, pueblos, suburbios y granjas.")

                elif class_name[0] == "Pantera":
                    await ctx.send("Esto es un jaguar negro es un críptido o un supuesto nuevo taxón de gran félido del género Panthera, viven en  bosques y selvas, en las sabanas, en los sembrados y en lugares rocosos, e incluso en desiertos, y se alimentan de mamíferos medianos y pequeños.")

                elif class_name[0] == "Ballena":
                    await ctx.send("Esto es una ballena es el mamífero más grande que existe en la Tierra y se alimentan de una variedad de presas marinas, que van desde pequeños crustáceos como el krill hasta peces y calamares.")

                elif class_name[0] == "Oso":
                    await ctx.send("Esto es un oso es el mamífero perteneciente a la familia Ursidae, conocidos por su gran tamaño y apariencia robusta, y se alimentan de frutas, verduras, raíces, nueces, miel, insectos, peces, carroña y pequeños mamíferos.")

            except:
                await ctx.send("La clasifación ha fallado")

    else:
        await ctx.send("No hay archivos adjuntos")



bot.run("TOKEN")