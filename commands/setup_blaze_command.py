
import discord
from discord import app_commands

def setup_blaze_command(bot):
    @bot.tree.command(name="blaze", description="Blaze joints to earn points")
    async def blaze(interaction: discord.Interaction):
        await interaction.response.send_message("🔥 Blazed and earned 200 J-Points! (Placeholder logic)", ephemeral=True)
