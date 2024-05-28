import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='*', intents=intents)

allowed_users = {} 

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
   
    await bot.process_commands(message)

@bot.command()
async def zn(ctx, channel: discord.TextChannel, *args):
    if ctx.author.id in allowed_users.get(ctx.guild.id, []):
        content = " ".join(args) 
        message = await channel.send(content)
      
        emojis = ["<:emoji_5:1134834060317970472>", "<:emoji_6:1134834086582702130>"]
        for emoji in emojis:
            await message.add_reaction(emoji)
    else:
        await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")

@bot.command()
@commands.has_permissions(administrator=True) 
async def setpermission(ctx, user: discord.Member):
    allowed_users.setdefault(ctx.guild.id, set()).add(user.id)
    await ctx.send(f"{user.mention} a maintenant la permission d'utiliser !zn.")

@bot.command()
@commands.has_permissions(administrator=True) 
async def removepermission(ctx, user: discord.Member):
    allowed_users.setdefault(ctx.guild.id, set()).discard(user.id)
    await ctx.send(f"{user.mention} n'a plus la permission d'utiliser !zn.")

@bot.command()
async def commands(ctx):
    all_commands = bot.all_commands.keys()
    commands_list = "\n".join(all_commands)
    await ctx.send(f"Liste des commandes disponibles :\n```\n{commands_list}\n```")

bot.run(')








