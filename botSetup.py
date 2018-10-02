# Discord Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

# Load Bot
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Initialize Client
client = Bot('')
