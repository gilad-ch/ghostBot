import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL_ID = os.getenv('WELCOME_CHANNEL_ID')
ROLE_ID = os.getenv('ROLE_ID')

if not TOKEN or not WELCOME_CHANNEL_ID:
    raise ValueError('DISCORD_TOKEN and WELCOME_CHANNEL_ID must be set in the .env file.')

WELCOME_CHANNEL_ID = int(WELCOME_CHANNEL_ID)
if ROLE_ID:
    print(f"ROLE_ID: {ROLE_ID}")
    ROLE_ID = int(ROLE_ID)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_member_join(member):
    if ROLE_ID:
        role = member.guild.get_role(ROLE_ID)
        if role:
            try:
                await member.add_roles(role, reason="Auto-assigned by bot on join.")
            except discord.Forbidden:
                print(f"Missing permissions to assign role {role.name} to {member}.")
            except Exception as e:
                print(f"Error assigning role: {e}")
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await asyncio.sleep(5)
        msg = await channel.send(f"ממליץ לך לקרוא {member.mention}")
        await asyncio.sleep(2)
        await msg.delete()

bot.run(TOKEN) 