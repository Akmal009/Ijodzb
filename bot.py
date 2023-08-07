import asyncio
from webserver import keep_alive
from dis import dis, disco
from lib2to3.pgen2 import token
from re import T
import discord
from discord.ext import commands
import string
import os


client = commands.Bot(command_prefix= '!')

mat = ['сука', 'блять', 'еблан', 'уебок', 'ахуел', 'пидарас','похуй', 'далбаеб', 'уебок', 'мразь', 'бля', 'нахуй', 'хуй', 'иди нахуй', 'говно', 'пидр', 'ебало', 'ебаный', 'ебаный в рот', 'мамка ебер', 'пидарас', 'рот ебал', 'котакпас', 'котакбас']


@client.event
async def on_ready():
    print('Здрасте командир!, Ваш бот успешно включен!')

    await client.change_presence(status = discord.Status.online, activity = discord.Game('IjodZB'))

#clear
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def clear(ctx,*, amount = 1):
    emb = discord.Embed(colour = discord.Color.green() )
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit = amount)
    emb.set_footer(text = 'Чат был очищен {}✅'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
    await ctx.send(embed= emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

@clear.error
async def error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(titile = 'Чистьюля', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'У вас недостаточно прав! {ctx.author.name}')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )

#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed(titile = 'Кик', colour = discord.Color.green() )
    await ctx.channel.purge(limit = 1)
    await member.kick(reason=reason)
    emb.set_author(name = member.name, icon_url= member.avatar_url)
    emb.add_field(name = 'Кик', value = 'кикнул игрока : {}'.format(member.mention))
    emb.set_footer(text = 'Был кикнут администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
    await ctx.send( embed= emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1 )

@kick.error
async def error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(titile = 'Кик', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'У вас недостаточно прав! {ctx.author.name}')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )
    elif isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(titile = 'Кик', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'{ctx.author.name}, Укажите пользователя!')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )

#ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed(titile = 'Бан', colour = discord.Color.green() )
    await ctx.channel.purge(limit = 1)
    await member.ban(reason=reason)
    emb.set_author(name = member.name, icon_url= member.avatar_url)
    emb.add_field(name = 'Бан', value = 'Забанил игрока : {}'.format(member.mention))
    emb.set_footer(text = 'Был забанен администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
    await ctx.send( embed= emb)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1 )

@ban.error
async def error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(titile = 'Бан', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'У вас недостаточно прав! {ctx.author.name}')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )
    elif isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(titile = 'Бан', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'{ctx.author.name}, Укажите пользователя!')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )

#unban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member):
    
    await ctx.channel.purge(limit = 1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        return

@unban.error
async def error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(titile = 'Разбан', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'У вас недостаточно прав! {ctx.author.name}')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'{ctx.author.name}, Укажите пользователя!')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )

#autoclearmat
@client.event
async def on_message(message):
    await client.process_commands(message)

    msg = message.content.lower().translate(str.maketrans('', '', string.punctuation))
    user = message.author
    if msg in mat:
        await message.channel.purge(limit=1 )
        await message.channel.send(f'{user.mention} Эээй по окуратнее с матами! ' )
        await asyncio.sleep(5)
        await message.channel.purge(limit=1 )

#mute
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member, time: int, how: str, reason=None):
    role = user.guild.get_role(1012236722630823937) # айди роли которую будет получать юзер
    await user.add_roles(role) #выдает мьют роль
    if how == 's':
        emb = discord.Embed(title='Мьютер',
                            description=f"Участнику {user.mention} выдали мут!\nВремя пробывания в муте: {time} секунд\nПричина выдачи мута: {reason}!",
                            colour=discord.Color.green())
        emb.set_footer(text='Действие выполнено модератором/админом - ' + ctx.author.name,
                       icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        await asyncio.sleep(time)
    elif how == 'm':
        emb = discord.Embed(title='Мьютер',
                            description=f"Участнику {user.mention} выдали мут!\nВремя пробывания в муте: {time} минут\nПричина выдачи мута: {reason}!",
                            colour=discord.Color.green())
        emb.set_footer(text='Действие выполнено модератором/админом - ' + ctx.author.name,
                       icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        await asyncio.sleep(time * 60)
    elif how == 'h':
        emb = discord.Embed(title='Мьютер',
                            description=f"Участнику {user.mention} выдали мут!\nВремя пробывания в муте: {time} часа(ов)\nПричина выдачи мута: {reason}!",
                            colour=discord.Color.green())
        emb.set_footer(text='Действие выполнено модератором/админом - ' + ctx.author.name,
                       icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        await asyncio.sleep(time * 3600)
    await user.remove_roles(role) #снимает мьют роль

@mute.error
async def error(ctx, error):
    global emb
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(titile = 'Мьютер', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'У вас недостаточно прав! {ctx.author.name}')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )
    elif isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(titile = 'Мьютер', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'{ctx.author.name}, Укажите пользователя!')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )

#unmute
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, user: discord.Member):
    role = user.guild.get_role(1012236722630823937)
    ctx.channel.purge(limit=1)
    emb = discord.Embed(title='Унмьютер',
                        description=f"У участника {user.mention} убрали мут!",
                        colour=discord.Color.green())
    await user.remove_roles(role)
    emb.set_footer(text='Действие выполнено модератором/админом - ' + ctx.author.name,
                   icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

@unmute.error
async def error(ctx, error):
    global emb
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(titile = 'Унмьютер', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'У вас недостаточно прав! {ctx.author.name}')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )
    elif isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(titile = 'Унмьютер', colour = discord.Color.red() )
        await ctx.channel.purge(limit=1)
        emb.set_footer(text = f'{ctx.author.name}, Укажите пользователя!')
        await ctx.send( embed= emb)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1 )

keep_alive()
client.run(os.getenv("DSTOK"))