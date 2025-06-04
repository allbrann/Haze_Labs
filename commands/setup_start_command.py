
import discord
from discord import app_commands
from views.startview import StartView

def setup_start_command(bot):
    @bot.tree.command(name="start", description="Launch the Kush Kings Lab guide")
    async def start(interaction: discord.Interaction):
        embed = discord.Embed(
            title="👑 Welcome to the Kush Kings Haze Labs",
            description=(
                "Step into the smoke-filled labs of Kush Kings — where rogue growers, high-tech rollers, "
                "and THC alchemists hustle to dominate.\n\n"
                "Plant elite strains, climb the leaderboard, and earn J-Points to win real prizes at the end of each season.\n"
                "Link your wallet, build your empire, and blaze through syndicates.\n\n"
                "🌱 Grow | 🔥 Blaze | 👑 RULE THE HAZE.\n\n"
                "═══════════════════════════════════\n"
                "🧪 **HAZE LABS – HOW TO PLAY**\n"
                "Powered by $HAZE on WAX Blockchain\n"
                "═══════════════════════════════════"
            ),
            color=0x6f42c1
        )
        embed.set_footer(text="🧠 TIP: Stack all 3 characters for max buffs!")
        await interaction.response.send_message(embed=embed, view=StartView(), ephemeral=True)
