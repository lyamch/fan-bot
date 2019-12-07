import discord
import random
from discord.ext import tasks, commands
import os

Bot = commands.Bot(command_prefix= "+")
Bot.remove_command('help')
@Bot.command()
async def help(ctx):
    embed = discord.Embed(title="топ бот", description="создатель бота <@427792105537142794>", color=0xeee657)

    embed.add_field(name="привет", value="сказать боту привет", inline=False)
    embed.add_field(name="пока", value="сказать боту пока", inline=False)
    embed.add_field(name="unmute", value="размутить нарушителя", inline=False)
    embed.add_field(name="avatar", value="показывает аватар участника", inline=False)
    embed.add_field(name="ban", value="забанить нарушителя", inline=False)
    embed.add_field(name="kick", value="кикнуть нарушителя", inline=False)
    await ctx.send(embed=embed)
@Bot.command()
@commands.has_permissions(administrator= True)
async def unmute(ctx, member : discord.Member = None ):
                    await ctx.message.delete()
                    if not member:
                        ctx.send("Укажите пользователя!")
                    else:
                        membern = member.nick
                        if member.nick == None:
                            membern = member.name
                        unmute_cnt = f"Пользователь {membern} быз раззамучен админом {ctx.author}!"
                        unmute = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x000000)
                        role = discord.utils.get(ctx.message.guild.roles, name="muted")
                        await member.remove_roles(role)
                        await ctx.send(embed= unmute)           
@Bot.command(pass_context= True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
            await ctx.guild.ban(user)
            emb = discord.Embed(title = "*** Пользователь {} был забанен***".format(user), colour= 0x42f4f4)
            await ctx.send(embed= emb)
            await ctx.send("Произошёл бан")
@Bot.command(pass_context= True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
                        await ctx.guild.kick(user)
                        emb = discord.Embed(title = "*** Пользователь {} был кикнут***".format(user), colour= 0x42f4f4)
                        await ctx.send(embed= emb)
@Bot.command()                      
async def avatar(ctx, member : discord.Member = None):
                            user = ctx.message.author if (member == None) else member
                            await ctx.message.delete()
                            embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=user.color)
                            embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
                            embed.set_image(url=user.avatar_url)
                            await ctx.send(embed=embed)
@Bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''
    await ctx.send('pong') 
    # Get the latency of the bot
    latency = Bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
@Bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)           
@Bot.command()
async def cat(ctx):
            await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")                               
@Bot.command()
async def dog(ctx):
            await ctx.send("https://media.tenor.com/images/a0e28d22bb8f37bc83e1d4d1f1337e2b/tenor.gif")                                             
@Bot.command()
async def say(ctx, arg):
            await ctx.send(arg)
            await ctx.message.delete()                         
@Bot.event
async def on_ready():
        print("Я запущен !")
                        
@Bot.command()
async def привет(ctx):
        await ctx.send(f'Привет {ctx.message.author.mention}')                        
@Bot.command()
async def пока(ctx):
        await ctx.send(f'Пока {ctx.message.author.mention}')       
@Bot.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
            await ctx.channel.purge(limit=amount)
            await ctx.send("ваши сообщении удалились")

token = os.environ.get("BOT_TOKENS")