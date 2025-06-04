
import discord
from discord import app_commands

def setup_harvest_command(bot):
    @bot.tree.command(name="harvest", description="Harvest your grown crops")
    async def harvest(interaction: discord.Interaction):
        await interaction.response.send_message("🌾 Harvest complete! (Placeholder logic)", ephemeral=True)
