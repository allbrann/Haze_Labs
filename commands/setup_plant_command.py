
import discord
from discord import app_commands

def setup_plant_command(bot):
    @bot.tree.command(name="plant", description="Plant a seed in your grow room")
    async def plant(interaction: discord.Interaction):
        await interaction.response.send_message("🌱 Seed planted! (Placeholder logic)", ephemeral=True)
