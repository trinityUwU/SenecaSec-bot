#https://data.lacity.org/resource/6rrh-rzua.json?buisness_nameGOOGLE
import discord
import discord.ext
from discord import role
from discord.ext import commands, tasks
import json
from discord.utils import get
import re
import random
import os
from discord.ext.commands import Bot, has_permissions, MissingPermissions
from itertools import cycle
from urllib import parse, request
from datetime import datetime, timedelta
import asyncio
from time import sleep
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from os import system
import youtube_dl
import requests
from discord import Activity, ActivityType
import pyfiglet
import socket
import sys
from requests import get
import bs4
from bs4 import BeautifulSoup
import hashlib 
import base64
import datetime
import safygiphy
import urllib.request
from urllib.request import Request, urlopen
import io
import string

ascii_banner = pyfiglet.figlet_format("SenecaSec")
print(ascii_banner)

TOKEN = 'NjA1Mzc1NDI0ODg0ODk5ODUw.XT7lzA.kx-8g1bHF4Syvb8FBKg9GOfJ80g'
bot = commands.Bot(command_prefix ="$")
bot.remove_command('help')
client = discord.Client()

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Panel d'aide", color=0x00ff00)
    embed.set_author(name="")
    embed.add_field(name='***$admin***', value='Administrateur', inline=True)
    embed.add_field(name='***$mod***',value='Modération', inline=True)
    embed.add_field(name='***$tool***',value='Boite à outils', inline=True)
    await ctx.send("https://64.media.tumblr.com/0870408ef69639327475f93f665ac490/5c7bd8bcc33b5478-02/s500x750/ee4ec4c470d99ab8460c749465e887e34373caae.gif")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def admin(ctx):
    admin = False

    if "PDG" in str(ctx.message.author.roles):
        admin = True
        pass
    elif "*" in str(ctx.message.author.roles):
        admin = True
        pass
    else:
        admin = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if admin == True:
        embed = discord.Embed(title="", color=0x00ff00)
        embed.set_author(name="")
        embed.add_field(name='***$admin***', value='Commande Administrateur', inline=True)
        embed.add_field(name='***$clear [number]***', value='Supprimer des messages en masse', inline=True)
        embed.add_field(name='***$pseudo [user]***', value='Modifier un pseudonyme', inline=True)
    
        await ctx.send(embed=embed)
    else:
        pass

@bot.command(pass_context=True)
async def mod(ctx):
    mod = False

    if "PDG" in str(ctx.message.author.roles):
        mod = True
        pass
    elif "*" in str(ctx.message.author.roles):
        mod = True
    else:
        mod = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if mod == True:    
        embed = discord.Embed(title="", color=0x00ff00)
        embed.set_author(name="")
        embed.add_field(name='***$warn [@user]***', value='Warn un utilisateur', inline=True)
        embed.add_field(name='***$kick [@user]***', value='Exclure un utilisateur', inline=True) 
        embed.add_field(name='***$ban [@user]***', value='Bannir un utilisateur', inline=True) 
        embed.add_field(name='***$unban [@user]***', value='Debannir un utilisateur', inline=True) 
        embed.add_field(name='***$mute [@user]***', value='Mute un utilisateur', inline=True) 
        embed.add_field(name='***$unmute [@user]***', value='Demute un utilisateur', inline=True) 

        await ctx.send(embed=embed)
    else:
        pass

@bot.command(pass_context=True)
#@commands.has_permissions(administrator=True)
async def tool(ctx):
    tool = False

    if "Analyste" in str(ctx.message.author.roles):
        tool = True
        pass
    elif "*" in str(ctx.message.author.roles):
        tool = True
    else:
        tool = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if tool == True:
        embed = discord.Embed(title="", color=0x00ff00)
        embed.set_author(name="")
        embed.add_field(name='***$cve [text]***',value='Faire une recherche CVE', inline=True)
        embed.add_field(name='***$geoip [0.0.0.0]***',value='Geolocaliser une adresse IP', inline=True)
        embed.add_field(name='***$nmap [0.0.0.0] ou [URL]***',value='Analyse NMAP', inline=True)
        embed.add_field(name='***$whatweb [URL]***',value='Footprinting WhatWeb', inline=True)
        embed.add_field(name='***$md5 [text]***',value='Hashing MD5', inline=True)
        embed.add_field(name='***$sha256 [text]***',value='Hashing SHA256', inline=True)
        embed.add_field(name='***$sha512 [text]***',value='Hashing SHA512', inline=True)
        embed.add_field(name='***$pp [@user]***', value='Obtenir un avatar', inline=True)
        embed.add_field(name='***$theharvester [command]***', value='-h for help', inline=True)
        embed.add_field(name='***$finalrecon [site], (sans https/http)***', value='scan of site', inline=True)
        await ctx.send(embed=embed)
    else:
        pass

