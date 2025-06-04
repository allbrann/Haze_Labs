
import discord
from discord import app_commands

def setup_roll_command(bot):
    @bot.tree.command(name="roll", description="Roll joints using harvested buds")
    async def roll(interaction: discord.Interaction):
        await interaction.response.send_message("💨 Rolled 10 joints! (Placeholder logic)", ephemeral=True)
