import discord
from discord import app_commands
from discord.ext import commands

def setup_stake_command(bot: commands.Bot):
    @bot.tree.command(name="stake", description="Stake NFTs to earn $HAZE")
    async def stake(interaction: discord.Interaction):
        await interaction.response.send_message("🔒 Staking logic coming soon!", ephemeral=True)