@bot.command()
async def clear(context, amount = 2):
    await context.channel.purge(limit = amount)
    await context.send(f'***{amount-1} messages on été supprimé.***')

@bot.command(pass_context=True) 
@commands.has_guild_permissions(manage_nicknames=True)
async def pseudo(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f"{member.name}' à changer sont pseudonyme !**")

@bot.command()
async def md5(ctx, *, msg :str):
    md5 = False
    if "Analyste" in str(ctx.message.author.roles):
        md5 = True
        pass
    elif "*" in str(ctx.message.author.roles):
        md5 = True
    else:
        md5 = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if md5 == True:    
        """Hasher MD5"""
        await ctx.send("`{}`".format(hashlib.md5(bytes(msg.encode("utf-8"))).hexdigest()))\

    else:
        pass

@bot.command()
async def sha256(ctx, *, msg:str):
    sha256 = False
    if "Analyste" in str(ctx.message.author.roles):
        sha256 = True
        pass
    elif "*" in str(ctx.message.author.roles):
        sha256 = True
    else:
        sha256 = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass
    
    if sha256 == True:
        """Hasher SHA256"""
        await ctx.send(f"https://i.gzn.jp/img/2020/05/14/sha-256-animation/105.gif")
        await ctx.send("`{}`".format(hashlib.sha256(bytes(msg.encode("utf-8"))).hexdigest()))

@bot.command()
async def sha512(ctx, *, msg:str):
    sha512 = False
    if "Analyste" in str(ctx.message.author.roles):
        sha512 = True
        pass
    elif "*" in str(ctx.message.author.roles):
        sha512 = True
    else:
        sha512 = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if sha512 == True:
        """Hasher SHA512"""
        await ctx.send(f"https://techcrunch.com/wp-content/uploads/2019/01/tracking-phones.gif")
        await ctx.send("`{}`".format(hashlib.sha512(bytes(msg.encode("utf-8"))).hexdigest()))
    else:
        pass

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    kick = False
    if "PDG" in str(ctx.message.author.roles):
        kick = True
        pass
    elif "*" in str(ctx.message.author.roles):
        kick = True
    else:
        kick = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if kick == True:
        await member.kick(reason=reason)
        await ctx.send(f"https://i.giphy.com/media/xTk9ZBWrma4PIC9y4E/giphy.gif")
        await ctx.send(f'***{member.mention} cette utlisateur à été expulser de {ctx.guild.name} !***')
    else:
        pass

@bot.command()
async def ban(ctx, member:discord.Member = None):
    ban = False
    if "PDG" in str(ctx.message.author.roles):
        ban = True
        pass
    elif "*" in str(ctx.message.author.roles):
        ban = True
    else:
        ban = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if ban == True:
        if not member:
            await ctx.send("***Spécifier le membre !***")
            return
        await member.ban()
        await ctx.send(f"https://i.giphy.com/media/xTk9ZBWrma4PIC9y4E/giphy.gif")
        await ctx.send(f"***Cette utilisateur {member.mention} à été banni de {ctx.guild.name} !***")
    else:
        pass

@bot.command()
async def unban(ctx, user, *reason):
    unban = False
    if "PDG" in str(ctx.message.author.roles):
        unban = True
        pass
    elif "*" in str(ctx.message.author.roles):
        unban = True
    else:
        unban = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if unban == True:
        reason = " ".join(reason)
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user, reason = reason)
                await ctx.send(f'{user} à été unban !')
                return
                await ctx.send(f'L''utilisateur {user} n''est pas dans la liste des bans !')
    else:
        pass

