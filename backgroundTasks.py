import random
import asyncio
from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()

async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]["red orbs"] = 0
        users[str(user.id)]["level"] = 1

async def add_red_orbs(users, user, red_orbs):
    users[str(user.id)]["red orbs"] += red_orbs    

def get_red_orbs(users, user):
    if str(user.id) in users:
        return users[str(user.id)]["red orbs"]
    return 0

#<:redorb:729815039329959947>