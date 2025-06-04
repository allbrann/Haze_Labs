
import discord
from discord import app_commands

def setup_water_command(bot):
    @bot.tree.command(name="water", description="Water your active grow")
    async def water(interaction: discord.Interaction):
        await interaction.response.send_message("💧 Plant watered! (Placeholder logic)", ephemeral=True)
