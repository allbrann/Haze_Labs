
import discord
from discord.ui import View, Button

class StartView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="🧪 How to Play", style=discord.ButtonStyle.primary, custom_id="how_to_play"))
        self.add_item(Button(label="🌱 Buy Seeds", style=discord.ButtonStyle.success, custom_id="buy_seeds"))
        self.add_item(Button(label="🎒 Inventory", style=discord.ButtonStyle.secondary, custom_id="inventory"))