@bot.command()
async def mute(ctx, member: discord.Member=None):
    mute = False
    if "PDG" in str(ctx.message.author.roles):
        mute = True
        pass
    elif "*" in str(ctx.message.author.roles):
        mute = True
    else:
        mute = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if mute == True:
        if not member:
            await ctx.send("***Spécifier le membre !***")
            return
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.add_roles(role)
        await ctx.send(f"***Cette utilisateur {member.mention} à été mute !***")
    else:
        pass

@bot.command()
async def unmute(ctx, member: discord.Member=None):
    unmute = False
    if "PDG" in str(ctx.message.author.roles):
        unmute = True
        pass
    elif "*" in str(ctx.message.author.roles):
        unmute = True
    else:
        unmute = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if unmute == True:
        if not member:
            await ctx.send("***Spécifier le membre !***")
            return
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.remove_roles(role)
        await ctx.send(f"***Cette utilisateur {member.mention} à été unmute !***")
    else:
        pass

@bot.command()
async def warn(ctx, member : discord.Member, *, reason=None):
    warn = False
    if "PDG" in str(ctx.message.author.roles):
        warn = True
        pass
    elif "*" in str(ctx.message.author.roles):
        warn = True
    else:
        warn = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if unmute == True:
        await member.send(f"Vous avez étais warn par {ctx.guild.name} raison : {reason}")
        await ctx.send(f"***{member.mention} à été warn pour : {reason} !***")
    else:
        pass

