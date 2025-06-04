import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from commands.setup_start_command import setup_start_command
from commands.setup_plant_command import setup_plant_command
from commands.setup_harvest_command import setup_harvest_command
from commands.setup_water_command import setup_water_command
from commands.setup_blaze_command import setup_blaze_command
from commands.setup_roll_command import setup_roll_command
from commands.setup_inventory_command import setup_inventory_command
# from commands.setup_stake_command import setup_stake_command

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Logged in as {bot.user} and synced slash commands.")

# Register all slash commands
setup_start_command(bot)
setup_plant_command(bot)
setup_harvest_command(bot)
setup_water_command(bot)
setup_blaze_command(bot)
setup_roll_command(bot)
setup_inventory_command(bot)
# setup_stake_command(bot)

# Load environment and run
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Missing DISCORD_BOT_TOKEN environment variable")
bot.run(TOKEN)