@bot.command()
async def pp(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()
async def geoip(ctx, *, ipadd):
    geoip = False
    if "Analyste" in str(ctx.message.author.roles):
        geoip = True
        pass
    elif "*" in str(ctx.message.author.roles):
        geoip = True
    else:
        geoip = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if geoip == True:
        r = requests.get(f'http://extreme-ip-lookup.com/json/{ipadd}')
        geo = r.json()
        IP = geo['query']
        ISP = geo['isp']
        Country = geo['country']
        City = geo['city']
        Region = geo['region']  
        ORG = geo['org']
        em = discord.Embed(description=f"**IP**: {ipadd}\n \n**AdresseIP**: ``{IP}``\n**Ville**: ``{City}``\n**Région**: ``{Region}``\n**Pays**: ``{Country}``\n**ISP**: ``{ISP}``\n**ORG**: ``{ORG}``", color=0x00ff00)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/744132540998221864/748121107764084856/51zdsrq20LL.png")
        await ctx.send(f"https://techcrunch.com/wp-content/uploads/2019/01/tracking-phones.gif")
        await ctx.send(embed=em)
    else:
        pass

@bot.command()
async def nmap(ctx, arg1):
    nmap = False
    if "Analyste" in str(ctx.message.author.roles):
        nmap = True
        pass
    elif "*" in str(ctx.message.author.roles):
        nmap = True
        pass
    else:
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if nmap == True:
        scanyuh = get(f"https://api.hackertarget.com/nmap/?q={arg1}")
        result = scanyuh.text.strip(" ( https://nmap.org/ )")
        em = discord.Embed(title=f"Nmap", description=f"**{result}**", color=0x00ff00)
        await ctx.send(embed=em)
    else:
        pass

@bot.command()
async def reconng(ctx):
    reconng = False
    if "Analyste" in str(ctx.message.author.roles):
        reconng = True
        pass
    elif "*" in str(ctx.message.author.roles):
        reconng = True
        pass
    else:
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if reconng == True:
        result = os.popen('gnome-terminal ~/recon-ng/recon-ng')
        await ctx.send('ok')
    else:
        pass

@bot.command()
async def whatweb(ctx, arg1):
    whatweb = False
    if "Analyste" in str(ctx.message.author.roles):
        whatweb = True
        pass
    elif "*" in str(ctx.message.author.roles):
        reconng = True
        pass
    else:
        whatweb = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if whatweb == True:
        scanyuh = get(f"https://api.hackertarget.com/whatweb/?q={arg1}")
        result = scanyuh.text.strip(" ( https://github.com/urbanadventurer/WhatWeb )")
        em = discord.Embed(title=f"WhatWeb", description=f"**{result}**", color=0x00ff00)
        await ctx.send(embed=em)
    else:
        pass

@bot.command()
async def cve(ctx, arg1):
    cve = False
    if "Analyste" in str(ctx.message.author.roles):
        cve = True
        pass
    elif "*" in str(ctx.message.author.roles):
        reconng = True
        pass
    else:
        cve = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if cve == True:
        scanyuh = get(f"https://api.cvesearch.com/search?q={arg1}")
        result = scanyuh.text.strip(" ( https://github.com/urbanadventurer/WhatWeb )")
        em = discord.Embed(title=f"CVE", description=f"**{result}**", color=0x00ff00)
        await ctx.send(embed=em)
    else:
        pass

@bot.command()
async def theharvester(ctx, *text):
    #directory : C:\theHarvester
    theharvester_args = False
    theharvester == False

    if "Analyste" in str(ctx.message.author.roles):
        theharvester = True
        pass
    elif "*" in str(ctx.message.author.roles):
        theharvester = True
        pass
    else:
        theharvester = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if "-h" in text:
        theharvester_args = True
        pass
    elif ' ' in text:
        print(text)
        await ctx.send('aucun argument')
    else:
        theharvester_args = True

    if theharvester == True:
        if theharvester_args == True:
            print(text)
            print('ok')
            await ctx.send('ok')
            await ctx.send(text)
            
            arg = text[0]
            info = text[1]
            command = f'thearvester {arg} {info}'
            em = discord.Embed(title='theHarvester', description=f'command : {command}', color=0x00ff00)
            await ctx.send(embed=em)
        else:
            pass
        
    else:
        pass

@bot.command()
async def finalrecon(ctx, host):
    finalrecon = False
    if "Analyste" in str(ctx.message.author.roles):
        finalrecon = True
        pass
    elif "*" in str(ctx.message.author.roles):
        finalrecon = True
        pass
    else:
        finalrecon = False
        await ctx.send("vous n'avez pas les perm requis .")
        pass

    if finalrecon == True:
        if "linux" in sys.platform:
            site = host
            em0 = discord.Embed(title='FinalRecon', description=f'wait ...', color=0x00ff00)
            await ctx.send(embed=em0)
            result = os.popen(f'python3 /FinalRecon/finalrecon.py https://{site} --headers --sslinfo --whois --dns --trace --ps').read()
            print(result)
            
            with open(f'/root/.local/share/finalrecon/dumps/{host}.txt', "rb") as file:
                await ctx.send("result : ", file=discord.File(file, f"{host}.txt"))
            
        else:
            await ctx.send('```use linux machine for finalrecon .```')
    else:
        pass

@bot.command()
async def roles(ctx):
    roles = ctx.message.author.roles
    """
    for char in roles:
        if char in " ?.!/;:":
            roles.replace(char,'')
    """
    print(roles)
    em = discord.Embed(title=f'users roles', description=f'{roles}', color=0x00ff00)
    await ctx.send(embed=em)

@bot.command()
async def test(ctx):
    em = discord.Embed(title=f"test perm", description=f"**ok**", color=0x00ff00)
    await ctx.send(embed=em)

@bot.command()
async def testA(ctx):
    #print(ctx.message.guild.roles)
    username = ctx.message.author.name
    file_name = f"{str(username)}.txt"
    file_name = file_name.split('"')[1]
    guild = ctx.guild
    print(file_name)
    open(file_name, 'a').close()
    #role_id = 301768450282356737
    #role = get(guild.roles, id=role_id)
    #print(role)

    ctx_roles = ctx.message.author.roles

    if "Développeur" in str(ctx.message.author.roles):
        await ctx.send('ok Développeur')
    else:
        await ctx.send('Développeur non')

    em = discord.Embed(title=f"info", description=f"**name : {ctx.author}\nid : {ctx.author.id}\nroles : {ctx_roles}**", color=0x00ff00)

    await ctx.send(embed=em)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(pass_context=True)
async def leave (ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

bot.run(TOKEN)
